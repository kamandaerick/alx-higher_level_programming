#!/usr/bin/python3
"""
The writes a string to textfile and returns the number of
characters written
"""


def write_file(filename="", text=""):
    """Write to a file and return the number of characters written

    Args:
        filename (str): Name of the file to write to.
        text (str): The contents to add to the file. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
