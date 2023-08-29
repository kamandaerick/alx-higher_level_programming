#!/usr/bin/python3
""" This is a shebang the runs python script using python3"""


class Square:
    """
    This is the definition of a class Square that has one instance called size
    """
    def __init__(self, size):
        """Constructor.
        Args:
            size: the length of one side of a square
        """
        self.__size = size
