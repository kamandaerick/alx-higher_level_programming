#!/usr/bin/python3
"""
    This module prints out my first and last names.
    It checks first is the names are of type string.
    If one or oth names are not of type str,
    a type error is riased
"""


def say_my_name(first_name, last_name=""):
    """

    Args:
        first_name (str): my first name. Must be a string
        last_name (str): My last name. Must be a string

    Raises:
        TypeError: raised if first or last name is not a str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
