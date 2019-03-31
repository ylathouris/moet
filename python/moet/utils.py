"""
Utilities

This module contains moet utility functions.
"""

import math
import string


ALPHABET = string.ascii_uppercase


def get_id(number):
    """
    Get ID.

    This function is used to create an ID. If the given number is
    within the range of the alphabet, the ID returned will be nth
    character. Otherwise a number is returned.

    Args:
        number (int): The index for a character in the alphabet.

    Returns:
        str: ID
    """
    if number > 25:
        return str(number)
    else:
        return ALPHABET[number]


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
         float: The triangular root for the given number.
    """
    value = (math.sqrt(8 * number + 1) - 1) / 2
    return value


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
