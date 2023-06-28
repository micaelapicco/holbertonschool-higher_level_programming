#!/usr/bin/python3
"""
Task 4: Write a function that returns an object
(Python data structure) represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """from json to string"""
    python_str = json.loads(my_str)
    return (python_str)

# 1: json.loads converter json into python object
