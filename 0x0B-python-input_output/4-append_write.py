#!/usr/bin/python3
""" module """


def append_write(filename="", text=""):
    """ append file """
    with open(filename, "a") as file:
        chars = file.write(text[:])
    return chars
