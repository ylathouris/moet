"""Moet Command Line Interface (CLI)"""


import click

from .tower import create_tower
from . import utils


LIQUIDS = ["champagne", "beer", "wine", "sake", "water", "tea", "coffee"]


@click.command()
@click.option(
    "-r", "--rows", type=int, default=4, help="The number of rows in the tower (max=6)"
)
@click.option(
    "-f",
    "--fill",
    type=float,
    default=3.75,
    help="The amount of liquid to pour over the tower (litres)",
)
@click.option("-i", "--uid", type=str, help="The ID of the glass to select/highlight")
@click.option(
    "-p",
    "--position",
    type=int,
    nargs=2,
    help="The position of the glass to select/highlight",
)
@click.option(
    "-l",
    "--liquid",
    type=click.Choice(LIQUIDS),
    default="champagne",
    help="The type of liquid",
)
@click.option(
    "-b",
    "--breakdown",
    is_flag=True,
    default=False,
    help="Show breakdown of each glass in the tower.",
)
def moet(rows, fill, uid, position, liquid, breakdown):
    """
    Build a tower of glasses. Fill them with champagne!

    """
    version = utils.get_version()
    click.echo(f"moet (version: {version})\n")

    tower = create_tower(rows=rows)
    click.echo(f"Pouring {fill} litres of {liquid} over the tower:\n")
    millilitres = fill * 1000
    overflow = tower.fill(millilitres)

    if uid and position:
        msg = (
            f"Options --uid={uid} and --position={position} are " "mutaually exclusive"
        )
        click.echo(click.style(msg, fg="bright_red"))
        raise click.Abort(msg)

    if position:
        for glass in tower.glasses:
            if position == glass.position:
                uid = glass.uid
                break

    pprint(tower, uid, overflow, breakdown, liquid)


def pprint(tower, uid, overflow, breakdown, liquid):
    """
    Print the tower.

    Args:
        tower (Tower): The tower to print.
        uid (str): The ID of the glass to select/highlight.
        overflow (float): The amount of overflowing liquid.
        breakdown (bool): If true, show a breakdown of each glass.
        liquid (str): The type of liquid used.
    """
    lines = []

    indent = " "
    rows = list(tower.get_rows())
    rows = reversed(rows[:])
    for index, row in enumerate(rows):
        text = format_row(row, uid, indent, liquid)
        if index != 0:
            edges = indent + "/ \\ " * len(row)
            lines.insert(0, edges)

        lines.insert(0, text)
        indent += "  "

    lines.append("\n")
    click.echo("\n".join(lines))

    breakdown_text = format_breakdown(tower, uid, overflow)
    if breakdown:
        click.echo(breakdown_text)


def format_row(row, uid, indent, liquid):
    """
    format a row in the tower.

    Args:
        row (list of Glass): The list of glasses in a row.
        uid (str, optional): The glass ID selected by the user.
        indent (str): Indentation level (depends on row)
        liquid (str): The type of liquid used.

    Returns:
        str: Formatted row information.
    """
    chars = []
    match = False
    for glass in row:
        text = highlight(f"({glass.uid})", glass, uid)
        chars.append(text)
        if glass.uid == uid:
            match = glass

    if match:
        quantity = utils.to_integer(glass.quantity)
        extra = (
            f"  <-- Glass ({match.uid}), at position {match.position}, "
            f"contains {quantity} millilitres of {liquid}."
        )
        chars.append(paint(extra))

    text = indent + " ".join(chars)
    return text


def format_breakdown(tower, uid, overflow):
    """
    Format a breakdown of the quantities in each glass.

    Args:
        tower (Tower): The tower.
        uid (str, optional): The glass ID selected by the user.
        overflow (float): The amount of overflow liquid.

    Returns:
        str: Formatted breakdown of each glass in the tower.
    """
    lines = []
    for glass in tower.glasses:
        quantity = utils.to_integer(glass.quantity)
        line = f"id=({glass.uid}) position={glass.position} quantity={quantity}"
        line = highlight(line, glass, uid)
        lines.append(line)

    text = "Breakdown:\n\n"
    text += "\n".join(lines)
    text += "\n" + paint(f"\nOverflow: {overflow}", color="yellow") + "\n"
    return text


def highlight(text, glass, uid):
    """
    Highlight the given text if the glass matches the given ID.

    Args:
        text (str): Text to highlight
        glass (Glass): The glass to paint.
        uid (str): Glass ID.

    Returns:
        str: Highlighted text.
    """
    return paint(text) if glass.uid == uid else text


def paint(text, color="green"):
    """
    Paint the given text green.

    Args:
        text (str): Text to be painted.
        color (green): Color to paint text.

    Returns:
        str: Painted text.
    """
    return click.style(text, fg=color)
