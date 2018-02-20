""""This module solves the task 555."""


def current_row(number):
    """"
    Take a natural number and return current row of Pascal's triangle,
    where 'number' is its length.

    Args:
        number (int): any natural number

    Returns:
        row (list): represents current row of Pascal's triangle

    """
    row = []
    for i in range(number):
        if i == 0 or i == number - 1:
            row.append(1)
        else:
            c_row = current_row(number - 1)
            row.append(c_row[i - 1] + c_row[i])
    return row


def triagle(number_of_rows):
    """"
    Take a natural number and make Pascal's triangle list,
    where each sublist is a row of Pascal's triangle.

    Args:
        number_of_rows(int): any natural number

    Returns:
        result (list): represents Pascal's triangle

    """
    result = []
    for i in range(number_of_rows):
        result.append(current_row(i + 1))
    return result
