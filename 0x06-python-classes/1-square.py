#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The length of a side of the square.
    """

    def __init__(self, size):
        """Square constructor.

        Args:
            size (int): The length of a side of the square.
        """
        self.__size = size
