#!/usr/bin/python3
"""Defines a Square subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square.

    Args:
        Rectangle (class): The class being inherited from.
    """

    def __init__(self, size):
        """Initialize a new square with the given size.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)  # Validate and set the size.
        super().__init__(size, size)  # Initialize the square using the size.
        self.__size = size  # Store the size as a private attribute.
