#!/usr/bin/python3
from add_0 import add

def hola():
    # a and b must be defined in 2 different lines: a = 1 and another b = 2
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

# Your code should not be executed when imported - by using __import__
if __name__ == "__main__":
    hola()
