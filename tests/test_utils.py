"""
Test Utilities

This module contains tests for the moet's utility functions.
"""


import moet


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
        assert value == expected[index]


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
        assert not value


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
