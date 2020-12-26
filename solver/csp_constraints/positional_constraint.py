class PositionalConstraint():

    def __init__(self, w1, w2, h1, h2, width, height, not_used_val: int = -1000):
        self.w1 = w1
        self.w2 = w2
        self.h1 = h1
        self.h2 = h2
        self.width = width
        self.height = height
        self.not_used_val = not_used_val

    def is_well_positioned(self, x1, x2, y1, y2):
        r1_left = x1
        r2_left = x2
        r1_top = y1
        r2_top = y2
        r1_right = x1 + self.w1
        r2_right = x2 + self.w2
        r1_bottom = y1 + self.h1
        r2_bottom = y2 + self.h2
        return self._inside_garden(r1_left, r1_right, r1_top, r1_bottom) and \
               self._inside_garden(r2_left, r2_right, r2_top, r2_bottom) and \
               self._is_not_overlapping(r1_left, r1_right, r1_top, r1_bottom,
                                        r2_left, r2_right, r2_top, r2_bottom)

    def _is_not_overlapping(self, r1_left, r1_right, r1_top, r1_bottom,
                            r2_left, r2_right, r2_top, r2_bottom):

        return r2_left > r1_right or r2_right < r1_left or r2_top > r1_bottom or r2_bottom < r1_top

    def _inside_garden(self, r1_left, r1_right, r1_top, r1_bottom):
        if r1_left == self.not_used_val:
            return True
        else:
            return r1_left >= 0 and r1_top >= 0 and r1_bottom <= self.height and r1_right <= self.width
