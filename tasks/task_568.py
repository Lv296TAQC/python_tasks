"""Insert between digits 1, 2, 3, 4, 5, 6, 7, 8, 9 concatenation, sum or division
    operators, so its result equals to given natural number
"""

from tasks.task_88d import is_natural


def find_subset(combination_id: int) -> int:
    """Evaluate subset for given id

    :param combination_id: Number (id) of subset, e.g. '5' - 00000012 - "1-2+3456789"
    :return: Evaluated number in decimal numeral system which represents evaluated subset

    :Example:

    In this example -456789 will be returned as a result of evaluation, received as result of next
        steps: converting 25 to ternary number, putting operations: concatenation if 0 in ternary,
        sum if 1 in ternary, division if 2 in ternary, in reversed order between set of numbers
        1 2 3 4 5 6 7 8 9. See example in parameters.

    .. doctest::

        >>> print(find_subset(25))
        -456789
    """
    result = 0
    l_bound = 0
    operation = 1
    for i in range(1, 10):
        l_bound = l_bound * 10 + i
        if combination_id % 3 != 0:
            if operation == 2:
                result -= l_bound
            else:
                result += l_bound
            l_bound = 0
            operation = combination_id % 3
        combination_id //= 3

    if operation == 2:
        result -= l_bound
    else:
        result += l_bound
    return result


def print_subset(combination_id: int):
    """Print given combination

    :param combination_id: Number (id) of subset, e.g. '5' - 00000012 in reverse order "1-2+3456789"
    """
    id_ = combination_id
    for j in range(1, 9):
        print(j, "" if id_ % 3 == 0 else "+" if id_ % 3 == 1 else "-", sep='', end='')
        id_ //= 3
    print("9", end='')


def single_solution(natural: int) -> str:
    """Find single solution for given number after validation

    :param natural: Any given integer (natural) number
    :return: First founded solution (equation) or message that it is
        impossible to generate such equation

    In this example 1-2+3-4+5-67+89 will be returned as a result of matching evaluated subset with
    number 25 and converting it to needed equation.

    .. doctest::

        >>> print(single_solution(25))
        1-2+3-4+5-67+89
    """
    lists = ""
    if is_natural(natural):
        for i in range(6561):
            calculated_value = find_subset(i)
            if calculated_value == int(natural):
                for j in range(1, 9):
                    lists += f"{j}"
                    lists += ("" if i % 3 == 0 else "+" if i % 3 == 1 else "-")
                    i //= 3
                lists += "9"
                return lists
        return "No possible solutions"
    return "Invalid input. Please write correct natural number"


def print_all_solutions(natural: int):
    """Validate input, find all possible subsets, print results

    Args:
        natural (int): Any given integer (natural) number
    """
    if is_natural(natural):
        print(f"\nAll possible subsets for given natural value '{natural}'")
        count = 0
        for i in range(6561):
            calculated_value = find_subset(i)
            if calculated_value == int(natural):
                count += 1
                print_subset(i)
                print(f" = {calculated_value} ({i})")

        if count == 0:
            print("Impossible to find needed combinations.")
        print(f"\nFound {count}", "combination." if count == 1 else "combinations.")
    else:
        print("Invalid input. Please write correct natural number")


if __name__ == '__main__':
    print(single_solution(121))
    print_all_solutions(121)
