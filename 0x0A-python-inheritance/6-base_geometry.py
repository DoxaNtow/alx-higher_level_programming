#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry class with an unimplemented 'area' method.

    Attributes:
        None

    Methods:
        area(self): Raises an exception.
    """

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
