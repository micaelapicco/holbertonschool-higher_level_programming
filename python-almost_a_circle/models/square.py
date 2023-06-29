#!/usr/bin/python3
"""
Task 9: write the class square that inherits from rectangle
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

    def update(self, *args, **kwargs):
        """updated args and kwards"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs.get(key)
                if key == "size":
                    self.size = kwargs.get(key)
                if key == "x":
                    self.x = kwargs.get(key)
                if key == "y":
                    self.y = kwargs.get(key)

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y

        }
