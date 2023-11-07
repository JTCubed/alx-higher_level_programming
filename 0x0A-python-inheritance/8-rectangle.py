#!/usr/bin/python3

"""Represents the BaseGeometry class."""


class BaseGeometry:
    """Represents the BaseGeometry class."""

    def area(self):
        """Calculates the area of the geometry. Currently not implemented."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integers as positive and ints"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """New added attributes"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
