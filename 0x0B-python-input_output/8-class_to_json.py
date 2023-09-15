#!/usr/bin/python3
"""Return a dictionary with a data structure"""


def class_to_json(obj):
    """Return a dictionary representation of simple data

    Args:
        obj (object): A ython obect

    Returns:
        dictionary: a dictionary representation of the ob
    """    
    return obj.__dict__
