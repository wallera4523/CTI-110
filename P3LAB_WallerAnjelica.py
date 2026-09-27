# Anjelica Waller
# 9/16/2026
# P3LAB - Money Calculator
# This program calculates the number of dollars, quarters, dimes, nickels, and pennies needed to make change for a given amount of money.

# Prompt the user to enter an amount of money
change = float(input("Enter an amount of money: $"))

print(f"Change Amount: (${change:.2f})")

# Convert the change amount to cents
change = int(round(change * 100))

# Calculate the number of dollars, quarters, dimes, nickels, and pennies

num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change

# If and else statements to print the number of each type of coin, with proper singular/plural formatting
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} dollar")
    else:
        print(f"{num_dollars} dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} quarter")
    else:
        print(f"{num_quarters} quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} dime")
    else:
        print(f"{num_dimes} dimes")

if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} nickel")
    else:
        print(f"{num_nickels} nickels")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} penny")
    else:
        print(f"{num_pennies} pennies")

if num_dollars == 0 and num_quarters == 0 and num_dimes == 0 and num_nickels == 0 and num_pennies == 0:
    print("No change.")