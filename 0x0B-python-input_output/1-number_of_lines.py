#!/usr/bin/python3
""" Module """


def number_of_lines(filename=""):
    """ number of lines """
    n_lines = 0
    with open(filename) as file:
        for line in file:
            n_lines += 1
    return n_lines
