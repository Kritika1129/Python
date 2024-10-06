myAge = input("Enter age: ")
myAge = int(myAge)

if myAge >= 18:
    mycomment = "You are in middle school."
elif myAge >= 6:
    mycomment = "You are in primary school."
else:
    mycomment = "You are too small to learn Python."

print("At age " + str(myAge) + " -> " + mycomment)
print("This program is written by KRITIKA ERP-067")
