#!/usr/bin/python3
"""Returns json representation of an oject"""


import json


def to_json_string(my_obj):
    """Returns json representation of an oject

    Args:
        my_obj (object): the oject
    """
    return json.dumps(my_obj)
