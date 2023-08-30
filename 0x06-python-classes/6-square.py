#!/usr/bin/python3
"""Definies a class Square"""


class Square:
    """The definition of a class called Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor.
        Args:
            size (int): the length of the sides of the square
            position (tuple): the position of the square
        Raises:
            TypeError: the value of size is not an integer
            ValueError: the value of size is negative
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter => getting the size"""
        return self.__size

    @property
    def position(self):
        """Getter => getting the position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter => Setting the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter => Setting the position"""
        if isinstance(value, tuple):
            if len(value) != 2:
                raise TypeError(
                        "position must be a tuple"
                        "of 2 positive integers"
                        )
            for item in value:
                if not isinstance(item, int) or item < 0:
                    raise TypeError(
                            "position must be a tuple"
                            "of 2 positive integers"
                            )
            self.__position = value

    def area(self):
        """
        This method calculates the area of a given square object.
        Return: returns the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """print the square with the character # to the stdout"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
