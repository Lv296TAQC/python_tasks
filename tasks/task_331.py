"""
This module solves task 331_a from zadachi.pdf.
"""

from sys import argv


def sum_of_three_squares(number):
    """
    Description: converts string into int,
                 checks whether the number is the sum
                 of the squares of three numbers.

    Arg: string in int number format, like "17".

    Return: tuple with squares of three numbers.

    """
    number = int(number)
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
    """Start 'sum_of_three_squares' function."""
    try:
        if sum_of_three_squares(argv[1]):
            first, second, third = sum_of_three_squares(argv[1])
            print(f"The number {argv[1]} is the sum", end=" ")
            print("of the squares of three numbers:")
            print(f"{argv[1]} = {first}^2 + {second}^2 + {third}^2")
        else:
            print(f"The number {argv[1]} isn't the sum", end=" ")
            print("of the squares of three numbers.")
    except ValueError:
        print("Please type number in string format, like '29'.")


if __name__ == "__main__":
    main()
