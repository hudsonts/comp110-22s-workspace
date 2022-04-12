"""These functions test the functionality of the functions defined in utils.py. Each function has an endcase test and two use case tests."""

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    """This function tests to see if the first index of the given list is an even value."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs)[0] % 2 == 0


def test_only_evens_middle_value() -> None:
    """This function tests to see if the second item in the only_evens list is 4."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs)[1] == 4


def test_only_evens_again() -> None:
    """This function tests the last value in the only_evens list to see if it is an even integer."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs)[len(xs) - 1] % 2 == 0


def test_sub() -> None:
    """This function tests to see if the sub function removes all items from the list except for the two that are defined by the parameters."""
    xs: list[int] = [10, 20, 30, 40]
    assert len(sub(xs, 1, 3)) == 2


def test_sub_endcase() -> None:
    """This function tests to make sure that the third item in the final product is equal to 350, ensuring that the right values have been removed from the original list."""
    xs: list[int] = [150, 200, 250, 300, 350, 400, 450]
    assert sub(xs, 2, 5)[2] == 350


def test_sub_again() -> None:
    """This function tests if the first item in the given range of values aligns with the expected output of four."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(xs, 3, 8)[0] == 4


def test_concat() -> None:
    """This function combines two given lists and makes sure the 4th item in the list is equal to 4, ensuring that the lists were conjoined in the correct sequence."""
    xs: list[int] = [1, 2, 3]
    xz: list[int] = [4, 5, 6]
    assert concat(xs, xz)[3] == 4


def test_concat_endcase() -> None:
    """This funciton ensures that the first item of the first list aligns with the first item of the combined list, making sure everything is still in expected order."""
    xs: list[int] = [1, 2]
    xz: list[int] = [3, 4]
    assert concat(xs, xz)[0] == 1


def test_concat_again() -> None:
    """This function tests to see if the middle item in a list aligns with the expected output of 11, ensuring that the values in each list were not arranged in any new order."""
    xs: list[int] = [7, 3]
    xz: list[int] = [11, 9, 21]
    assert concat(xs, xz)[len(xz) - 1] == 11