#!/usr/bin/python3
"""
Task 8: Write a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """return dictonary for json seialization"""
    return (obj.__dir__)
