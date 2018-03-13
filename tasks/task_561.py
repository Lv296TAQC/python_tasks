"""
This module solves task 561 from zadachi.pdf.
"""

import argparse
from typing import List


def squares_of_numbers(value: int) -> List[str]:
    """Find numbers that correspond
    to the last records of their square.

    :param value: The number that more or equal 0.
    :return: List of strings.
    :Example:

    >>> squares_of_numbers(17)
    ['1^2 = 1', '5^2 = 25', '6^2 = 36']
    """

    result = []
    for number in range(1, value):
        squares = str(number ** 2)
        number_str = str(number)
        if squares.endswith(number_str):
            result.append(f"{number_str}^2 = {squares}")
    return result


def main():
    """Start 'squares_of_numbers' function."""
    parser = argparse.ArgumentParser(description='Input argument into \
                                     squares_of_numbers()')
    parser.add_argument('integer', type=int, help='Natural number > 0')
    args = parser.parse_args()

    try:
        squares = squares_of_numbers(args.integer)
        for element in squares:
            print(element)
    except ValueError:
        print("Inputted data isn't integer.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()