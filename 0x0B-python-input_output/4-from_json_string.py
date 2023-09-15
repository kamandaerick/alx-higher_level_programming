#!/usr/bin/python3
"""Return an object represented by a python string"""
import json


def from_json_string(my_str):
    """Return a python oject from a son string

    Args:
        my_str (str): son string to deserialize

    Returns:
        object: python oect
    """
    return json.loads(my_str)
