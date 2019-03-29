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


def test_create_glass__returns_expected_value():
    """
    Test creating a glass.

    This test demonstrates how to create a glass. It is also used
    to verify the initial values of the glass properties.
    """
    glass = moet.create_glass("A")
    assert glass.uid == "A"
    assert glass.position is None


def test_glass_str__returns_uid():
    """
    Test the string representation of a glass.

    This test is used to verify that the string representation
    of a glass is the glass's unique identifier.
    """
    glass = moet.create_glass("A")
    assert str(glass) == glass.uid


def test_glass_repr__returns_expected_value():
    """
    Test the object representation of a glass.

    This test is used to verify that the object representation
    of a glass contains the expected information (i.e. uid and position).
    """
    glass = moet.create_glass("A")
    assert "moet.api.Glass(uid=A, pos=None)" in repr(glass)
