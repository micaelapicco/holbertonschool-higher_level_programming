#!/usr/bin/python3
"""
Task 10: Write a class Square that inherits from Rectangle (9-rectangle.py):
"""

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
