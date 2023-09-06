#!/usr/bin/python3
"""
This module adds two integers and returns the result


"""


def add_integer(a, b=98):
    """
    Args:
        a (int): first int to add
        b (int, 98): second int to add. Defaults to 98.

    Raises:
        TypeError: raised if a is not an int
        TypeError: raised if b is not an int

    Returns:
        int : the result of the sum of a and b
    """
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
