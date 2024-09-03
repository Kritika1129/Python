# Simple program to demonstrate while, break, and continue

count = 1

while count <= 10:
    if count == 5:
        # Skip printing 5
        count += 1
        continue
    
    print(count)
    count += 1

print("Done")
print("this program is written by KRITIKA ERP-067")

