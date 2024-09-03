def print_patterns():
    # Pattern 1
    print("Pattern 1:")
    for i in range(1, 6):
        print('*' * i)
    print()  # Blank line for separation

    # Pattern 2
    print("Pattern 2:")
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end='')
        print()
    print()  # Blank line for separation

    # Pattern 3
    print("Pattern 3:")
    for i in range(1, 6):
        print(str(i) * i)
    print()  # Blank line for separation

    # Pattern 4
    print("Pattern 4:")
    for i in range(5, 0, -1):
        print('*' * i)
    print()  # Blank line for separation

    # Pattern 5
    print("Pattern 5:")
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end='')
        print()
    print()  # Blank line for separation

    # Pattern 6
    print("Pattern 6:")
    for i in range(5, 0, -1):
        print(str(i) * i)

# Call the function to print all patterns
print_patterns()
print("THIS PROGRAM IS WRITTEN BY KRITIKA ERP-067")
