#!/usr/bin/python3
"""
Task 2: write the class rectagle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if self.width != type(int):
            raise TypeError("width must be an integer")
        if self.width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if self.height != type(int):
            raise TypeError("height must be an integer")
        if self.height <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if self.x != type(int):
            raise TypeError("x must be an integer")
        if self.x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        if self.y != type(int):
            raise TypeError("y must be an integer")
        if self.y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
