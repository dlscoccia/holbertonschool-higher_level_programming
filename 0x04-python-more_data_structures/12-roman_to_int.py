#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or len(roman_string) is 0:
        return 0
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    number = 0
    for i in roman_string:
        if i == 'I':
            number += 1
        elif i == 'V':
            number += 5
        elif i == 'X':
            number += 10
        elif i == 'L':
            number += 50
        elif i == 'C':
            number += 100
        elif i == 'D':
            number += 500
        elif i == 'M':
            number += 1000
    return (number)
