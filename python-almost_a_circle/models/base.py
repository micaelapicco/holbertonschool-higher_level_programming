#!/usr/bin/python3
"""
Task 1-14: empty class Base
"""

import json


class Base():
    """Class base of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """json representation of dictionaries"""
        if list_dictionaries is None or list_dictionaries == 0:
            return ([])
        else:
            return json.dumps(list_dictionaries)
