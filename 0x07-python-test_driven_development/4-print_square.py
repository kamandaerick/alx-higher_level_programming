#!/usr/bin/python3
"""
    This module prints a square of the dimension
    passed to the function print_square() as an argument.
    if size is less than 0, it raises a value error and if
    it is not an int, it raises a Typeerror
"""


def print_square(size):
    """

    Args:
        size (int): the size of the square

    Raises:
        TypeError: error raised if size is not an integer
        ValueError: error raised if size is less than 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        size = int(size)
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
