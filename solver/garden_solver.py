from typing import List
import numpy as np
from constraint import Problem, BacktrackingSolver, RecursiveBacktrackingSolver, MinConflictsSolver

from constraints.alignment import AlignmentConstraint
from constraints.filling import FillingRatioConstraint
from constraints.no_overlap import NoOverlapConstraint

from model.vegetable import Vegetable


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


class FillingConstraint():
    # TODO: we can first try with n = number of veggies and then incrementally relax the constraint till we find a sol

    def __init__(self, n: int, not_used_val: int = -1000):
        self.n = n
        self.not_used_val = not_used_val

    def is_filled(self, *vars):
        outside = 0
        for v in vars:
            if v == self.not_used_val:
                outside += 1
        inside = len(vars) - outside
        return inside >= self.n


class PackingConstraint():

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


    def is_packed(self, *vars):
        # TODO: this is too complex (too long)
        xs = vars[(len(vars) // 2):]
        ys = vars[:(len(vars) // 2)]
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


class GardenSolver:
    NOT_USED = -1000

    def __init__(self,
                 height: int,
                 width: int,
                 vegetables: List[int],
                 ):

        # Making sure the garden is not a single point or empty
        assert width >= 2 and height >= 2

        self.problem = Problem(solver=BacktrackingSolver())
        self.add_variables(height, width, vegetables)
        self.add_constraints(height, width, vegetables)

    def add_variables(self,
                      height: int,
                      width: int,
                      vegetables: List[int]
                      ):
        x_domain = [i for i in range(0, width)] + [GardenSolver.NOT_USED]
        y_domain = [i for i in range(0, height)] + [GardenSolver.NOT_USED]
        for v in vegetables:
            self.problem.addVariable(f"x_{v}", x_domain)
            self.problem.addVariable(f"y_{v}", y_domain)

    def add_constraints(self,
                        height: int,
                        width: int,
                        vegetables: List[int],
                        N: int = None):

        veggies_dict = Vegetable.get_vegetable_list_by_id("../list_vegetables.json")
        for i in vegetables:
            for j in vegetables:
                if i != j:
                    v_i = veggies_dict[i]
                    v_j = veggies_dict[j]
                    align_constr = PositionalConstraint(v_i.shape_width, v_j.shape_width, v_i.shape_height,
                                                        v_j.shape_height, width, height)
                    self.problem.addConstraint(align_constr.is_well_positioned,
                                               (f"x_{i}", f"x_{j}", f"y_{i}", f"y_{j}"))

        if N is None:
            N = len(vegetables)
        xs = []
        ys = []
        for v in vegetables:
            xs.append(f"x_{v}")
            ys.append(f"y_{v}")
        filling_constr = FillingConstraint(N, GardenSolver.NOT_USED)
        self.problem.addConstraint(filling_constr.is_filled, tuple(xs))
        self.problem.addConstraint(filling_constr.is_filled, tuple(ys))

        vegetables_width = []
        vegetables_height = []
        for v in vegetables:
            vegetables_width.append(veggies_dict[v].shape_width)
            vegetables_height.append(veggies_dict[v].shape_height)

        packing_constr = PackingConstraint(vegetables, vegetables_width, vegetables_height,
                                           width, height, GardenSolver.NOT_USED)
        self.problem.addConstraint(packing_constr.is_packed, (xs + ys))

    def solve(self):
        return self.problem.getSolutionIter()


if __name__ == "__main__":
    garden_solver = GardenSolver(10, 10, [1, 2, 3])
    res = garden_solver.solve()
    for i in res:
        print(i)
        break
