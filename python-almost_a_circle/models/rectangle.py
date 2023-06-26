#!/usr/bin/python3
"""
Task 2: write the class rectagle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__X = x
        self.__y = y
        super().__init__(id)


@property
def width(self):
    return self.__width


@width.setter
def width(self):
    self.__width = width


@property
def height(self):
    return self.__height


@height.setter
def height(self):
    self.__height = height


@property
def x(self):
    return self.__x


@x.setter
def x(self):
    self.__x = x


@property
def y(self):
    return self.__y


@x.setter
def y(self):
    self.__y = y
