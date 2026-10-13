# Anjelica Waller
# 10/13/26
# P4LAB2
# Use for/while loops to generate a multiplication table for a given number.

"""
Prompt the user to input an integer.
The program will generate a multiplication table for the given integer from 1 to 12.
If the user inputs a negative integer, display an error message indicating that the input is invalid.
The entire program will be contained within a while loop that allows the user to run the program multiple times.
At the end of the run, the program will ask the user if they would like to run the program again.
If the input is 'yes', the program will loop. If the input is 'no', the program will terminate.
"""

run_again = 'yes'
while run_again != 'no':


    number = int(input("Enter an integer: "))
    if number >= 0:
        print(f"Multiplication Table for {number}:")
        for i in range(1, 13):
            product = number * i
            print(f"{number} x {i} = {product}")
    else:
        print("Invalid input. Please enter a non-negative integer.")
    run_again = input("Would you like to run the program again? (yes/no): ")

print("Program terminated.")