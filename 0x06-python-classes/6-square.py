#!/usr/bin/python3
"""
Square class docstring
"""


class Square:
    """
    init square class with size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        def init
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        size property
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        position setter
        """
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int \
           or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        if self.__position[1] > 0:
            for x in range(0, self.__position[1]):
                print("")
        row = 0
        for row in range(0, self.__size):
            column = 0
            i = 0
            for i in range(0, self.__position[0]):
                print(" ", end="")
            for column in range(0, self.__size):
                print("#", end="")
            print("")
