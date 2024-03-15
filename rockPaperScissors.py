#learning user input and control flow

import sys
import random

print("")
playerChoice = input("Enter a choice...\n1 Rock\n2 Paper\n3 Scissors:\n\n")

player = int(playerChoice)

if player<1|player>3:
    sys.exit("You must enter 1,2 or 3")

computerChoice  = random.choice("123")

computer= int(computerChoice)

print("")
print ("You chose " + playerChoice +".\nComputer chose "+ computerChoice+".")

if player==1:
    if computer==1:
        print("\nIt's a tie!\n")
    elif computer==2:
        print("\nYou Win!!\n")
    elif computer==3:
        print("\nYou Lose...\n")
elif player==2:
    if computer==1:
        print("\nYou Win!!\n")
    elif computer==2:
        print("\nIt's a tie!\n")
    elif computer==3:
        print("\nYou Lose...\n")
elif player==3:
    if computer==1:
        print("\nYou Lose...\n")
    elif computer==2:
        print("\nYou Win!!\n")
    elif computer==3:
        print("\nIt's a tie!\n")