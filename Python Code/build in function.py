user_input = input("Enter the numbers separated by spaces: ")
input_list = user_input.split()
numbers = list(map(int, input_list))
total = sum(numbers)
length = len(numbers)
sorted_numbers = sorted(numbers)

print(f"Original list of numbers: {numbers}")
print(f"Sum of numbers: {total}")
print(f"Number of elements: {length}")
print(f"Sorted list of numbers: {sorted_numbers}")
print("THIS PROGRAM IS WRITTEN BY Sachin ERP-025")
