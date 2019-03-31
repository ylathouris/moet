"""
Test API

This module contains tests for the moet API.
"""

from hypothesis import given
from hypothesis.strategies import integers
import pytest

import moet


@pytest.mark.xfail(raises=NotImplementedError)
@given(integers(min_value=0, max_value=5))
def test_create_tower__with_n_rows__returns_expected_hierarchy(rows):
    r"""
    Test creating a tower of glasses.

    This test demonstrates how to create a tower of glasses and then
    verifies that the tower has the expected hierarchy. For example,
    a tower with four rows should look something like:

                           (A)
                           / \
                         (B) (C)
                         / \ / \
                       (D) (E) (F)
                       / \ / \ / \
                     (G) (H) (I) (J)

    Args:
        rows (int): The number of rows in the tower (0-5)
    """
    tower = moet.create_tower(rows=rows)

    n = 0
    parents = []
    for row in tower.rows:

        # Check node(s) - does the current row have the expected
        # number of items (i.e. glasses)
        count = len(row)
        assert count == n + 1
        n = count

        for index, item in enumerate(row):

            # If the node is at the beginning of the row it should
            # only have one parent.
            if item.column == 0:
                start = 0
                end = 1

            # Similarly, if the node is at the end of the row, it also
            # only has one parent.
            elif index == count:
                start = -2
                end = -1

            # Finally, if the node is somewhere in the middle of the
            # row, it should have two parents.
            else:
                start = index - 1
                end = start + 2

            # Check edges - does the current item have the expected
            # parents (i.e. will the overflowing liquid be distributed
            # to the correct glasses)
            assert item.parents == parents[start:end]

        # Now that we've finished processing the current row, we can
        # use it as the next set of parents.
        parents = row


@given(integers(min_value=1, max_value=21))
def test_add_glasses_to_tower(number):
    """
    Test adding glasses to a tower.

    This test demonstrates how to add glasses to a tower of
    glasses. It then verifies that the glasses were added by
    checking the properties of the tower.

    Args:
        number (int): The number of glasses to add to the tower.
    """
    tower = moet.Tower()

    glasses = []
    for index in range(number):
        id_ = moet.utils.get_id(index)
        glass = moet.create_glass(id_)
        tower.add_glass(glass)
        glasses.append(glass)

    assert tower.glasses == glasses


@given(integers(min_value=1, max_value=21))
def test_add_glasses_to_tower__returns_expected_positions(number):
    """
    Test getting the position of a glass in the tower.

    This test demonstrates how to get the position of a glass in a
    tower of glasses.

    Args:
        number (int): The number of glasses to add to the tower
    """
    tower = moet.Tower()

    # Add glasses
    for index in range(number):
        id_ = moet.utils.get_id(index)
        glass = moet.create_glass(id_)
        tower.add_glass(glass)

    # Check positions.
    rows = list(tower.get_rows())
    for row_index, row in enumerate(rows):
        for column_index, glass in enumerate(row):
            print(glass, glass.position)
            assert glass.position == (row_index, column_index)
