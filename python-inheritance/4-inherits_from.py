#!/usr/bin/python3
"""4-inherits from Module"""


def inherits_from(obj, a_class):
    """inherit direct or indirect"""
    return isinstance(obj, a_class) and type(obj) is not a_class
