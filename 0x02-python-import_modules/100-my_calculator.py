#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = sys.argv[2]
    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif sys.argv[2] == "+":
        result = add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "-":
        result = sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == "*":
        result = mul(int(sys.argv[1]), int(sys.argv[3]))
    else:
        result = div(int(sys.argv[1]), int(sys.argv[3]))
    print("{} {} {} = {}".format(sys.argv[1], op, sys.argv[3], result))
