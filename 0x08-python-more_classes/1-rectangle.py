#!/usr/bin/python3
""" Module Rectangle """


class Rectangle:
    """ Class Rectangle """
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
        return self.__width

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
        return self.__height

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
