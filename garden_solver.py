from constraint import Problem, BacktrackingSolver

from constraints.alignment import AlignmentConstraint
from constraints.filling import FillingRatioConstraint


class GardenSolver:
    def __init__(self):
        self.problem = Problem(BacktrackingSolver())
        self.problem.addVariable("a", [1, 2, 3])
        self.problem.addVariable("b", [4, 5, 6])
        self.add_constraints()

    def add_constraints(self):
        self.problem.addConstraint(AlignmentConstraint())
        self.problem.addConstraint(FillingRatioConstraint(0.75))
        return

    def solve(self):
        return self.problem.getSolutions()
