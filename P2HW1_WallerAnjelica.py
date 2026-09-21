# Anjelica Waller
 # 9/10/26
 # P1HW2 - Travel Expenses
 # Program that calculates travel budgets

# The program will ask the user for their travel budget, destination, and other estimated expenses.
travel_budget = input("Enter your travel budget: ")
travel_destination = input("Enter your travel destination: ")
gas_price = input("How much will you spend on gas? ")
accommodation_cost = input("How much will you spend on accommodations? ")
food_cost = input("How much will you spend on food? ")
# After all inputs are collected, the program will calculate the total expenses and remaining budget.
total_expenses = float(gas_price) + float(accommodation_cost) + float(food_cost)
remaining_budget = float(travel_budget) - total_expenses
# The program will print a receipt based on the information provided by the user. Formatting used for a more tidy result.
print("------ Travel Budget Receipt ------")
print(f'{"Total Budget:":<18} ${float(travel_budget):.2f}')
print(f'{"Destination:":<18} {travel_destination}')
print(f'{"Total Expenses:":<18} ${total_expenses:.2f}')
print('-'*35) 
print(f'{"Remaining Budget:":<18} ${remaining_budget:.2f}')