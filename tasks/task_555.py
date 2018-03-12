""""This module solves the task 555."""


def current_row(number: int) -> list:
    """
    Take a natural number and return current row of Pascal's triangle,
    where 'number' is its length.

    :param int number: Any natural number.
    :return list row: Represents current row of Pascal's triangle.

    >>> current_row(10)
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    """
    row = []
    for i in range(number):
        if i == 0 or i == number - 1:
            row.append(1)
        else:
            c_row = current_row(number - 1)
            row.append(c_row[i - 1] + c_row[i])
    return row

def triagle(number_of_rows: int) -> list:
    """"
    Take a natural number and make Pascal's triangle list,
    where each sublist is a row of Pascal's triangle.

    Args:
        number_of_rows(int): any natural number

    Returns:
        result (list): represents Pascal's triangle

    >>> triagle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    result = []
    for i in range(number_of_rows):
        result.append(current_row(i + 1))
    return result
