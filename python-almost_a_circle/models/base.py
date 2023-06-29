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

    @staticmethod
    def to_json_string(list_dictionaries):
        """json representation of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save a file with json string"""
        if list_objs is None:
            l_objs = []
        else:
            l_objs = []
            for obj in list_objs:
                l_objs.append(obj.to_dictionary())
        file = cls.__name__ + ".json"
        with open(file, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(l_objs))
