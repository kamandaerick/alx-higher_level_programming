#!/usr/bin/python3
"""
Check if an obect is an instance of a class
that inherited (directly or indirectly) from the specified class ;
otherwise False.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class

    Args:
        obj (object): The object to check
        a_class (class): The class to check against

    Returns:
        boolean: returns True if the obect is an instance of a class
                and False if it is not
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
