#!/usr/bin/python3

"""Prints a square using the # symbol"""


def print_square(size):

    """
    Prints a square using the # symbol

    args: size. Determines the size of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#".format(), end="")
        print()
