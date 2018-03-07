"""In the sequence replace with zeros members, which absolute/p gives the reminder q"""


def update(number_p, number_q, sequence):
    """Method for replacing p, q, array"""
    if (number_p <= number_q) or (number_q < 0):
        return 'incorrect values'
    for k, element in enumerate(sequence):
        if abs(element) % number_p == number_q:
            sequence[k] = 0
    return sequence


print(update(43, 12, [23, 34, 123, 43, 34, 12]))
