#!/usr/bin/python3
"""Read a text file (UTF-8) and print it to stdout"""


def read_file(filename=""):
    """Read a file and print it to stdout

    Args:
        filename (str): Name of the file to be read. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end='')
