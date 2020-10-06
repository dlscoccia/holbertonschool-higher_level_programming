#!/usr/bin/python3
""" Module """


class MyInt(int):
    """ class MyInt """
    def __eq__(self, other):
        """ eq method """
        return (int(self) != int(other))

    def __ne__(self, other):
        """ ne method """
        return (int(self) == int(other))
