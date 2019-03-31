"""
Glass

This module contains functions and classes related to the glasses
that form a tower of glasses.
"""

import inspect


def create_glass(uid):
    """
    Create a glass.

    Args:
        uid (str): A unique identifier for the glass.

    Returns:
        Glass: A new glass
    """
    glass = Glass(uid)
    return glass


class Glass:
    """
    Glass.

    The `glass` object represents a glass.
    """

    def __init__(self, uid):
        """
        Initialize glass with the given code.

        Args:
            uid (str): Glass code
        """
        self.uid = uid
        self.position = None

    def __repr__(self):
        """
        Get object representation.

        Returns:
             str: Object representation.
        """
        mod = inspect.getmodule(self).__name__
        cls = self.__class__.__name__
        address = hex(id(self))
        return f"<{mod}.{cls}(uid={self.uid}, pos={self.position}) at {address}>"

    def __str__(self):
        """
        Get string representation.

        Returns:
            str: String representation.
        """
        return self.uid
