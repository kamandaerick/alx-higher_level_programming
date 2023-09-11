#!/usr/bin/python3
"""Define a class that inherit from list"""


class MyList(list):
    """Define class MyList that printed sorted list"""
    def print_sorted(self):
        """Print list in sorted format"""
        print(sorted(self))
