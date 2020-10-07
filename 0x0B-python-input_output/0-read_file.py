#!/usr/bin/python3
""" Module """


def read_file(filename=""):
    """ read file """
    with open(filename, "r") as file:
        text = file.read()
    print("{}".format(text))
    file.close()
