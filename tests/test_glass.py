"""
Test Glass

This module contains tests for the `moet.Glass` object.
"""

from hypothesis import given
from hypothesis.strategies import integers
import pytest

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


@given(integers(min_value=0, max_value=250))
def test_fill_glass__with_no_overflow__returns_expected(number):
    """
    Test filling a glass with liquid.

    Args:
        number (int or float): The number of millilitres to fill the glass with.
    """
    glass = moet.create_glass("A")
    print(number, glass.millilitres)
    overflow = glass.fill(number)
    print(number, overflow, glass.millilitres)
    assert not overflow
    assert glass.millilitres == number


@given(integers(min_value=250, max_value=500))
def test_fill_glass__with_overflow__returns_expected(number):
    """
    Test filling a glass with liquid.

    This test demonstrates the behaviour when trying to fill a glass
    with more liquid than it is capable of holding.

    Args:
        number (int or float): The number of millilitres to fill the glass with.
    """
    glass = moet.create_glass("A")
    overflow = glass.fill(number)
    assert overflow == number - 250
    assert glass.millilitres == 250


def test_glass_capacity__has_expected_default_value():
    """
    Test the default value for the amount of liquid a glass can hold.
    """
    glass = moet.create_glass("A")
    assert glass.capacity == 250


def test_set_glass_capacity__with_valid_numbers__returns_expected():
    """
    Test setting the value for the amount of liquid a glass can hold.

    In this case, we're using valid numbers (i.e. 0 or greater)
    """
    glass = moet.create_glass("A")
    numbers = [0, 1, 250, 0.0, 100.5]
    for number in numbers:
        glass.capacity = number
        assert glass.capacity == number


def test_set_glass_capacity__with_invalid_numbers__returns_expected():
    """
    Test setting the value for the amount of liquid a glass can hold.

    In this case, we're using invalid numbers (i.e. negative numbers)
    """
    glass = moet.create_glass("A")
    with pytest.raises(ValueError):
        glass.capacity = -100


def test_set_glass_millilitres__with_negative_number__raises_value_error():
    """
    Test setting the amount of liquid in the glass directly.

    This test demonstrates the behaviour when trying to set the
    amount of liquid in a glass using a negative number.
    """
    glass = moet.create_glass("A")
    with pytest.raises(ValueError):
        glass.millilitres = -100
