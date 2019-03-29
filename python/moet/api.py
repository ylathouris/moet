"""
API

This module contains the API for moet.
"""

import inspect


def create_tower(rows=4):
    r"""
    Create a tower of glasses.

    This function is used to create a tower of glasses with the given
    number of rows (default: 4).

    Example:
                           (Y)
                           / \
                         (Y) (Y)
                         / \ / \
                       (Y) (Y) (Y)
                       / \ / \ / \
                     (Y) (Y) (Y) (Y)

    Args:
        rows (int): Number of rows in the tower of glasses.
    """
    raise NotImplementedError("This function is not currently supported")


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


class Tower:
    """
    Tower

    This class represents a tower of glasses which can be filled
    with champagne (or any other form liquid).
    """

    def __init__(self):
        """Initialize tower"""
