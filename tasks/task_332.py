""""Equate lagrange's theorem for given number"""

from tasks.task_88d import is_natural


def lagrange(natural: int) -> tuple:
    """"Find needed squares of numbers

    :param natural: Any integer (natural) number
    :return:  Tuple of integers, which sum of squares is equals to given natural

    :Example:

    In this example tuple (3, 3, 2, 1) of natural numbers will be returned as 4 numbers, sum
        of squares of which is equal to number 23

    .. doctest::

        >>> print(lagrange(23))
        (3, 3, 2, 1)
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


def print_solution():
    """"Validate input, find each square of lagrange's theorem, print result."""
    natural = 188
    if is_natural(natural):
        combination = lagrange(int(natural))
        print(f"{natural} =", end='')
        for i, value in enumerate(combination):
            print(f" {value}^2({value ** 2})",
                  "" if len(combination) == i+1 else "+", end='')
    else:
        print("Invalid input. Please write correct natural number")


if __name__ == '__main__':
    print_solution()
