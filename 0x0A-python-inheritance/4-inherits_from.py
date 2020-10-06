#!/usr/bin/python3
""" Module """


def inherits_from(obj, a_class):
    """ inherits from """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
