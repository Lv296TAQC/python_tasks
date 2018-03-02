"""Insert between digits 1, 2, 3, 4, 5, 6, 7, 8, 9 concatenation, sum or division
    operators, so its result equals to given natural number
"""

from tasks.task1_exercise88r import input_and_validate


def find_subset(id_):
    """Evaluate subset for given id

        Args:
            id_ (int): Number(id) of subset in ternary numeral system,
                e.g. '5' - 00000012 - "1234567+8-9"

        Returns:
            int: Evaluated number in decimal numeral system which represents evaluated subset

    """

    result = 0
    l_bound = 0
    operation = 1
    for i in range(1, 10):
        l_bound = l_bound * 10 + i
        if id_ % 3 != 0:
            if operation == 2:
                result -= l_bound
            else:
                result += l_bound
            l_bound = 0
            operation = id_ % 3
        id_ //= 3

    if operation == 2:
        result -= l_bound
    else:
        result += l_bound
    return result


def print_subset(combination_id):
    """Print given combination

            Args:
                combination_id (int): Number of subset in ternary numeral system,
                    e.g. '5' - 00000012 - "1234567+8-9"

    """

    id_ = combination_id
    for j in range(1, 9):
        print("{}".format(j), "" if id_ % 3 == 0 else "+" if id_ % 3 == 1 else "-", sep='', end='')
        id_ /= 3
    print("9", end='')


def single_solution(natural):
    """Find single solution for given number

        Args:
            natural (int): Any given integer (natural) number

        Returns:
            str: String that represents first founded solution (equation) or message that it
                is impossible to generate such equation

    """
    lists = ""
    for i in range(6561):
        calculated_value = find_subset(i)
        if calculated_value == natural:
            for j in range(1, 9):
                lists += "{}".format(j)
                lists += ("" if i % 3 == 0 else "+" if i % 3 == 1 else "-")
                i //= 3
            lists += "9"
            return lists
    return "No possible solutions"


def all_solutions_with_ui_output():
    """"Ask for valid input, find all possible subsets, print results"""
    natural = input_and_validate()
    print("\nSubsets for given natural value '{}'\n".format(natural))
    count = 0
    for i in range(6561):
        calculated_value = find_subset(i)
        if calculated_value == natural:
            count += 1
            print_subset(i)
            print(" = {} ({})".format(calculated_value, i))

    if count == 0:
        print("Impossible to find needed combinations.")
    print("\nFound {}".format(count), "combination." if count == 1 else "combinations.")
    return 0


if __name__ == '__main__':
    print(single_solution(55555))
    # print(eval(solution))
