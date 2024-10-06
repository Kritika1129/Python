def categorize_numbers(start, end):
    even_numbers = []
    divisible_by_5 = []
    other_numbers = []

    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
        elif num % 5 == 0:
            divisible_by_5.append(num)
        else:
            other_numbers.append(num)
    
    print("Even numbers:", even_numbers)
    print("Numbers divisible by 5:", divisible_by_5)
    print("Other numbers:", other_numbers)

# Define the range
start_range = 1
end_range = 20

# Categorize and print the numbers
categorize_numbers(start_range, end_range)
print("This program is written by KRITIKA ERP-067")

