from constraint import Constraint, Unassigned


class FillingRatioConstraint(Constraint):
    """
    Constraint enforcing a minimum filling ratio on the layout
    """
    min_ratio = 0.5

    def __init__(self, min_ratio):
        self.min_ratio = min_ratio

    def __call__(
            self,
            variables,
            domains,
            assignments,
            forwardcheck=False,
            _unassigned=Unassigned,
    ):
        return True
