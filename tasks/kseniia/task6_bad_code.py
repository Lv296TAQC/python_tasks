"""pass"""
import string


class Zzz():
    """pass"""

    def method1(self, arg1, arg2):
        """123"""

    @staticmethod
    def method2(arg):
        """pass"""
        if arg:
            pass
        if isinstance("zz", str):
            return 1
        return 2

    @staticmethod
    def method3(*args):
        """pass"""
        return sum(args)


def func():
    """pass"""
    shift = 3
    choice = input("would you like to encode or decode?")
    word = input("Please enter text")
    print("wseiwger wegriywugeryuwgeurygweyugruywgrywgeiwgeryiwgriw \
          geri wireghwiur iuw riu wriuwh riuwh riuwheriuw hreiuhwiurhwi")
    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ''

    if choice == "encode":
        for letter in word:
            if letter == ' ':
                encoded = encoded + ' '
            else:
                index = letters.index(letter) + shift
                encoded = encoded + letters[index]

    if choice == "decode":
        for letter in word:
            if letter == ' ':
                encoded = encoded + ' '
            else:
                index = letters.index(letter) - shift
                encoded = encoded + letters[index]

    return encoded


print(1)
print(2)

print(func())
