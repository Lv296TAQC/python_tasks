""""This module solves the task 325."""


def func4(number: int) -> list:
    """
    Take natural number and return all simple divisors of entered number.

    :param number: Any natural number.
    :return mylist: List of all simple divisors of entered number.

    >>> func4(100)
    [2, 2, 5, 5]
    """
    i = 2
    mylist = []
    while i * i <= number:
        while number % i == 0:
            mylist.append(i)
            number = int(number / i)
        i += 1
    if number > 1:
        mylist.append(number)
    return mylist
