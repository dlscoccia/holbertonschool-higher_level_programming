#!/usr/bin/python3
""" create a new class Scuare """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ new class
        Args:
            Rectangle (class): Inheritance: from Base Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor
            Args:
                size (int): side of square
                x (int, optional): axis x. Defaults to 0.
                y (int, optional): axis y. Defaults to 0.
                id (int, optional): description. Defaults to None.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        This function returns the size (width)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            This function sets the size (width and height)
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ overloading
            Returns:
                str: string
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
        )
