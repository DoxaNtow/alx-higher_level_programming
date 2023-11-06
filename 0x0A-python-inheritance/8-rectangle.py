#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry Definition."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)  # Validate and set the width.
        self.__width = width  # Store the width as a private attribute.
        self.integer_validator("height", height)  # Validate and set the height.
        self.__height = height  # Store the height as a private attribute.
