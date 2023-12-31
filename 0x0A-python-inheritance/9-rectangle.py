#!/usr/bin/python3

"""Represents the BaseGeometry class."""


class BaseGeometry:
    """Represents the BaseGeometry class."""

    def area(self):
        """Calculates the area of the geometry. Currently not implemented."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """inherits from BaseGeometry"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates the area"""

        return self.__width * self.__height

    def __str__(self):
        """
        Override the string representation for Square
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
