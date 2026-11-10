# Anjelica Waller
# 11/7/26
# P5LAB: Self-Checkout
#

"""
Set up main function and disperse_change function
Copy the code from P3LAB and put it in the disperse_change function to calculate the change
The program will randomly generate a total amount owed and prompt the user to enter the amount of cash they're paying with.
The program will then calculate the change and call the disperse_change function to calculate the number of dollars, 
quarters, dimes, nickels, and pennies needed to make change for the given amount of money.
"""

import random

def disperse_change(change):

    print(f"Change Amount: (${change:.2f})")

    change = int(round(change * 100))

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change

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


def main():
    money_owed = round(random.uniform(0.01, 100.00), 2)
    cash = float(input(f"Your total is ${money_owed:.2f}. How much cash are you paying with? $"))
    change = cash - money_owed
    disperse_change(change)

main()