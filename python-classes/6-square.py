#!/usr/bin/python3
""" Class Square,size & area of square"""


class Square:
    """define size of square"""

    def __init__(self, size=0, position=(0, 0)):
        """if size is not type int or > 0, errors:"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set errors of position"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            print("{}{}".format(" " * self.position[0], "#" * self.size))
