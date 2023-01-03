# ©2022, ANSYS Inc. Unauthorized use, distribution or duplication is prohibited.

from ansys.saf.glow.solution import StepModel, StepSpec, transaction


class FirstStep(StepModel):
    """First step."""
    first_arg: float = 0
    second_arg: float = 0
    result: float = 0

    @transaction(self=StepSpec(upload=["result"], download=["first_arg", "second_arg"]))
    def calculate(self) -> None:
        """Method to compute the sum of two numbers."""
        self.result = self.first_arg + self.second_arg
