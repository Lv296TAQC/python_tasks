"""
This module solves task 243_a from zadachi.pdf.
"""

import argparse
from typing import Tuple, Union


def sum_of_two_squares(number: int) -> Union[bool, Tuple[int, int]]:
    """Check whether the number is the sum
    of the squares of two numbers.

    :param number: The number that more or equal 0.
    :return: Tuple with two numbers if successful, False otherwise.
    """

    first = 1
    while first ** 2 <= number:
        second = 1
        while second ** 2 <= number:
            if first**2 + second**2 == number:
                return first, second
            second += 1
        first += 1
    return False


def main():
    """Start sum_of_two_squares()."""
    parser = argparse.ArgumentParser(description='Input argument into \
                                     sum_of_two_squares()')
    parser.add_argument('integer', type=int, help='Natural number > 0')
    args = parser.parse_args()

    if sum_of_two_squares(args.integer):
        first_square, second_square = sum_of_two_squares(args.integer)
        print(f"The number {args.integer} is the sum", end=" ")
        print("of the squares of two numbers:")
        print(f"{args.integer} = {first_square}^2 + {second_square}^2")
    else:
        print(f"The number {args.integer} isn't the sum", end=" ")
        print("of the squares of two numbers.")


if __name__ == "__main__":
    main()
