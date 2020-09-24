#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as exception:
        sys.stderr.write("Exception: " + str(exception) + "\n")
        return None
