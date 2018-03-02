"""
This module solves task 88_б from zadachi.pdf.
"""

from sys import argv


def reverse_int(number):
    """
    Description: reverse string and return as int number.

    Arg: string in int number format, like "12".

    Return: reversed int number.

    """
    return int(number[::-1])


def main():
    """Start 'reverse_int' function."""
    try:
        print(reverse_int(argv[1]))
    except ValueError:
        print("Please type number in string format, like '15'.")


if __name__ == "__main__":
    main()
