# Anjelica Waller
# 10/6/26
# M3BONUS
# A dungeon-themed text adventure based on the game show concept of the original file.

"""
PSEUDOCODE
Display the welcome banner
Ask the player to pick door 1, 2, 3, 4, 5, or 6
If the player picks 1: go to the skeleton room
Elseif the player picks 2: go to the shield room
Elseif the player picks 3: go to the armor room
Elseif the player picks 4: go to the mimic room
Elseif the player picks 5: go to the spider room
Elseif the player picks 6: meet Jerry the goblin
Else: Error message: "That is not a door."
"""



def door_1():
    print()
    print("You stumble upon a decrepit skeleton wielding a rusted sword. Will you fight it or run away?")
    print("1: Fight")
    print("2: Run away")
    door1_outcome = input("Choose your action (1 or 2): ")
    if door1_outcome == "1":
        print("The skeleton falls apart with one swing of your sword. You win: a rusty sword and a pile of bones.")
    elif door1_outcome == "2":
        print("You run away safely, but you feel like you've missed an opportunity. You win: nothing.")
    else:
        print("Invalid choice. The skeleton attacks you while you hesitate. You have died.")

def door_2():
    print()
    print("You enter a room and find an ancient shield leaning against the wall. Will you take it or leave it?")
    print("1: Take the shield")
    print("2: Leave it")
    door2_outcome = input("Choose your action (1 or 2): ")
    if door2_outcome == "1":
        print("You take the shield and feel a surge of protection. You win: an ancient shield.")
    elif door2_outcome == "2":
        print("You leave the shield behind, but you feel a sense of loss. You win: nothing.")
    else:
        print("Invalid choice. The shield magically disappears, and you are left empty-handed.")

def door_3():
    print()
    print("You enter a room and immediately notice a skeleton leaning against the wall, wearing a suit of armor. It doesn't appear to be sentient. Will you take the armor or leave it?")
    print("1: Take the armor")
    print("2: Leave it")
    door3_outcome = input("Choose your action (1 or 2): ")
    if door3_outcome == "1":
        print("You take the armor and feel a sense of invincibility. You win: a suit of armor.")
    elif door3_outcome == "2":
        print("You leave the armor behind, but you feel a sense of regret. You win: nothing.")
    else:
        print("Invalid choice. You are left empty-handed.")

def door_4():
    print()
    print("You enter a room and find a chest full of shimmering gold. Do you take the gold or leave it?")
    print("1: Take the gold")
    print("2: Leave it")
    door4_outcome = input("Choose your action (1 or 2): ")
    if door4_outcome == "1":
        print("As you lift the lid on the chest, you realize it's a mimic! It easily overpowers you and devours you whole. You have died.")
    elif door4_outcome == "2":
        print("You figure it's too good to be true and leave the chest alone. You win: nothing.")
    else:
        print("Invalid choice. The mimic attacks you while you hesitate. You have died.")

def door_5():
    print()
    print("As you enter the room, you immediately step in something sticky. Before you can react, a giant spider descends from the ceiling and attacks. What will you do?")
    print("1: Fight the spider")
    print("2: Try to befriend it.")
    print("3: Run away:")
    door5_outcome = input("Choose your action (1, 2, or 3): ")
    if door5_outcome == "1":
        print("You raise your sword to strike the spider, but it immediately shoots a web that pins your arm to the wall. It eats you alive. You have died.")
    elif door5_outcome == "2":
        print("You try to befriend the spider, but it doesn't seem interested. It ignores your pleas and attacks you. You have died.")
    elif door5_outcome == "3":
        print("You quickly turn and run, but the spider is faster. It catches up and eats you alive. You have died.")
    else:
        print("Invalid choice. The spider attacks you while you hesitate. You have died.")

def door_6():
    print()
    print("You enter a room and stumble upon a goblin named Jerry. He offers you 10G for every second you can hold a handstand, with a 1.5x bonus for any time over 40 seconds.")
    handstand_time = float(input("Enter the number of seconds you can hold a handstand: "))
    if handstand_time < 0:
        print("Invalid input. Handstand time cannot be negative.")
    elif handstand_time <= 40:
        reward = handstand_time * 10
        print(f"You held a handstand for {handstand_time:.2f} seconds. You earned {reward:.2f}G.")
    else:
        bonus_seconds = handstand_time - 40
        reward = 40 * 10 + bonus_seconds * 10 * 1.5
        print(f"You held a handstand for {handstand_time:.2f} seconds! You earned {reward:.2f}G.")

    print("-----CHALLENGE COMPLETE-----")
    print(f"{'Total seconds:' :<20} {handstand_time:.2f}")
    if handstand_time > 40:
        print(f"{'Bonus seconds:' :<20} {bonus_seconds:.2f}")
        print(f"{'Base pay:' :<20} {40 * 10:.2f}G")
        print(f"{'Bonus pay:' :<20} {bonus_seconds * 10 * 1.5:.2f}G")
        print(f"{'Total reward:' :<20} {reward:.2f}G")
    if handstand_time <= 40:
        print(f"{'Bonus seconds:' :<20} 0")
        print(f"{'Base pay:' :<20} {reward:.2f}G")
        print(f"{'Bonus pay:' :<20} 0")
        print(f"{'Total reward:' :<20} {reward:.2f}G")
    print("-" * 28)


def start():
    print("=" * 40)
    print("You find yourself in a dark, musty dungeon. There are six doors in front of you. Which one do you choose?")
    print("=" * 40)
    choice = input("Pick a door (1, 2, 3, 4, 5, or 6): ")
    if choice == "1":
        door_1()
    elif choice == "2":
        door_2()
    elif choice == "3":
        door_3()
    elif choice == "4":
        door_4()
    elif choice == "5":
        door_5()
    elif choice == "6":
        door_6()
    else:
        print("That's not a door. Please try again.")

start()
