# Input marks
roll_no = input("Enter Roll-no: ")
name = input("Enter Name: ")
student_class = input("Enter Class: ")
eng = int(input("English marks: "))
maths = int(input("Maths marks: "))
science = int(input("Science marks: "))
sst = int(input("Social Science marks: "))
computer = int(input("Computer marks: "))

# Calculate total marks
total = eng + maths + science + sst + computer
max_marks = 500  # Total maximum marks
percentage = (total / 5) * 100

# Print the formatted output using f-strings
print(f"\nROLL NO : \t\t {roll_no}")
print(f"NAME : \t\t {name}")
print(f"CLASS : \t\t {student_class}")

print("--------------------------------------------------")
print("SUBJECT \t FULL MARKS \t OBTAINED MARKS")

print(f"ENGLISH \t 100 \t\t {eng}")
print(f"MATHS   \t 100 \t\t {maths}")
print(f"SCIENCE \t 100 \t\t {science}")
print(f"SOCIAL SCIENCE \t 100 \t\t {sst}")
print(f"COMPUTER \t 100 \t\t {computer}")

print("------------------------------------------------------")
print(f"TOTAL    \t {max_marks} \t\t {total}")
print("-----------------------------")

# Determine the grade
if percentage >= 80:
    print("GRADE: A")
elif percentage >= 70:
    print("GRADE: B")
elif percentage >= 60:
    print("GRADE: C")
elif percentage >= 50:
    print("GRADE: D")
elif percentage >= 40:
    print("GRADE: F")
    print("You have failed.")
else:
    print("GRADE: F")
    print("You have failed.")
print("this program is written by kritika erp-067")
