"""This program will define three different functions that will be called and tested later."""

__author__ = "730509671"


def only_evens(xs: list) -> list[int]:
    """This function takes the items imported in a list and returns only the even values from that list."""
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 != 0:
            xs.pop(i)
        else:
            i += 1
    return xs


def sub(xs: list, a: int, b: int) -> list[int]:
    """This function takes an inputted list from the user and returns that same list, only including indexes specified by the user."""
    user_list: list[int] = xs[a:b]
    return user_list


def concat(list_1: list, list_2: list) -> list[int]:
    """This function will take the items in list 1 and the items in list 2 to make a long list of the elements in 1 followed by the elements in 2."""
    i: int = 0
    while i < len(list_2):
        list_1.append(list_2[i])
        i += 1
    return list_1