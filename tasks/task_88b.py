"""
This module solves task 88_б from zadachi.pdf.
"""

import argparse


def reverse_int(number: int) -> int:
    """Convert int number that more than 0 into string,
    reverse it and return int value.

    :param number: The number that more or equal 0.
    :return: Reversed number.
    :Example:

    >>> reverse_int(123)
    321
    """

    return int(str(number)[::-1])


def main():
    """Start reverse_int(), create parser.

    """
    parser = argparse.ArgumentParser(description='Input argument into \
                                     reverse_int()')
    parser.add_argument('integer', type=int,
                        help='Only first int absolute number will be enabled')
    args = parser.parse_args()

    try:
        print(reverse_int(args.integer))
    except ValueError:
        print("Please, enter int number => 0.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()