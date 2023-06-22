#!/usr/bin/python3
"""inherit from rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Based on Rectangle"""

    def __init__(self, size):
        """size check"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of square"""
        return (self.__size ** 2)

    def __str__(self):
        """print a rectangle"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
