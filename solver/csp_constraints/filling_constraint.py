class FillingConstraint():

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
