#!/usr/bin/python3
"""
This module restricts attributes the following class can have.
"""


class LockedClass:
    """This class has a restriction of attributes"""
    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = None
