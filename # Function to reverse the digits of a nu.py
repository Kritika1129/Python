# Function to reverse the digits of a number
def reverse_number(num):
    reversed_num = 0
    
    while num > 0:
        last_digit = num % 10         # Get the last digit
        reversed_num = reversed_num * 10 + last_digit  # Append last digit to reversed_num
        num = num // 10               # Remove the last digit from num
    
    return reversed_num

# Input from the user
number = int(input("Enter a number: "))

# Call the function and display the reversed number
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)
print("this program is written by KRITIKA ERP-067")

