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
