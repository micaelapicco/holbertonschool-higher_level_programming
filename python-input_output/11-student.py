#!/usr/bin/python3
"""
Task 11: Write a class Student that defines a student by:
first name, last name and age
"""


class Student:
    """student, first and last name, age"""

    def __init__(self, first_name, last_name, age):
        """set first, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """filter json"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """from a json file replace the atributes of a student"""
        return self.__dict__.update(json)
