import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 1:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

def find_special_numbers(limit):
    prime = perfect = armstrong = None
    for i in range(limit - 1, 0, -1):
        if not prime and is_prime(i):
            prime = i
        if not perfect and is_perfect(i):
            perfect = i
        if not armstrong and is_armstrong(i):
            armstrong = i
        if prime and perfect and armstrong:
            break
    return prime, perfect, armstrong

# Test the function
input_num = 1000
prime, perfect, armstrong = find_special_numbers(input_num)
print(f"Prime: {prime}, Perfect: {perfect}, Armstrong: {armstrong}")
print("This program is written by KRITIKA ERP-067")
