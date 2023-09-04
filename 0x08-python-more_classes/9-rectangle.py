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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        The __init__() method initializes every instance of the class.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def update_symbol(cls, symbol):
        """Class method for updating print_symbol attribute"""
        cls.print_symbol = symbol

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares te sizes of two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns the square"""
        return cls(size, size)
