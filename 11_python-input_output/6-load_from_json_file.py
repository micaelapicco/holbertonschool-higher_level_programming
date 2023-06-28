#!/usr/bin/python3
"""
Task 6: Write a function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """read file json and save on python"""
    with open(filename, 'r', encoding="utf-8") as file:
        json_data = file.read()
        python_obj = json.loads(json_data)
        return (python_obj)
