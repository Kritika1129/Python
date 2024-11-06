# my_package/math_operations.py

def add(x, y):
    """Return the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Return the difference of two numbers."""
    return x - y

def multiply(x, y):
    """Return the product of two numbers."""
    return x * y

def divide(x, y):
    """Return the quotient of two numbers."""
    if y == 0:
        return "Cannot divide by zero!"
    return x / y
# we will import this file into our main file


# main.py

# Import the package and its modules
from my_package import math_operations

def main():
    a = 10
    b = 5

    print(f"Addition of {a} and {b}: {math_operations.add(a, b)}")
    print(f"Subtraction of {a} and {b}: {math_operations.subtract(a, b)}")
    print(f"Multiplication of {a} and {b}: {math_operations.multiply(a, b)}")
    print(f"Division of {a} and {b}: {math_operations.divide(a, b)}")
print("This program is written by KRITIKA ERP-067")
if __name__ == "__main__":
    main()
#this is our main file 
