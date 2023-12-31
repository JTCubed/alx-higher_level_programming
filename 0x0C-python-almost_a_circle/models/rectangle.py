#!/usr/bin/python3
"""
Rectangle claass
defines a rectangle by methods to print, update, validate and calculate
the area
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initiates the Rectangle attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return width as a private instance"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the validators for the width arguments"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return height as a private instance"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """sets the validators for the height arguments"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return x as a private instance"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets the validators for the x arguments"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return y as a private instance"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets the validators for the y arguments"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area/ height * width"""
        return (self.__height * self.__width)

    def display(self):
        """
        prints the rectangle
        to stdout
        """
        for line in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for r in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        returns [Rectangle] (<id>)
        <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x,
                        self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by improving the public
        method to print
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])

        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representaion of Rectangle"""
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}
