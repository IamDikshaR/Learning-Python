#learning user input and control flow

import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")
playerChoice = input("Enter a choice...\n1 Rock\n2 Paper\n3 Scissors\n\n")

player = int(playerChoice)

if player<1|player>3:
    sys.exit("You must enter 1,2 or 3")

computerChoice  = random.choice("123")

computer= int(computerChoice)

print("")
print ("You chose " + str(RPS(player)).replace('RPS.', '') +".\nComputer chose "+ str(RPS(computer)).replace('RPS.', '')+".")

# if player==1:
#     if computer==1:
#         print("\nIt's a tie!\n")
#     elif computer==3:
#         print("\nYou Win!!\n")
#     elif computer==2:
#         print("\nYou Lose...\n")
# elif player==2:
#     if computer==1:
#         print("\nYou Win!!\n")
#     elif computer==2:
#         print("\nIt's a tie!\n")
#     elif computer==3:
#         print("\nYou Lose...\n")
# elif player==3:
#     if computer==1:
#         print("\nYou Lose...\n")
#     elif computer==2:
#         print("\nYou Win!!\n")
#     elif computer==3:
#         print("\nIt's a tie!\n")

if player==1 and computer==3:
    print("\nYou win!!\n")
elif player==2 and computer==1:
    print("\nYou win!!\n")
elif player==3 and computer==2:
    print("\nYou win!!\n")
elif player==computer:
    print("\nIt's a tie!\n")
else:
    print("\nComputer wins...\n")