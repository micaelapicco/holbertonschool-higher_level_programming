#!/usr/bin/python3
"""
Task 1-14: empty class Base
"""

import json
from os.path import exists


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

    @staticmethod
    def from_json_string(json_string):
        """list of the json str representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return all attributes alredy set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 1)
        elif cls.__name__ == "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """list of instances"""
        filename = f"{cls.__name__}.json"
        if exists(filename):
            with open(filename, 'r', encoding="utf-8") as f:
                instances = cls.from_json_string(f.read())
                return (cls.create(**instance) for instance in instances)
        else:
            return []
