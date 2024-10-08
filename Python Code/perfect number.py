def is_perfect(n):
    """
    Returns True if n is a perfect number, False otherwise.
    """
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

# Test the function
num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
