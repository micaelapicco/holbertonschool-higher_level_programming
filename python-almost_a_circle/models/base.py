#!/usr/bin/python3
"""
Task 1: empty class Base
"""


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
