#!/usr/bin/python3

"""Divides each element of a matrix by a divisor and returns a new matrix."""


def matrix_divided(matrix, div):

    """
    Divides each element of a matrix by a divisor and returns a new matrix.

    Args:
    - matrix: List of lists containing ints or floats.
    - div: Non-zero int or float divisor.

    Returns:
    - New matrix with divided values, rounded to 2 decimal places.

    Raises:
    - TypeError: For invalid matrix or div types or mismatched row sizes.
    - ZeroDivisionError: If div is 0.
    """

    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix(list of lists) of"
                        "integers/floats")
    for i in matrix:
        if type(i) != list or len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of"
                            "integers/floats")
        for num in i:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of"
                                "integers/floats")

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
