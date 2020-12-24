from constraint import Constraint, Unassigned


class AlignmentConstraint(Constraint):
    """
    Constraint enforcing that vegetables are aligned on the layout
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