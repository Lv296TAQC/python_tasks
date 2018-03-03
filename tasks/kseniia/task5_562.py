"""This module solves the task 562 from zadachi.pdf"""


def split_into_digits(numb):
    """
    Split the the number into digits.

    Arg:
        numb (int): any number.

    Return:
        answer (list): contains digits of the numb.

    Example:
        >>> print(split_into_digits(123))
        [1, 2, 3]
    """
    answer = []
    while numb > 0:
        answer.append(numb % 10)
        numb //= 10
    return answer[::-1]


def get_armstrong_numbs(start, end):
    """
    Get all Armstrong numbers(PPDI)
    from given interval [start, end].

    Args:
        start (int): any number.
        end (int): greater than start.

    Return:
        answer (list): contains Armstrong numbers.

    Example:
        >>> print(get_armstrong_numbs(10, 999))
        [153, 370, 371, 407]
    """
    answer = []
    for i in range(start, end):
        arr = split_into_digits(i)
        exp = len(arr)
        arr = [pow(x, exp) for x in arr]
        if sum(arr) == i:
            answer.append(i)
    return answer
