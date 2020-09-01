#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
less = "and is less than 6 and not 0"
mod_neg = (number * -1) % 10
mod_n = number % 10

if mod_n == 0:
    print("{:s} {:d} is {:d} and is 0".format(str, number, mod_n))
elif number < 0 and mod_neg != 0:
    print("{:s} {:d} is -{:d} {:s}".format(str, number, mod_neg, less))
elif mod_n > 0 and mod_n < 6:
    print("{:s} {:d} is {:d} {:s}".format(str, number, mod_n, less))
elif mod_n > 5:
    print("{:s} {:d} is {:d} and is greater that 5".format(str, number, mod_n))
