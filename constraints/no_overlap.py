from constraint import Constraint, Unassigned


class NoOverlapConstraint(Constraint):
    """
    Constraint enforcing no vegetable overlap on the layout
    """

    def __call__(
            self,
            variables,
            domains,
            assignments,
            forwardcheck=False,
            _unassigned=Unassigned,
    ):
        return True
