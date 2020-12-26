from typing import List

from constraint import Problem, BacktrackingSolver, RecursiveBacktrackingSolver, MinConflictsSolver

from model.vegetable import Vegetable
from solver.csp_constraints.positional_constraint import PositionalConstraint
from solver.csp_constraints.filling_constraint import FillingConstraint

#
#  Not Working (it seems it looks for too much possible solutions)
#  (The constraints might need to be written in a more clever way
#   with maybe using the assignement dict and the forward_check variable)
#


class GardenSolver:
    NOT_USED = -1000

    def __init__(self,
                 height: int,
                 width: int,
                 vegetables: List[int],
                 ):

        # Making sure the garden is not a single point or empty
        assert width >= 2 and height >= 2

        self.problem = Problem()
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

        veggies_dict = Vegetable.get_vegetables_by_id("../list_vegetables.json")
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

    def solve(self):
        return self.problem.getSolutionIter()


if __name__ == "__main__":
    garden_solver = GardenSolver(50, 50, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    res = garden_solver.solve()
    for i in res:
        print(i)
        break