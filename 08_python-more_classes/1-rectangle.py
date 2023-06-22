#!/usr/bin/python3
"""
Task 1: Write a class Rectangle that defines a rectangle by:
(based on 0-rectangle.py)
"""


class Rectangle:
    """definition of a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set errors of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set errors of heigth"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
