#!/usr/bin/python3
""" module """
import json


def load_from_json_file(filename):
    """ load json """
    with open(filename, "r") as file:
        return json.load(file)
