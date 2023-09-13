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
        """Check if the value is an integer

        Args:
            name (string): variable name
            value (int): value of the variable

        Raises:
            TypeError: rased if value is not an integer
            ValueError: raised if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
