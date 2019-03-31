"""
Test API

This module contains tests for the moet API.
"""

from hypothesis import given
from hypothesis.strategies import integers
import pytest

import moet


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


def test_get_glass__that_does_not_exist__returns_none():
    """
    Test getting a glass from a tower of glasses.

    This test demonstrates the behaviour when trying to get a glass
    that does not exist within a tower.
    """
    tower = moet.create_tower(4)
    glass = tower.get_glass("Z")
    assert glass is None


def test_get_edges__for_root__returns_expected():
    """
    Test getting the parent/child glasses for the top most glass in the tower.

    This test is used to verify that the root glass (the top most
    point in the tower) has no parents and two children.
    """
    #        (A)       <------- glass (A) has no parents and two
    #        / \                children (B) and (C)
    #      (B) (C)
    #      / \ / \
    #    (D) (E) (F)
    #    / \ / \ / \
    #  (G) (H) (I) (J)

    tower = moet.create_tower(4)
    glass = tower.get_glass("A")

    # Check parents
    parents = tower.get_parents(glass)
    assert not list(parents)

    # Check children
    children = tower.get_children(glass)
    assert [c.uid for c in children] == ["B", "C"]


def test_get_edges__for_column_left___returns_expected():
    """
    Test getting the parent/child glasses for a glass on the left edge.

    This test is used to verify that a glass on the left side of a
    row in the tower, has the correct parents and children.
    """
    #        (A)
    #        / \
    #      (B) (C)
    #      / \ / \
    #    (D) (E) (F)   <------- glass (D) has one parent (B) and two
    #    / \ / \ / \            children (G) and (H)
    #  (G) (H) (I) (J)

    tower = moet.create_tower(4)
    glass = tower.get_glass("D")

    # Check parents
    parents = tower.get_parents(glass)
    assert [p.uid for p in parents] == ["B"]

    # Check children
    children = tower.get_children(glass)
    assert [c.uid for c in children] == ["G", "H"]


def test_get_edges__for_column_right__returns_expected():
    """
    Test getting the parent/child glasses for a glass on the right edge.

    This test is used to verify that a glass on the right side of a
    row in the tower, has the correct parents and children.
    """
    #        (A)
    #        / \
    #      (B) (C)
    #      / \ / \
    #    (D) (E) (F)   <------- glass (F) has one parent (C) and two
    #    / \ / \ / \            children (I) and (J)
    #  (G) (H) (I) (J)

    tower = moet.create_tower(4)
    glass = tower.get_glass("F")

    # Check parents
    parents = tower.get_parents(glass)
    assert [p.uid for p in parents] == ["C"]

    # Check children
    children = tower.get_children(glass)
    assert [c.uid for c in children] == ["I", "J"]


def test_get_parents__for_middle__returns_two_parents():
    """
    Test getting the parent glasses for a glass in the middle of row.

    This test is used to verify that a glass in the middle of a row
    has the correct parents and children.
    """
    #        (A)
    #        / \
    #      (B) (C)
    #      / \ / \
    #    (D) (E) (F)   <------- glass (E) has two parents (B) and (C)
    #    / \ / \ / \            and two children (H) and (I)
    #  (G) (H) (I) (J)

    tower = moet.create_tower(4)
    glass = tower.get_glass("E")

    # Check parents
    parents = tower.get_parents(glass)
    assert [p.uid for p in parents] == ["B", "C"]

    # Check children
    children = tower.get_children(glass)
    assert [c.uid for c in children] == ["H", "I"]


def test_get_edges__for_nonexistent_glass__raises_value_error():
    """
    Test getting the child/parent glasses for a glass that doesn't exist.
    """
    tower = moet.create_tower(4)

    # Check parents
    with pytest.raises(ValueError):
        tower.get_parents("Z")

    # Check children
    with pytest.raises(ValueError):
        tower.get_children("Z")
