#!/usr/bin/python3
"""
Class Reactangle
"""


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """
        init
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        property self
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        property self
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        area method
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        perimeter method
        """
        if ((self.__height == 0) or (self.__width == 0)):
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """
        str representation
        """
        if self.width == 0 or self.height == 0:
            return ""
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """
        str representation
        """
        return ("Rectangle({}, {})".format(self.width, self.height))
