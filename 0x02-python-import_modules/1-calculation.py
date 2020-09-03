#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
# You are not allowed to use * for importing or __import__


def main():
    # a and b must be defined in 2 different lines: a = 10 and another b = 5
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
# Your code should not be executed when imported
if __name__ == "__main__":
    main()
