bill_amount = float(input("Enter the bill amount: "))
sum_digits = 0
num = int(bill_amount)


while num > 0:
    sum_digits += num % 10
    num //= 10


if bill_amount < 10000:
    discount = 0.5 * sum_digits
else:
    discount = sum_digits


final_bill = bill_amount - discount


print(f"Discount: {discount}")
print(f"Final Bill: {final_bill}")
print("this program is written by KRITIKA erp-067")

