#program to print the location of a specific character in a string
my_string="Bharati"
char_to_find=input("enter the character you want to find:")
positions=[i for i, char in enumerate (my_string)if char==char_to_find]
if positions:
    print(f"the character '{char_to_find}'is found at positions:{positions}");
else:
    print(f"the character '{char_to_find}'is not found in the string.");
print("this program is written by kritika erp-067")
