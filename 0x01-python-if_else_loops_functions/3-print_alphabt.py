#!/usr/bin/python3
i = 97
while chr(i) <= 'z':
    if (chr(i) != 'e') and (chr(i) != 'q'):
        print("{}".format(chr(i)), end="")
    i = i + 1
