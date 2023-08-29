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
            ValueError: the value of size is a negative
        """
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
