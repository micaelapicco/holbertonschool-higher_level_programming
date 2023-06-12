#!/usr/bin/python3
""" Class Square and size of square"""


class Square:
    """define size of square"""

    def __init__(self, size=0):
        """if size is not type int or > 0, errors:"""
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if not size >= 0:
            raise ValueError("size must be >= 0")
        self.__size = size
