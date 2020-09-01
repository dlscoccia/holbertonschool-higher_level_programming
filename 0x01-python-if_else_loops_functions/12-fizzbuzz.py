#!/usr/bin/python3
def fizzbuzz():
    i = 1
    while i <= 100:
        if (i % 3 == 0) and (i % 5 == 0):
            print("Fizzbuzz", end=" ")
        elif (i % 3 == 0):
            print("Fizz", end=" ")
        elif (i % 5 == 0):
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
        i = i + 1
