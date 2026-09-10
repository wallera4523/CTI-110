# Anjelica Waller
 # 9/10/26
 # P1HW2 - Travel Expenses
 # Program that calculates travel budgets

travel_budget = input("Enter your travel budget: ")
travel_destination = input("Enter your travel destination: ")
gas_price = input("How much will you spend on gas? ")
accommodation_cost = input("How much will you spend on accommodations? ")
food_cost = input("How much will you spend on food? ")
total_expenses = float(gas_price) + float(accommodation_cost) + float(food_cost)
remaining_budget = float(travel_budget) - total_expenses

print("Budget: $" + str(travel_budget))
print("Destination: " + travel_destination)
print("Total Expenses: $" + str(total_expenses))
print("Remaining Budget: $" + str(remaining_budget))