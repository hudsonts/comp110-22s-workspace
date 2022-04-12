"""These functions test the functions defined in the dictionary.py document."""


from exercises.ex06.dictionary import invert, favorite_color, count


def test_invert() -> None:
    """This function tests to see if the first key in the resulting dictionary is equal to the first value of the original dictionary."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs)["z"] == "a"


def test_invert_endcase() -> None:
    """This function tests the last item in the resulting dictionary to make sure it is not equal to the last item of the original dictionary."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs)["x"] == "c"


def test_invert_middle_values() -> None:
    """This function tests the middle values of the resulting dictionary to ensure they are inverse of the original dictionary values."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs)["y"] == "b"


def test_favorite_color() -> None:
    """This function tests to see if the most prevalent color is displayed by the favorite_color function."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_again() -> None:
    """This function tests to see if the favorite color function works properly and displays the most prevalent color."""
    xs: dict[str, str] = {"turtle": "green", "bear": "brown", "frog": "green", "clownfish": "orange"}
    assert favorite_color(xs) == "green"


def test_favorite_color_endcase() -> None:
    """This function tests to see if when there are two values with a tied amount, the first color is the one that is returned as the favorite color."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Hudson": "yellow"}
    assert favorite_color(xs) == "yellow"


def test_count() -> None:
    """This function tests to see if the count function properly displays the values and the amount of time each appears in the list."""
    xs: list[str] = ['a', 'b', 'c', 'a', 'a', 'c', 'd']
    assert count(xs)["a"] == 3


def test_count_again() -> None:
    """This function again tests to see if the count function works properly."""
    xs: list[str] = ['a', 'b', 'c', 'a', 'a', 'c', 'd']
    assert count(xs)["c"] == 2


def test_count_endcase() -> None:
    """This function tests the endcase of the count function to make sure the smallest value is properly accounted for."""
    xs: list[str] = ['a', 'b', 'c', 'a', 'a', 'c', 'd']
    assert count(xs)["d"] == 1