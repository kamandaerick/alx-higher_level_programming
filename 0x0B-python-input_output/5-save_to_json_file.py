#!/usr/bin/python3
"""Write an oject to a text file using son representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write a text file using JSON representation

    Args:
        my_obj (object): Python oject
        filename (str): name of a file to write to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
