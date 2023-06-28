#!/usr/bin/python3
"""
Task 5: Write a function that writes an Object
to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """write a text using json"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)

# 1: dump used to write JSON representation of my_object on file
