#!/usr/bin/python3
"""
Task 3 - Write a function that returns the
JSON representation of an object (string):
"""


import json


def to_json_string(my_obj):
    """object to json"""
    json_rep = json.dumps(my_obj)
    return json_rep

# 1 - json dumps converters str to a valid json
