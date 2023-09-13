#!/usr/bin/python3
"""Import class Rectangle from '9-rectangle' module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a class Square that inherits from Rectanggle

    Args:
        Rectange (class): parent class
    """
    def __init__(self, size):
        """Square class initializer

        Args:
            size (int): size of the side of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate and return area

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """Definition of the str method"""
        return (f"[Square] {self.__size}/{self.__size}")
