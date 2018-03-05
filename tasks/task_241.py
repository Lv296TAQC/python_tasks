""""Evaluate given difficult formula"""

from tasks.task_88d import validate


def difficult_formula(natural, x_val):
    """Find algebraic sum for given formula

    Args:
        natural (int): Any integer (natural) number
        x_val (float): Any float number

    Returns:
        complex: Result of equation

    """
    result = 0
    i = 1
    while i <= natural:
        result += (pow(-1, (i ** 0.5))) / i * pow(x_val, i)
        i += 1
    return complex(result)


def validate_values(natural, x_val):
    """Check if valid data is entered

    Args:
        natural (int): Any integer (natural) number
        x_val (float): Any float number

    Returns:
        bool: True, if input data is valid, False otherwise

    """
    if validate(natural):
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
    if validate_values(natural, x_val):
        result = difficult_formula(int(natural), float(x_val))
        print(result)
    else:
        print("Invalid input. Please write correct values: natural number and float number")


if __name__ == '__main__':
    print_solution()
