#!/usr/bin/python3
"""Define a function that adds a new attriute to an obj"""


def add_attribute(obj, attribute_name, value):
    """Adds an attriute to an object

    Args:
        obj (oject): the object on which to add attribute
        attribute_name (string): the name of the attriute to add
        value (any): the value to assign

    Raises:
        TypeError: raised if ob does not accept new attributes
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute_name, value)
    else:
        raise TypeError("can't add new attribute")
