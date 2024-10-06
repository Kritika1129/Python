def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def cube_of_primes(start, end):
    """Print the cube of prime numbers in a given range"""
    for num in range(start, end + 1):
        if is_prime(num):
            print(f"The cube of {num} is {num ** 3}")

# Take input from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

cube_of_primes(start, end)
print("This program is written by KRITIKA ERP-067")
