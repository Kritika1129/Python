def right_angled_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

def incremental_numbers(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def repeating_digits(n):
    for i in range(1, n + 1):
        print(str(i) * i)

def inverted_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

def decreasing_digits(n):
    for i in range(n, 0, -1):
        for j in range(n, n - i, -1):
            print(j, end="")
        print()

def decreasing_line_repeating_digits(n):
    for i in range(n, 0, -1):
        print(str(i) * i)


n = 5


right_angled_triangle(n)
print()  

incremental_numbers(n)
print()  

repeating_digits(n)
print()  

inverted_triangle(n)
print() 

decreasing_digits(n)
print() 
decreasing_line_repeating_digits(n)
