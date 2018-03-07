"""This module solves the task 331b from zadachi.pdf"""


def func(numb: int) -> list:
    """
    Find all triples of natural numbers,
    whose sum of squares is equal to the numb.

    :param numb: any number.
    :return: contains tuples of the three natural numbers.

    :Example:
        >>> func(100)
        [(8, 6, 0), (10, 0, 0)]
    """
    answer = []
    for i in range(numb):
        for j in range(numb):
            for k in range(numb):
                if i * i + j * j + k * k == numb and k <= j <= i:
                    answer.append((i, j, k))
    return answer
