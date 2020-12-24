from constraint import Problem, BacktrackingSolver


class GardenSolver:
    def __init__(self):
        self.problem = Problem(BacktrackingSolver())
        self.add_constraints()

    def add_constraints(self):
        return

    def solve(self):
        return self.problem.getSolutions()
