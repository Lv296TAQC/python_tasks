""""Evaluate given difficult formula"""

from tasks.task_88r import input_and_validate


def difficult_formula(natural, x_val):
    """Find algebraic sum for given formula

        Args:
            natural (int): Randomly generated list of integers
            x_val (float): Randomly generated list of integers

        Returns:
            result: Result of equation

    """
    result = 0
    i = 1
    while i <= natural:
        result += (pow(-1, (i ** 0.5))) / i * pow(x_val, i)
        i += 1
    return result


def while_not_correct_values():
    """Ask for input until valid data entered

            Returns:
                tuple: Tuple of inputted float and integer values

    """
    x_val = input("Enter real number: ")
    try:
        x_val = float(x_val)
    except ValueError:
        print("Not a number, please write correct (natural number) value")
    return input_and_validate(), x_val


def main():
    """"Ask for valid input, evaluate sum, print result"""
    natural, x_val = while_not_correct_values()
    result = difficult_formula(natural, x_val)
    print(result)


if __name__ == '__main__':
    main()
