#!/usr/bin/python3
""" Module """


class BaseGeometry():
    """ class BaseGeometry """
    pass

    def area(self):
        """ area method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validator method """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0.".format(name))


class Rectangle(BaseGeometry):
    """ class retangle """
    def __init__(self, width, height):
        """ init """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ class square """
    def __init__(self, size):
        """ init """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ str method """
        return ("[Square] {}/{}".format(self.__size, self.__size))
