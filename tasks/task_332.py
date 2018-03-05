""""Equate lagrange's theorem for given number"""

from tasks.task_88d import input_and_validate


def lagrange(natural):
    """"Find needed squares of numbers

        Args:
            natural (int): Natural validated number from input

        Returns:
            tuple: Tuple of integers, which sum of squares is equals to given natural

    """
    natural_copy = natural
    x_val = int(natural_copy ** 0.5)
    while x_val > 0:
        natural_copy -= x_val * x_val
        y_val = int(natural_copy ** 0.5)
        natural_copy -= y_val * y_val
        z_val = int(natural_copy ** 0.5)
        natural_copy -= z_val * z_val
        t_val = int(natural_copy ** 0.5)
        if x_val * x_val + y_val * y_val + z_val * z_val + t_val * t_val == natural:
            return x_val, y_val, z_val, t_val
        else:
            natural_copy = natural
            x_val = x_val - 1


def main():
    """"Ask for valid input, find each square of lagrange's theorem, print result"""
    natural = input_and_validate()
    combination = lagrange(natural)
    print("{} =".format(natural), end='')
    for i in enumerate(combination):
        print(" {}^2({})".format(combination[i], combination[i]*combination[i]),
              "" if len(combination) == i+1 else "+", end='')


if __name__ == '__main__':
    main()
