def is_armstrong(number):
    total = 0
    num_digits = len(str(number))
    temp = number
    
    # Loop to fetch each digit and calculate the sum of powers
    while temp > 0:
        digit = temp % 10  # Get the last digit
        total += digit ** num_digits  # Add digit raised to the power of num_digits
        temp //= 10  # Remove the last digit
    
    return total == number

def find_n_armstrong_after_x(x, n):
    count = 0
    current = x + 1  # Start checking from the number right after x
    
    print(f"First {n} Armstrong numbers after {x}:")
    while count < n:
        if is_armstrong(current):
            print(current, end=" ")
            count += 1
        current += 1

# Take user input for the given number and count of Armstrong numbers to find
x = int(input("Enter the number after which to find Armstrong numbers: "))
n = int(input("Enter the count of Armstrong numbers to find: "))

# Find and display the first n Armstrong numbers after x
find_n_armstrong_after_x(x, n)
