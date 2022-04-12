"""This program establishes dictionary functions to achieve various tasks."""

__author__ = "730509671"


def invert(two_strings: dict[str, str]) -> dict[str, str]:
    """This function takes a dictionary of strings and inverts the keys and values."""
    new_dict: dict[str, str] = {}
    for key, value in two_strings.items():
        if two_strings[key] in new_dict:
            raise KeyError("KeyError has occurred.")
        else:
            new_dict[value] = key
    return new_dict


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """This function analyzes the input of individual's favorite colors and returns the most popular color as a string value."""
    colors: dict[str, int] = {}
    result: str = " "
    i: int = 0
    for key in names_and_colors:
        if names_and_colors[key] in colors: 
            colors[names_and_colors[key]] += 1
        else:
            colors[names_and_colors[key]] = 1
    for key in colors:
        if colors[key] > i:
            i = colors[key]
            result = key
    return result


def count(unique_strings: list[str]) -> dict[str, int]:
    """This function will count how many times each item appears in the list and return the items and their number of iterations in a dictionary."""
    result: dict[str, int] = {}
    for value in unique_strings:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result