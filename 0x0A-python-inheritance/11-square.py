#!/usr/bin/python3
"""Defines a Square class that is a subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square with equal width and height.

    Args:
        Rectangle (class): The class being inherited from.
    """

    def __init__(self, size):
        """Initialize a new square with the given size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)  # Validate and set the size.
        super().__init__(size, size)  # Initialize the squaret.
        self.__size = size  # Store the size as a private attribute.
