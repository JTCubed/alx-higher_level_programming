#!/usr/bin/python3
"""a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a Square and inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        returns [Rectangle] (<id>)
        <x>/<y> - <width>/<height>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
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
