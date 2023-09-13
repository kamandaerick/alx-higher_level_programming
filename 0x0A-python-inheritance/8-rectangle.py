#!/usr/bin/python3
"""Import BaseGeometry class from 7-base_geometry' module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
