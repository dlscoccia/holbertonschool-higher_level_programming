#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    numbers = ""
    for element in range(0, x):
        try:
            numbers += str(my_list[element])
        except IndexError:
            break
        counter += 1
    print(numbers)
    return (counter)
