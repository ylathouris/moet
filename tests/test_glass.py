"""
Test Glass

This module contains tests for the `moet.Glass` object.
"""

import moet


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
    assert "moet.glass.Glass(uid=A, pos=None)" in repr(glass)
