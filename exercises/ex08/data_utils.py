"""Dictionary related utility functions."""

__author__ = "730509671"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(data_cols: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in data_cols:
        first_n_values: list[str] = []
        i: int = 0
        if n > len(data_cols[column]):
            n = len(data_cols[column])
        while i < n:
            first_n_values.append(data_cols[column][i])
            i += 1
        result[column] = first_n_values
    return result


def select(column_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        if column in columns:
            result[column] = column_table[column]
    return result


def concat(column_table_1: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in column_table_1:
        result[column] = column_table_1[column] 
    for column in column_table_2:
        if column in result:
            result[column] += column_table_2[column]
        else:
            result[column] = column_table_2[column]
    return result


def count(lines: list[str]) -> dict[str, int]:
    """Count the number of times that a value appears in an input list."""
    counts: dict[str, int] = {}
    for value in lines:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts
        
    