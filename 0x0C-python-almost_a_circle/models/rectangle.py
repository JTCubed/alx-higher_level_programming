#!/usr/bin/python3
from models.base import Base

"""
Rectangle claass
defines a rectangle by methods to print, update, validate and callculate
the area
"""


class Rectangle(Base):
    """
    Rectangle claass
    defines a rectangle by methods to print, update, validate and callculate
    the area
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        return (self.__height * self.__width)

    def display(self):
        for l in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for r in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x,
                        self.__y, self.__width, self.__height))


    def update(self, *args):
        attributes = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, attributes[i], args[i])
