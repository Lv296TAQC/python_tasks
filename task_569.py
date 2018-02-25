def is_prime(number_to_check):
    for num in range(2, number_to_check):
        if (number_to_check % num) == 0:
            return False
    else:
        return True

def prime_numbers(number):
    array=[]
    for num in range(6, number):
        if is_prime(num):
            array.append(num)
    return array

def divide_by_prime(number):
    for num in prime_numbers(number):
        if (number % num) == 0:
            return True
    return False

def validate(number):
    if number % 2 == 0 and number % 3 == 0 and number % 5 == 0 and not(divide_by_prime(number)):
        return True
    else:
        return False

print(validate(210))









#def verify_division(a, num):
    #for index, num in enumerate(a):
        #if num / 2 and num / 3 and num / 5:
            #a[index] = 0
