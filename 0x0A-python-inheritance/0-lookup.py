#!/usr/bin/ppython3
"""
This module defines a function that returns a list of all
attributes and methods of an object
"""


def lookup(obj):
    """
    Definition of the function lookup that uses the dir()
    Args:
        obj (class instance/object): The argument is a class instance

    Returns:
        list: Returns a list of all attriutes and methods of obj
    """
    return (dir(obj))
