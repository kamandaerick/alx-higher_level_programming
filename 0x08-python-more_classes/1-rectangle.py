#!/usr/bin/python3
"""
    _summary_
    This proect involves creation of a class Rectangle the define a Rectangle.
    Importing modules is not allowed at all.__annotations__
"""


class Rectangle:
    """The definition of the class Rectangle"""
    def __init__(self, width=0, height=0):
        """
        The __init__() method initializes instances of the class.

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

    @property
    def height(self):
        """
        Height getter method

        Returns:
            int: Returns the height (int) of the rectangle
        """
        return self.__height

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
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

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
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
