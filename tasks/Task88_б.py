try:
    number = int(input("Введіть натуральне число > "))

    def reverse_int(number):
        return int(str(number)[::-1])
    print(reverse_int(number))
except ValueError:
    print("Введені Вами дані не являються натуральним числом.")
