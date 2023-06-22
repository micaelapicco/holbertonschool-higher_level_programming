#!/usr/bin/python3
"""Base geometry inherit"""

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
