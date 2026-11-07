# Anjelica Waller
# 11/7/26
# P5T: The Potion Pouch
# Program that randomizes HP and calculates how many potions are needed to restore HP.

import random

def drink_potions(hp_missing):

    large = hp_missing // 25
    hp_missing = hp_missing % 25
    if large == 1:
        print(large, "Large Potion")
    elif large > 1:
        print(large, "Large Potions")

    small = hp_missing // 5
    hp_missing = hp_missing % 5
    if small == 1:
        print(small, "Small Potion")
    elif small > 1:
        print(small, "Small Potions")

    print("Still missing:", hp_missing, "HP")

def main():
    gold = round(random.uniform(0.01, 100.00), 2)
    print(f"You find {gold:.2f} gold in the chest.")
    max_hp = int(input("What is your max HP? "))
    hp = random.randint(0, max_hp)
    print(f"A goblin hits you. You have {hp} HP left.")
    hp_missing = max_hp - hp
    print(f"You are missing {hp_missing} HP.")
    drink_potions(hp_missing)

main()
