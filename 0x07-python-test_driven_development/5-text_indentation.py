#!/usr/binpython3
"""
This module adds 2 lines after each of these characters
.
?
:
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after
    each of these characters: ., ? and :.

    Parameters:
    text (str): The text to be printed.
    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_chars = ".?:"

    for char in text:
        print(char, end="")
        if char in new_line_chars:
            print("\n\n", end="")
