"""
This module solves task 331_a from zadachi.pdf.
"""

from sys import argv


def sum_of_squares(number):
    """
    Description: checks whether the number is the sum
                 of the squares of three numbers.
    Arg: int number.
    Return: squares of three numbers.
    """
    number = int(number)
    var_x = 1
    while var_x * var_x <= number:
        var_y = 1
        while var_y * var_y <= number:
            var_z = 1
            while var_z * var_z <= number:
                if var_x*var_x + var_y*var_y + var_z*var_z == number:
                    return var_x, var_y, var_z
                var_z = var_z + 1
            var_y = var_y + 1
        var_x = var_x + 1
    return False


try:
    if sum_of_squares(argv[1]):
        VAL_X, VAL_Y, VAL_Z = sum_of_squares(argv[1])
        print(f"The number {argv[1]} is the sum", end=" ")
        print("of the squares of three numbers:")
        print(f"{argv[1]} = {VAL_X}^2 + {VAL_Y}^2 + {VAL_Z}^2")
    else:
        print(f"The number {argv[1]} isn't the sum", end=" ")
        print("of the squares of three numbers.")
except ValueError:
    print("Inputted data isn't integer.")
