""""Write one to the start and to the end of given natural number"""


def one_bounds(natural: int) -> int:
    """
    Add one to the first and to the last digit, two to one-digit natural number.

    :param natural: Natural validated number from input
    :return: Natural number with added one to the first and to the last digit

    :Example:

    In this example number 555 will be returned as number 454 with added 1 to
        the first and to the last digits.

    .. doctest::

        >>> print(one_bounds(454))
        555
    """
    natural_most = natural
    counter = 1
    while natural_most > 9:
        natural_most = natural_most // 10
        counter *= 10
    if counter == 1:
        return natural + 2
    return natural + counter + 1


def is_natural(natural: int) -> bool:
    """
    Ask for input until valid data entered.

    :param natural: Any integer (natural) number
    :return: True, if input data is valid, False otherwise
    """
    try:
        natural = int(natural)
    except (ValueError, TypeError):
        return False
    else:
        if natural < 1:
            return False
        return True


def print_solution():
    """"Validate input, add numbers, print result."""

    natural = 13456788
    if is_natural(natural):
        print(one_bounds(int(natural)))
    else:
        print("Invalid input. Please write correct natural number")


if __name__ == '__main__':
    print_solution()
