try:
    number = int(input("enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input, please enter a valid number")
else:
    print("The result is:", result)
print("This program is written by KRITIKA ERP-076")
