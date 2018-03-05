""""Equate lagrange's theorem for given number"""

from tasks.task_88d import validate


def lagrange(natural):
    """"Find needed squares of numbers

    Args:
        natural (int): Any integer (natural) number

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


def print_solution():
    """"Validate input, find each square of lagrange's theorem, print result"""
    natural = 188
    if validate(natural):
        combination = lagrange(int(natural))
        print(f"{natural} =", end='')
        for i, value in enumerate(combination):
            print(f" {value}^2({value ** 2})",
                  "" if len(combination) == i+1 else "+", end='')
    else:
        print("Invalid input. Please write correct natural number")


if __name__ == '__main__':
    print_solution()
