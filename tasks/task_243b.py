"""This module solves the task 243b from zadachi.pdf"""


def func(numb: int) -> list:
    """
    Find all pairs of natural numbers,
    whose sum of squares is equal to the numb.

    :param numb: any number.
    :return: contains tuples of pairs of the natural numbers.

    :Example:
        >>> func(100)
        [(8, 6), (10, 0)]
    """
    answer = []
    for i in range(numb):
        for j in range(numb):
            if i * i + j * j == numb and i >= j:
                answer.append((i, j))
    return answer
