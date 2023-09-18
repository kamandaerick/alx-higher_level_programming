#!/usr/bin/python3
"""Define a Base class "BAse" """


class Base:
    """Definition of a class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id (int): tracks the instances of the class. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
