"""
This module solves some tasks.
"""

import string


class Zzz:
    """Docstring."""

    def method1(self, var_x, var_y):
        """123."""
        pass

    @staticmethod
    def method2(var_zz, var_x):
        """Docstring."""
        if var_x:
            pass
        elif isinstance(str, var_zz):
            return 1
        return 2

    @staticmethod
    def method3(*args):
        """Docstring."""
        return sum(args)


print(1)
print(2)

SHIFT = 3
CHOICE = input("would you like to encode or decode?")
WORD = input("Please enter text")
print("wseiwger wegriywugeryuwgeurygweyugruywgrywge iwgeryiwgriwgeri \
      wireghwiur iuw riu wriuwh riuwh riuwheriuw hreiuhwiurhwi")
LETTERS = string.ascii_letters + string.punctuation + string.digits
ENCODED = ''
if CHOICE == "encode":
    for letter in WORD:
        if letter == ' ':
            ENCODED = ENCODED + ' '
        else:
            x = LETTERS.index(letter) + SHIFT
            ENCODED = ENCODED + LETTERS[x]
if CHOICE == "decode":
    for letter in WORD:
        if letter == ' ':
            ENCODED = ENCODED + ' '
        else:
            x = LETTERS.index(letter) - SHIFT
            ENCODED = ENCODED + LETTERS[x]

print(ENCODED)
