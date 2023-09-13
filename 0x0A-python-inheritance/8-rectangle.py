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
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """Definition of a class Rectangle that is a child of BAseGeometry"""
    def __init__(self, width, height):
        """Initialize the class Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
