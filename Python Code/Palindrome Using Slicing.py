def is_palindrome(s):
    # Remove whitespace and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Test the function
string = "MOM"
print(f"Is the string '{string}' a palindrome? {is_palindrome(string)}")
print("This program is written by KRITIKA ERP-067")
