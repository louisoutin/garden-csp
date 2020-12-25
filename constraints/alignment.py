from typing import List

from constraint import Constraint, Unassigned


class AlignmentConstraint(Constraint):
    """
    Constraint enforcing that vegetables are aligned on the layout
    """

    def __init__(self,
                 vegetables_id: List[int],
                 vegetables_width: List[int],
                 vegetables_height: List[int],
                 width: int,
                 height: int,
                 not_used_val: int = -1000):
        self.width = width
        self.height = height
        self.vegetables_id = vegetables_id
        self.vegetables_width = vegetables_width
        self.vegetables_height = vegetables_height
        self.not_used_val = not_used_val

    def _is_corner_touch(self,
                         top_touch,
                         bottom_touch,
                         left_touch,
                         right_touch):
        side_touch = left_touch or right_touch
        return (top_touch and side_touch) or (bottom_touch and side_touch)

    def __call__(
            self,
            variables,
            domains,
            assignments,
            forwardcheck=False,
            _unassigned=Unassigned,
    ):
        print(assignments)
        xs = assignments[(len(assignments) // 2):]
        ys = assignments[:(len(assignments) // 2)]
        for i in range(len(xs)):
            r1_left = xs[i]
            r1_top = ys[i]
            r1_right = xs[i] + self.vegetables_width[i]
            r1_bottom = ys[i] + self.vegetables_height[i]

            top_touch = False
            bottom_touch = False
            left_touch = False
            right_touch = False

            if r1_top == 0:
                top_touch = True
            if r1_bottom == self.height:
                bottom_touch = True
            if r1_left == 0:
                left_touch = True
            if r1_right == self.width:
                right_touch = True

            if self._is_corner_touch(top_touch, bottom_touch, left_touch, right_touch):
                continue  # we pass to the next rectangle object

            for j in range(len(xs)):
                if i != j:
                    r2_left = xs[j]
                    r2_top = ys[j]
                    r2_right = xs[j] + self.vegetables_width[j]
                    r2_bottom = ys[j] + self.vegetables_height[j]
                    # check that at least one corner of the current rectangle touch the wall or another rect
                    if r2_left <= r1_left < r2_right:
                        if r1_top == r2_bottom:
                            top_touch = True
                        if r1_bottom == r2_top:
                            bottom_touch = True
                    if r2_top <= r1_top < r2_bottom:
                        if r1_left == r2_right:
                            left_touch = True
                        if r1_right == r2_left:
                            right_touch = True

                    if self._is_corner_touch(top_touch, bottom_touch, left_touch, right_touch):
                        break  # we pass to the next rectangle object
            if not self._is_corner_touch(top_touch, bottom_touch, left_touch, right_touch):
                return False
        return True
