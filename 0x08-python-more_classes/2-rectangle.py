#!/usr/bin/python3
"""
Module Rectangle
"""


class Rectangle:
    """
    Class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        init
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        property
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        property
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        setter
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
