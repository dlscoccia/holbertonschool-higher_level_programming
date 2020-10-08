#!/usr/bin/python3
""" module """
import json


def save_to_json_file(my_obj, filename):
    """ json to file """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
