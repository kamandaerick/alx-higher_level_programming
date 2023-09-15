#!/usr/bin/python3
"""This module appends a string at the end of a file"""


def append_write(filename="", text=""):
    """Append a string to a file

    Args:
        filename (str): the name of the file to append to. Defaults to "".
        text (str): the contents to append. Defaults to "".
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
