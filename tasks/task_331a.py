"""
This module solves task 331_a from zadachi.pdf.
"""

import argparse
from typing import Tuple, Union


def sum_of_three_squares(number: int) -> Union[bool, Tuple[int, int, int]]:
    """Check whether the number is the sum
    of the squares of three numbers.

    :param number: The number that more or equal 0.
    :return: Tuple with three numbers if successful, False otherwise.
    """

    value_one = 1
    while value_one ** 2 <= number:
        value_two = 1
        while value_two ** 2 <= number:
            value_three = 1
            while value_three ** 2 <= number:
                if value_one**2 + value_two**2 + value_three**2 == number:
                    return value_one, value_two, value_three
                value_three += 1
            value_two += 1
        value_one += 1
    return False


def main():
    """Start sum_of_three_squares()."""
    parser = argparse.ArgumentParser(description='Input argument into \
                                     sum_of_three_squares()')
    parser.add_argument('integer', type=int, help='Natural number > 0')
    args = parser.parse_args()

    try:
        if sum_of_three_squares(args.integer):
            first, second, third = sum_of_three_squares(args.integer)
            print(f"The number {args.integer} is the sum", end=" ")
            print("of the squares of three numbers:")
            print(f"{args.integer} = {first}^2 + {second}^2 + {third}^2")
        else:
            print(f"The number {args.integer} isn't the sum", end=" ")
            print("of the squares of three numbers.")
    except ValueError:
        print("Please type int number.")


if __name__ == "__main__":
    main()
