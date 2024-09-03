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

# Function to print all Armstrong numbers in a given range and count them
def find_armstrong_in_range(start, end):
    count = 0
    print(f"Armstrong numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_armstrong(number):
            print(number, end=" ")
            count += 1
    print(f"\nTotal Armstrong numbers found: {count}")

# Take user input for range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Find and display Armstrong numbers in the given range
find_armstrong_in_range(start, end)
print("this program is written by KRITIKA ERP-067")
