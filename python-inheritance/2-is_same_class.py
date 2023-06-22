#!/usr/bin/python3
"""
Task 2:Write a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """verified if obj is inistance of class"""
    return type(obj) is a_class
