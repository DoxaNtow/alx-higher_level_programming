#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry.

    Args:
        BaseGeometry (class): The class being inherited from.
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle with the given width and height.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)  # Validate and set width.
        self.__width = width  # Store the width as a private attribute.
        super().integer_validator("height", height)  # Validate and set height.
        self.__height = height  # Store the height as a private attribute.

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of a Rectangle.

        Returns:
            str: A string representing the class and its dimensions.
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
