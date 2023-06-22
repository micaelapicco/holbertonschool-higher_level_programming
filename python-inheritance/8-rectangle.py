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
