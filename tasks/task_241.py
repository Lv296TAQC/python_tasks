""""Evaluate given difficult formula"""

from tasks.task_88d import is_natural


def difficult_formula(natural, x_val) -> complex:
    """Find algebraic sum for given formula

    :param natural: Any integer (natural) number
    :param x_val: Any float number

    :return: Result of equation

    :Example:

    In this example (205, 3) will be returned as (sum, quantity) of only numbers from
        list [5, 50, 3, 150, 11] which are dividing by 5 and not dividing by 7

    .. doctest::

        >>> print(difficult_formula(1, 25.05))
        (-25.05+0j)
    """
    result = 0
    i = 1
    while i <= natural:
        result += (pow(-1, (i ** 0.5))) / i * pow(x_val, i)
        i += 1
    return complex(result)


def is_natural_and_float(natural, x_val):
    """
    Check if valid data is entered.

    :param natural: Any integer (natural) number
    :param x_val: Any float number
    :return:  True, if input data is valid, False otherwise
    """
    if is_natural(natural):
        try:
            float(x_val)
        except (ValueError, TypeError):
            return False
        else:
            return True
    else:
        return False


def print_solution():
    """"Validate input, evaluate sum, print result"""
    natural, x_val = 1, 9.2
    if is_natural_and_float(natural, x_val):
        result = difficult_formula(int(natural), float(x_val))
        print(result)
    else:
        print("Invalid input. Please write correct values: natural number and float number")


if __name__ == '__main__':
    print_solution()
