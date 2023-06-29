#!/usr/bin/python3
"""
Task 9: write the class rectagle that inherits from Base
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """inizialize class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """getter width"""
        return self.width

    @size.setter
    def size(self, value):
        """setter width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
