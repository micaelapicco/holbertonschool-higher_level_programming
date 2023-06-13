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
        if not type(position) == tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not position[0] == int and not position[1] == int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not position[0] >= 0 and not position[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """set errors of size"""
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if not value >= 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate size of square """
        return (self.__size ** 2)

    def my_print(self):
        """Print square"""
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
        """Set errors of position"""
        if not type(value) == tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not value[0] == int and not value[1] == int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not value[0] >= 0 and not value[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
