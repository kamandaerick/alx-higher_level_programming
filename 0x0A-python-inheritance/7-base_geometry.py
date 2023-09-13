#!/usr/bin/python3
"""Define an empty class BaseGeometry"""


class BaseGeometry:
    """An empty class BaseGeometry"""
    def area(self):
        """Define a function area

        Raises:
            Exception: raised since the area is nt defined
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
