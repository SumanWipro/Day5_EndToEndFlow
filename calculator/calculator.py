"""Calculator class providing a unified interface for arithmetic operations."""

from . import operations


class Calculator:
    """A simple calculator supporting addition, subtraction, multiplication, and division."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        return operations.add(a, b)

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a minus b."""
        return operations.subtract(a, b)

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        return operations.multiply(a, b)

    def divide(self, a: float, b: float) -> float:
        """Return a divided by b.

        Raises:
            ValueError: If b is zero.
        """
        return operations.divide(a, b)
