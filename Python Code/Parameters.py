#Positional Parameters 
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.") 
greet("Alice", 30)
print("The result of Positional Parameters")
#Default Parameters
def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.") 
 
greet("Alice")
print("The result of Default Parameters")

#Keyword Parameters
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.") 
 
greet(name="Alice", age=30)
print("The result of Keyword Parameters")


#Variable-Length Parameters 
#The *args parameter allows a function to accept any number of positional arguments. 
 
def sum_numbers(*args): 
    return sum(args)
print(sum_numbers(1, 2, 3))       # Output: 6 
print(sum_numbers(4, 5, 6, 7, 8)) # Output: 30
print("The result of Variable-Length (args) Parameters")
#The **kwargs parameter allows a function to accept any number of keyword arguments. 
 
def print_info(**kwargs):
    for key, value in kwargs.items(): 
        print(f"{key}: {value}") 
print_info(name="Alice", age=30, city="New")
print("The result of Variable-Length(kwargs) Parameters")
print("This program is written by KRITIKA ERP-067")




