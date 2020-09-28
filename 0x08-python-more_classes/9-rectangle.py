#!/usr/bin/python3
"""
Class Reactangle
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        init
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """
        str representation
        """
        if self.width == 0 or self.height == 0:
            return ""
        fix = ((str(self.print_symbol) * self.width + "\n") * self.height)[:-1]
        return fix

    def __repr__(self):
        """
        str representation
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """
        del instance
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

    @classmethod
    def square(cls, size=0):
        """
        class method
        """
        return Rectangle(size, size)

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compare method
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2
