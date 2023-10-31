#!/usr/bin/python3

"""Add two numbers together."""


def add_integer(a, b=98):
    """
    Add two numbers: a and b.
    a and b must be floats or integers.
    Raise a TypeError otherwise.
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
