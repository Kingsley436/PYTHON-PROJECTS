# Import random
# Define a function to roll the dice
# Create a dictionary that will have the drawings of the dice
# Create a dictionary that will have the values of the dice
# Create a while loop to ask user whether they want to continue or not


import random


def roll_dice():

    dice_drawings = {
        1: (
            "┌─────────┐",
            "│    1    │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│    2    │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ● 3    │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    4    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ● 5 ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ● 6 ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }

    roll = input("Do you want to roll the dice? (Yes/No)  ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print()

        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawings[dice1]))
        print("\n".join(dice_drawings[dice2]))
        print()

        roll = input("Roll again? (Yes/No):  ")
        print()


roll_dice()
