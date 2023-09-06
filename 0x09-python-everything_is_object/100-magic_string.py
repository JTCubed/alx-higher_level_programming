#!/usr/bin/python3

"""returns a string “BestSchool” n times the number of the iteration"""


def magic_string():
    """returns a string “BestSchool” n times the number of the iteration"""
    magic_string.counter = getattr(magic_string, "counter", -1) + 1
    return ", ".join(["BestSchool"] * (magic_string.counter + 1))
