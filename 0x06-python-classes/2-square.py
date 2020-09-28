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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
