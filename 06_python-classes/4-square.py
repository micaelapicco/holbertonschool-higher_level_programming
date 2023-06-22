#!/usr/bin/python3
"""
Task 4: Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """define size of square"""

    def __init__(self, size=0):
        """if size is not type int or > 0, errors:"""
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if not size >= 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if not value >= 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate size of square """
        return (self.__size ** 2)
