#!/usr/bin/python3
""" module """
import json


def to_json_string(my_obj):
    """ json to string """
    pyson = json.dumps(my_obj)
    return pyson
