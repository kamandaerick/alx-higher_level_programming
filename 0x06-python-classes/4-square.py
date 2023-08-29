#!/usr/bin/python3
"""Definition os a class and its private instance"""


class Square:

    """The definition of a class called Square"""
    def __init__(self, size=0):
        """
        Constructor.
        Args:
            size(int): the length of the sides of the square
        Raises:
            TypeError: the value of size is not an integer
            ValueError: the value of size is a negativie
        """
        self.__size = size

    @property
    def size(self):
        """Getter => getting the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter => Setting the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This method calculates the area of a given square object.
        Return: returns the area of the square
        """
        return self.__size * self.__size
