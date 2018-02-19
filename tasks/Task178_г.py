try:
    numbers = list(map(int, input("Введіть послідовність чисел: ").split()))
    count = 0
    for first, second, third in zip(numbers, numbers[1:], numbers[2:]):
        if (first + third) / 2 > second:
            count += 1
    print(f"Кількість елементів, які відповідають умові завдання: {count}")
except ValueError:
    print("Введені Вами дані не являються натуральним числом.")
