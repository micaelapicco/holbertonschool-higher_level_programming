#!/usr/bin/python3
"""Simple rectangle"""


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

    def area(self):
        """calculate area"""
        return (self.width * self.height)

    def perimeter(self):
        """calculate the perimeter"""
        if self.height == 0 or self.width == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Returns the rectangle in string format"""
        rectangle = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                rectangle += "#" * self.width
                if i != self.height - 1:
                    rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """string representacion a new instance"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """delete mesagge"""
        print("Bye rectangle...")
