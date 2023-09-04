#!/usr/bin/python3
"""
    This project involves creation of a class Rectangle
    Importing modules is not allowed at all.
    The class has two attributes
    1. width
    2. height
"""


class Rectangle:
    """
    The definition of the class Rectangle
    Private instance attributes:
        __width: the width of the rectangle
        __height: the height of the rectangle

    Properties:
        width: getter and setter for the width attribute
        height: getter and setter for the height attribute
    """
    def __init__(self, width=0, height=0):
        """
        The __init__() method initializes every instance of the class.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Width getter method

        Returns:
            int: Returns the width (int) of the object rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter method

        Args:
            value (int): The value of the width

        Raises:
            TypeError: Error thrown if width is not an int
            ValueError: Error thtown if width is a negative value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height getter method

        Returns:
            int: Returns the height (int) of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter method

        Args:
            value (int): The value if the height

        Raises:
            TypeError: Error thrown if the value of height is not an int
            ValueError: Error thrown is value of height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
