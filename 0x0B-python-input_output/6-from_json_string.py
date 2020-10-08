#!usr/bin/python3
""" module """
import json


def from_json_string(my_str):
    """ json to string """
    sonpy = json.loads(my_str)
    return sonpy
