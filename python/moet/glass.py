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
        self._capacity = 250
        self._millilitres = 0.0

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

    @property
    def capacity(self):
        """
        Get the amount of liquid in this glass can hold (millilitres)

        int or float: The amount of liquid this glass can hold (millilitres)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            msg = f"Invalid value for capacity. Gor {value}, " f"expected value above 0"
            raise ValueError(msg)

        self._capacity = value

    @property
    def millilitres(self):
        """
        Get the amount of liquid in this glass (millilitres)

        int or float: The amount of liquid in the glass (millilitres)
        """
        return self._millilitres

    @millilitres.setter
    def millilitres(self, value):
        if value < 0 or value > self.capacity:
            msg = (
                f"Invalid value for millilitres. Gor {value}, "
                f"expected value between 0 and {self.capacity}"
            )
            raise ValueError(msg)

        self._millilitres = value

    def fill(self, liquid_in_millilitres):
        """
        Fill the glass with the given amount of liquid (millilitres)

        Args:
            liquid_in_millilitres(int or float): Liquid (millilitres)

        Returns:
            float: Overflowing liquid (millilitres)
        """
        raise NotImplementedError("This method is currently unsupported!")
