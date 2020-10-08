#!/usr/bin/python3
''' Module '''


def print_square(size):
    ''' print squares everywhere '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        column = 0
        for column in range(size):
            print("#", end="")
        print("")
