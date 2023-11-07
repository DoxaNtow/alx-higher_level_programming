#!/usr/bin/python3
"""Defines a MyInt class that inherits from int."""


class MyInt(int):
    """Custom integer class that inverts the behavior of == and != operators.

    Args:
        int (class): The class being inherited from.
    """

    def __eq__(self, value):
        """Override the == operator to perform inequality comparison."""
        return self.real != value

    def __ne__(self, value):
        """Override the != operator to perform equality comparison."""
        return self.real == value
