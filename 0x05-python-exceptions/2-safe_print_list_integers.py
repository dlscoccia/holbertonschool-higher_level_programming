#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    number = ""
    for element in range(x):
            try:
                print("{:d}".format(my_list[element]), end="")
                counter += 1
            except (TypeError, ValueError):
                continue
    print("")
    return counter
