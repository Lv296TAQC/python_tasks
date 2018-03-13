"""
This module solves task 178_г from zadachi.pdf.
"""

import argparse
from typing import List


def task_function(numbers: List[int]) -> int:
    """Check how many numbers in list are less than
    the sum of the previous and next numbers divided by 2.

    :param numbers: List of int numbers.
    :return: Count of numbers that are less than
             the sum of the previous and next numbers divided by 2.
    :Example:

    >>> task_function([1, 2, 8, 25])
    2
    """

    count = 0
    for first, second, third in zip(numbers, numbers[1:], numbers[2:]):
        if (first + third) / 2 > second:
            count += 1
    return count


def main():
    """Start task_function()."""
    parser = argparse.ArgumentParser(description='Input argument into \
                                     task_function()')
    parser.add_argument('list_int', nargs='*', type=int, help='natural numbers in a row')
    args = parser.parse_args()
    print("Elements that correspond to the task condition:", end=' ')
    print(task_function(args.list_int))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()