import math

def is_prime(number):
    if number < 2:
        return False
    else:
        for n in range(2,number):
            if number % n == 0:
               return False
        return True

def factorial(number):
    result=1
    for i in range(1,number+1):
        result=result*i
    return result

def palindrome(list):
    return list==list[::-1]


def sqrt(number):
    root = math.sqrt(number)
    return int(root + 0.5) ** 2 == number
