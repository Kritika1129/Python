# Creating a nested tuple
nested_tuple = (1, 2, (3, 4, (5, 6)))

# Accessing elements
print("First element:", nested_tuple[0])              # 1
print("Second element:", nested_tuple[1])             # 2
print("Nested element (3rd position):", nested_tuple[2])  # (3, 4, (5, 6))
print("Access 4 inside nested tuple:", nested_tuple[2][1])  # 4
print("Access 6 deeply nested:", nested_tuple[2][2][1])     # 6

# This program is written by Kritika ERP-067
