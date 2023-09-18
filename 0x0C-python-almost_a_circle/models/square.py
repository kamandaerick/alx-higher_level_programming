#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square

    Args:
        Rectangle (class): Parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor

        Args:
            size (int): Size of the square
            x (int): x-cordinate of the square. Defaults to 0.
            y (int): y-cordinate if the square. Defaults to 0.
            id : the id f the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The str method of the square

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter"""
        return self.width
    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def display(self):
        """Display the square"""
        for i in range(self.y):
            print()

        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Udate the class Square"""
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
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
