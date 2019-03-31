"""
Tower

This module contains functions and classes related to a tower
of glasses.
"""

import math

import networkx

from . import utils


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


class Tower:
    """
    Tower

    This class represents a tower of glasses which can be filled
    with champagne (or any other form liquid).
    """

    def __init__(self):
        """Initialize tower"""
        self._graph = networkx.DiGraph()

    @property
    def count(self):
        """
        Get glass count.

        int: Number of glasses in the tower.
        """
        return len(self.glasses)

    @property
    def glasses(self):
        """
        Get glasses.

        list of Glass: Glasses
        """
        return list(self._graph.nodes)

    def get_glass(self, uid):
        """
        Get the glass with the given ID.

        Args:
            uid (str): Glass ID.

        Returns:
            Glass or None: Glass with the given ID.
        """
        for glass in self.glasses:
            if glass.uid == uid:
                return glass

    def add_glass(self, glass):
        """
        Add new glass to the tower.

        Args:
            glass (Glass): New glass.
        """
        glass.position = self.get_next_position()
        self._graph.add_node(glass)

    def get_row_count(self):
        """
        Get the number of rows in the tower.

        Returns:
            int: Number of rows in the tower.
        """
        root = utils.get_triangular_root(self.count)
        return int(math.floor(root))

    def get_rows(self):
        """
        Get the rows in the tower.

        Yields:
            list: The rows in the tower.
        """
        row = []
        for index, glass in enumerate(self._graph.nodes):
            row.append(glass)
            root = utils.get_triangular_root(index + 1)
            if root.is_integer():
                yield row
                row = []

    def get_next_position(self):
        """
        Get the next available position.

        Returns:
             tuple: Next available position (i, j).
        """
        # Use triangular number sequence to determine the next
        # available row.
        glasses = list(self._graph.nodes)
        row_count = self.get_row_count()
        root = utils.get_triangular_root(self.count)
        if root.is_integer():
            row = row_count
            column = 0
        else:
            _, previous_column = glasses[-1].position
            row = row_count
            column = previous_column + 1

        return row, column
