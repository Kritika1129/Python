import importlib

# Dynamically import the math_utils module
math_utils = importlib.import_module('maths_utils')

# Call the add function from the math_utils module
result = math_utils.add(5, 3)

# Print the result
print(result)
