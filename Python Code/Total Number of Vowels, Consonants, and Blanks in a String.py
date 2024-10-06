def count_elements(s):
    vowels = "aeiouAEIOU"
    num_vowels = sum(1 for char in s if char in vowels)
    num_consonants = sum(1 for char in s if char.isalpha() and char not in vowels)
    num_blanks = s.count(' ')
    return num_vowels, num_consonants, num_blanks

# Test the function
string = "Hello, how are you?"
vowels, consonants, blanks = count_elements(string)
print(f"Vowels: {vowels}, Consonants: {consonants}, Blanks: {blanks}")
print("This program is written by KRITIKA ERP-067")
