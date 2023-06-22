#!/usr/bin/python3
"""
Task 9: Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle inherit base geometry"""

    def __init__(self, width, height):
        """width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """print a rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
