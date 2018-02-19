def sum_of_squares(n):
    x = 1
    while x * x <= n:
        y = 1
        while y * y <= n:
            if x * x + y * y == n:
                print(f"Число {n} представляє собою суму")
                print("двох квадратів натуральних чисел:")
                print(f"{n} = {x}^2 + {y}^2")
                return True
            y = y + 1
        x = x + 1
    return False


try:
    n = int(input("Введіть натуральне число > "))
    if sum_of_squares(n):
        print("Розрахунки завершені.")
    else:
        print(f"Число {n} не являється сумою")
        print("двох квадратів натуральних чисел.")
except ValueError:
    print("Введені Вами дані не являються натуральним числом.")
