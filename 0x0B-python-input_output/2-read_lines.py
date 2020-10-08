#!/usr/bin/python3
""" module """


def read_lines(filename="", nb_lines=0):
    """ read n lines """
    n = 0
    text = ""
    with open(filename) as file:
        if nb_lines <= 0:
            text = file.read()
            print("{:s}".format(text))
        else:
            for line in range(nb_lines):
                text = file.readline()
                print("{:s}".format(text[:-1]))
