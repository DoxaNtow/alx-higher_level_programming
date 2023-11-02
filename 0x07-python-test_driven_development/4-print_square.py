#!/usr/bin/python3
"""
This module is responsible for printing a square using the character '#'.
"""

def print_square(size):
    """
    Prints a square with the character '#' of the specified size.

    Args:
        size (int): The length of one side of the square.

    Raises:
        TypeError: If the 'size' parameter is not an integer.
        ValueError: If the 'size' parameter is less than 0.
        TypeError: If the 'size' parameter is a float and is less than 0.

    Returns:
        None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
