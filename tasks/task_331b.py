"""This module solves the task 331b from zadachi.pdf"""


def func(numb):
    """
    Find all triples of natural numbers,
    whose sum of squares is equal to the numb.

    Arg:
        numb (int): any number.

    Return:
        answer (list): contains tuples of the three natural numbers.

    Example:
        >>> print(func(100))
        [(8, 6, 0), (10, 0, 0)]
    """
    answer = []
    for i in range(numb):
        for j in range(numb):
            for k in range(numb):
                if i * i + j * j + k * k == numb and k <= j <= i:
                    answer.append((i, j, k))
    return answer
