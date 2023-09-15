#!/usr/bin/python3
"""Create a python oject from a JSON file"""
import json


def load_from_json_file(filename):
    """Create a python object from a JSON

    Args:
        filename (path): name of the file

    Returns:
        object: a python object
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
