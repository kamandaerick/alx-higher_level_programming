#!/usr/bin/python3
"""Define class MyInt that inverts equality operators"""


class MyInt(int):
    """Define class MyInt that inherits from int"""
    def __ne__(self, other):
        """Defintition of inequality

        Args:
            other (int): the value to compare self with

        Returns:
            bool: returns True for inequality and False for equality
        """
        return super().__eq__(other)

    def __eq__(self, other):
        """Defintition of inequality

        Args:
            other (int): the value to compare self with

        Returns:
            bool: returns False for inequality and True for equality
        """
        return super().__ne__(other)
