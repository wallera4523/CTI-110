# CTI-110
# P3LAB1 - Dungeon Gatekeeper
# Anjelica Waller
# 9/27/2026

# Print welcome message
print("=== ADVENTURER CHECK-IN TERMINAL ===")

# Prompt user to input character level
character_level = int(input('Enter your character level: '))

# Using if/else logic, determine if the user's level is high enough to enter the dungeon
if character_level >= 21:
    print(f'Clearance granted! Welcome to the Dragon Spire\'s dungeon.')
else:
    print(f'Clearance denied! You are level {character_level}. You must be at least level 21 to enter.')

# Prompt user to input potion count
potions = int(input("How many health potions are you carrying? "))

# Using if/else logic again, determine the appropriate message to give the user based on the potion amount, as well as an error message for invalid inputs
if potions == 0:
    print("Warning: You have no potions equipped! Entering without healing is dangerous.")
if potions == 1:
    print("Equipped: 1 Health Potion.")
if potions > 1:
    print(f"Equipped: {potions} Health Potions.")
if potions < 0:
    print("Invalid potion count.")

