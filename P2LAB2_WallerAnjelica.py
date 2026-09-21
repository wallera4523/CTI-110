# This program will calculate the amount of gas needed to drive a certain distance based on the miles per gallon (mpg) of a specific car. The user will be prompted to enter a car name and the distance they plan to drive, and the program will output the amount of gas needed for that trip.
# Create a dictionary of cars and their corresponding miles per gallon (mpg) values. The keys are the car names, and the values are the mpg values.
cars = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}
cars_keys = cars.keys()

# Print the keys of the cars dictionary to show the available car options to the user. The keys are printed in a comma-separated format for better readability.
print(cars_keys)
print(*cars_keys, sep=', ')

# Prompt the user to enter a car name from the available options. The input is case-sensitive, so the user must enter the car name exactly as it appears in the dictionary keys.
car_name = input("Enter a car name: ")

car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon.")

# Calculate the amount of gas needed to drive a certain distance based on the miles per gallon (mpg) of the selected car. The user is prompted to enter the distance they plan to drive, and the program calculates the gallons of gas needed using the formula: gallons_needed = miles_driven / car_mpg.
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))
gallons_needed = miles_driven / car_mpg
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles. ")
