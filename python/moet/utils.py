"""
Utilities

This module contains moet utility functions.
"""

import math


def get_triangular_value(number):
    """
    Apply the triangular rule to the given number.

    This function is used to determine the number of items (i.e.
    glasses) required to create a triangle with the given number
    of rows. For this we use the rule:

        x = n * (n + 1) / 2

    Args:
        number (int): Some number.

    Returns:
         int: The number of items required to form the triangle.
    """
    return number * (number + 1) // 2


def get_triangular_root(number):
    """
    Apply the inverse of the triangular rule to the given number.

    This function is used to determine the number of rows
    made from the given number of items (i.e. glasses)

        n = sqrt(8x + 1) - 1 / 2

    Args:
        number (int): Some number.

    Returns:
         int or None: The number of rows made from the given items.
    """
    value = (math.sqrt(8 * number + 1) - 1) / 2
    return int(value) if value.is_integer() else None


def is_triangular(number):
    """
    Check if the given number is triangular.

    This function is used to check is the given number is in the
    triangular number sequence. For example:

        1, 3, 6, 10, 15 .. etc.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is in the sequence, false otherwise.
    """
    for index in range(number + 1):
        value = index * (index + 1) // 2
        if value < number:
            continue

        return value == number

    return False
