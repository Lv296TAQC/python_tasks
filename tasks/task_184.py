"""
In the sequence replace with zeros members, which absolute/p gives the reminder q. Solves task 184 from zadachi.pdf
"""


def update(number_p, number_q, sequence):
    """
    Method replace with zeros members, which absolute/p gives the reminder q

    Arg:
        int numbers, sequence
    Return:
        sequence of numbers
    Example:
        print(update(2, 1, [3 , 4])) --> [0, 4]
        print(update(1, 2, [5, 4])) --> incorrect values
    """
    if (number_p <= number_q) or (number_q < 0):
        return 'incorrect values'
    for k, element in enumerate(sequence):
        if abs(element) % number_p == number_q:
            sequence[k] = 0
    return sequence
