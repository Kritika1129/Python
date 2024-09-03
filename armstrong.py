def is_armstrong(number):
    total = 0
    num_digits = len(str(number))
    temp = number
    
    
    while temp > 0:
        digit = temp % 10 
        total += digit ** num_digits  
        temp //= 10  
    
    return total == number


number = int(input("Enter a number to check if it's an Armstrong number: "))


if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
print("this program is written by KRITIKA ERP-067")

