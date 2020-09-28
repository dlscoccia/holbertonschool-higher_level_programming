#!/usr/bin/python3
"""
Square class docstring
"""


class Square:
    """
    init square class with size
    """
    def __init__(self, size=0):
        """
        def init
        """
        self.size = size

    @property
    def size(self):
        """
        size property
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        area method
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        print square method
        """
        if self.__size == 0:
            print("")
        row = 0
        for row in range(0, self.__size):
            column = 0
            for column in range(0, self.__size):
                print("#", end="")
            print("")
