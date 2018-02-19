from math import sqrt


def squares_of_numbers(n):
    print("Результати пошуку записів,")
    print("які збігаються з останніми цифрами записів їх квадратів:")
    for number in range(1, n):
        if sqrt(number).is_integer():
            if str(int(sqrt(number))) == str(number)[-(len(str(number)) - 1):]:
                print(f"{int(sqrt(number))}^2 = {number}")


try:
    n = int(input("Введіть натуральне число > "))
    squares_of_numbers(n)
except ValueError:
    print("Введені Вами дані не являються натуральним числом.")
