#!/usr/bin/python3
"""
This module is designed for dividing elements within a matrix.
"""

def matrix_divided(matrix, div):
    """Divides all the elements of a matrix by a divisor.

    Args:
        matrix (list): A matrix, represented as a list of lists containing integers/floats.
        div (int or float): The divisor used for division.

    Returns:
        list: A new matrix with elements divided by the specified divisor.

    Raises:
        TypeError: If the matrix or its elements are not integers or floats.
        TypeError: If rows of the matrix have varying sizes.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    # Handling potential errors related to the matrix and its elements
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Handling potential errors related to the divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing elements and rounding to 2 decimal places
    divided_matrix = []
    for row in matrix:
        divided_row = [round(element / div, 2) for element in row]
        divided_matrix.append(divided_row)

    return divided_matrix
