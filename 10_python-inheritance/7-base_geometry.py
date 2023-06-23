#!/usr/bin/python3
"""
Task 7: Write a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """area exception"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
