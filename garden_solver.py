from constraint import Problem, BacktrackingSolver


class GardenSolver:
    def __init__(self):
        self.problem = Problem(BacktrackingSolver())

    def solve(self):
        return self.problem.getSolutions()
