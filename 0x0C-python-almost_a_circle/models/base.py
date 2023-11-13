#!/usr/bin/python3

"""
Class Base
"""


class Base:
    """
    The superclass initiated
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id =id
            __nb_objects =+ 1
            id = __nb_objects
