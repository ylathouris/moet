"""
Tower

This module contains functions and classes related to a tower
of glasses.
"""

import math

import networkx

from .glass import create_glass
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
    tower = Tower()
    count = utils.get_triangular_value(rows)
    for index in range(count):
        glass = create_glass(utils.get_id(index))
        tower.add_glass(glass)

    return tower


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
        self._set_overflow_dependencies(glass)

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

    def _set_overflow_dependencies(self, glass):
        """
        Set the overflow dependencies for the hew glass.

        This method is used to determine how the new glass is affected
        by overflowing liquid from higher up in the tower.

        Args:
            glass (Glass): New glass
        """
        rows = list(self.get_rows())
        row, column = glass.position

        # If the glass being added is the first glass. It has no
        # parents. Just return.
        if row == 0:
            return

        # If the glass is at the beginning of the row, it will
        # only receive overflowing liquid from one parent.
        previous_row = rows[row - 1]
        if column == 0:
            start = 0
            end = 1

        # Similarly, if the glass is at the end of the row, it
        # will only receive overflowing liquid from one parent.
        elif column == row:
            start = len(previous_row) - 1
            end = len(previous_row)

        # Finally, if the glass in somewhere in the middle of
        # the row, it will receive overflowing liquid from two
        # parents.
        else:
            start = column - 1
            end = start + 2

        parents = previous_row[start:end]
        for parent in parents:
            self._graph.add_edge(parent, glass)

    def get_parents(self, glass):
        """
        Get parents for the given glass

        Args:
            glass (Glass): A glass in the tower.

        Returns:
             list of Glass: Parent glasses.
        """
        try:
            return self._graph.predecessors(glass)
        except networkx.NetworkXError as error:
            raise ValueError(str(error))

    def get_children(self, glass):
        """
        Get parents for the given glass

        Args:
            glass (Glass): A glass in the tower.

        Returns:
             list of Glass: Parent glasses.
        """
        try:
            return self._graph.successors(glass)
        except networkx.NetworkXError as error:
            raise ValueError(str(error))

    def fill(self, liquid_in_millilitres):
        """
        Pour the given amount of liquid (millilitres) over the tower.

        Args:
            liquid_in_millilitres (int or float): Liquid (millilitres)
        """
        raise NotImplementedError("This method is not currently supported")
