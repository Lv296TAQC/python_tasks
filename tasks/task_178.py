"""
This module solves task 178_г from zadachi.pdf.
"""

from sys import argv


def task_function(numbers):
    """
    Description: convert string into int,
                 checks how many numbers in list are less than
                 the sum of the previous and next numbers.

    Args: list of strings in int number format, like ['3', '5', '10'].

    Return: count of numbers that are less than
            the sum of the previous and next numbers.

    """
    numbers = list(map(int, numbers))
    count = 0
    for first, second, third in zip(numbers, numbers[1:], numbers[2:]):
        if (first + third) / 2 > second:
            count += 1
    return count


def main():
    """Start 'task_function'."""
    try:
        print("Elements that correspond to the task condition:",
              task_function(argv[1:]))
    except ValueError:
        print("Type list of numbers in string format in a row", end=" ")
        print("like ['15', '12', '19'].")


if __name__ == "__main__":
    main()
