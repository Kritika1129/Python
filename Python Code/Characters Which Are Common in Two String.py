def common_characters(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    common_chars = set1.intersection(set2)
    return ''.join(common_chars)

# Test the function
string1 = "apple"
string2 = "pineapple"
print("Common characters:", common_characters(string1, string2))
print("This program is written by KRITIKA ERP-067")


