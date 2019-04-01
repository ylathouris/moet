"""Test Command Line Interface (CLI)"""

import os

from click.testing import CliRunner

from moet import cli


def _get_test_data(name):
    testdir = os.path.dirname(__file__)
    path = os.path.join(testdir, "data", name)
    with open(path, "r") as test_file:
        data = test_file.read()

    return data


def test_moet__with_defaults__returns_expected():
    """
    Test running the moet command with defaults.

        $ moet

    """
    runner = CliRunner()
    result = runner.invoke(cli.moet)
    assert result.exit_code == 0
    assert result.output == _get_test_data("defaults.txt")


def test_moet__with_fill_500__returns_expected():
    """
    Test running the following moet command

        $ moet --fill 0.5 --uid C

    """
    expected = _get_test_data("fill-0.5-litres-uid-C.txt")

    runner = CliRunner()
    options = ["--fill", "0.5", "--uid", "C"]
    result = runner.invoke(cli.moet, options)
    assert result.exit_code == 0
    assert result.output == expected


def test_moet__with_fill_1500__returns_expected():
    """
    Test running the following moet command

        $ moet --fill 1.5 --uid E

    """
    expected = _get_test_data("fill-1.5-litres-uid-E.txt")

    runner = CliRunner()
    options = ["--fill", "1.5", "--uid", "E"]
    result = runner.invoke(cli.moet, options)
    assert result.exit_code == 0
    assert result.output == expected


def test_moet__with_fill_2500__returns_expected():
    """
    Test running the following moet command

        $ moet --fill 2.5 --position 2 2

    """
    expected = _get_test_data("fill-2.5-litres-pos-2-2.txt")

    runner = CliRunner()
    options = ["--fill", "2.5", "--position", "2", "2"]
    result = runner.invoke(cli.moet, options)
    assert result.exit_code == 0
    assert result.output == expected


def test_moet__with_fill_3750__returns_expected():
    """
    Test running the following moet command

        $ moet --fill 3.75 --position 4 0

    """
    expected = _get_test_data("fill-3.75-litres-pos-4-0.txt")

    runner = CliRunner()
    options = ["--fill", "3.75", "--position", "4", "0"]
    result = runner.invoke(cli.moet, options)
    assert result.exit_code == 0
    assert result.output == expected
