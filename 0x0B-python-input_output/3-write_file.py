#!/usr/bin/python3
""" module """


def write_file(filename="", text=""):
    """ write file """
    with open(filename, "w") as file:
        chars = file.write(text[:])
    return chars
