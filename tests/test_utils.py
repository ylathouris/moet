"""
Test Utilities

This module contains tests for the moet's utility functions.
"""

import string

from hypothesis import given
from hypothesis.strategies import integers

import moet


@given(integers(min_value=0, max_value=25))
def test_get_id__with_valid_number__returns_expected_string(number):
    """
    Test getting an alphabetical ID.

    This test demonstrates how to generate a string ID from a given
    number. For numbers between 0 and 25, a letter of the alphabet
    is returned. Otherwise we just return the given number as a
    string.

    Args:
        number: Some number between 0 and 25
    """
    char = moet.utils.get_id(number)
    assert char == string.ascii_uppercase[number]


def test_get_id__with_numbers_over_26__returns_expected_string():
    """
    Test getting an ID.

    This test demonstrates how to generate a string ID from a given
    number. For numbers between 0 and 25, a letter of the alphabet
    is returned. Otherwise we just return the given number as a
    string. In this case, we're testing with the latter.
    """
    id_ = moet.utils.get_id(26)
    assert id_ == "26"


def test_get_triangular_value__returns_expected_sequence():
    """
    Test applying the triangular rule to a set of numbers.

    This test demonstrates how moet uses the triangular sequence rule
    to determine the number of items (i.e. glasses) in a triangular
    tower.
    """
    numbers = range(6)
    expected = [0, 1, 3, 6, 10, 15]
    for index, number in enumerate(numbers):
        value = moet.utils.get_triangular_value(number)
        assert value == expected[index]


def test_get_triangular_root__with_valid_numbers__returns_expected_value():
    """
    Test applying the inverse of the triangular rule to a set of numbers.

    This test demonstrates how moet uses the triangular sequence rule
    to determine the number of rows in a tower of glasses.
    """
    numbers = [0, 1, 3, 6, 10, 15]
    expected = range(6)
    for index, number in enumerate(numbers):
        value = moet.utils.get_triangular_root(number)
        assert value.is_integer()
        assert int(value) == expected[index]


def test_get_triangular_root__with_invalid_numbers__returns_expected_value():
    """
    Test applying the inverse of the triangular rule to a set of numbers.

    This test demonstrates how moet uses the triangular sequence rule
    to determine the number of rows in a tower of glasses. In this case,
    we are testing with numbers that do not make a complete triangle.
    """
    numbers = [2, 4, 5, 7, 8, 9, 11]
    for index, number in enumerate(numbers):
        value = moet.utils.get_triangular_root(number)
        assert not value.is_integer()


def test_is_triangular_check__with_valid_numbers__returns_true():
    """
    Test `is_triangular` utility function with valid numbers.

    This test demonstrates how to check if a number exists in the
    triangular sequence. In this case, we're only testing the function
    with valid sequence entries.
    """
    valid_numbers = [0, 1, 3, 6, 10, 15]
    for number in valid_numbers:
        assert moet.utils.is_triangular(number)


def test_is_triangular_check__with_invalid_numbers__returns_false():
    """
    Test `is_triangular` utility function with valid numbers.

    This test demonstrates how to check if a number exists in the
    triangular sequence. In this case, we're only testing the function
    with invalid sequence entries.
    """
    valid_numbers = [2, 4, 5, 7, 8, 9, 11, 12, 13, 14, 16]
    for number in valid_numbers:
        assert not moet.utils.is_triangular(number)
