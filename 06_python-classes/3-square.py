#!/usr/bin/python3
"""
Task 3: Write a class Square that defines a square by: (based on 2-square.py)
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

    def area(self):
        """ Calculate size of square """
        self.area = self.__size * self.__size
        return (self.area)
