#!/usr/bin/python3
""" Class Square,size & area of square"""


class Square:
    """define size of square"""

    def __init__(self, size=0, position=(0, 0)):
        """if size is not type int or > 0, errors:"""
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if not size >= 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if not value >= 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate size of square """
        return (self.__size ** 2)

    def my_print(self):
        if self.size == 0:
            print()
        if self.position[1] > 0:
            for p in range(self.position[1]):
                print()
        for i in range(self.size):
            print("{}{}".format("_" * self.position[0], "#" * self.size))

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not value == int:
            raise TypeError("position must be a tuple of 2 positive integers")
