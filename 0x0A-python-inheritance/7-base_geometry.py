#!/usr/bin/python3

"""Represents the BaseGeometry class."""


class BaseGeometry:
    """Represents the BaseGeometry class."""


    def area(self):
        """Calculates the area of the geometry. Currently not implemented."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value."""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
