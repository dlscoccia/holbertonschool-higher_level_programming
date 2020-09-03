#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = sys.argv[1]
    op = sys.argv[2]
    b = sys.argv[3]

    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif sys.argv[2] == "+":
        print("{} {} {} = {}".format(a, op, b, add(int(a), int(b))))
    elif sys.argv[2] == "-":
        print("{} {} {} = {}".format(a, op, b, sub(int(a), int(b))))
    elif sys.argv[2] == "*":
        print("{} {} {} = {}".format(a, op, b, mul(int(a), int(b))))
    else:
        print("{} {} {} = {}".format(a, op, b, div(int(a), int(b))))
