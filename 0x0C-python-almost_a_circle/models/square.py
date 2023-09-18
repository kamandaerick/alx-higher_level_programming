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

    def display(self):
        """Display the square"""
        for i in range(self.y):
            print()

        for j in range(self.height):
            print(" " * self.x + "#" * self.width)
