def countdown(n):
    while n > 0:
        yield n 
        n -= 1 
 
for number in countdown(5):	 
    print(number)  # Outputs: 5, 4, 3, 2, 1
print("This program is written by KRITIKA ERP-067")
