# Anjelica Waller
# 9/7/2026
# P1LAB2 - Product Sales
# A program that demonstrates Input, Processing, and Output by calculating product sales.

product_type = input("Enter the product type")
item_count = int(input("Enter the item count"))
unit_price = float(input("Enter the unit price"))

total_price = item_count * unit_price
print(item_count,product_type + "(s)")
print("Price per unit:$" + str(unit_price))
print("Total price:$" + str(total_price))
print("Thank you for your order of", item_count, product_type + "(s) for a total of $" + str(total_price) + "!")
 