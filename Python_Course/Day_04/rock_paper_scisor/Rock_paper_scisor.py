import random
from figures import *

choice = input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors. \n")
your_choice = ""
my_choice = ""

if choice == "0":
    your_choice = rock
elif choice == "1":
    your_choice = paper
elif choice == "2":
    your_choice = scissors
else:
    print("you have choose the wrong option, you are disqualified from the game")
print("Your choice :")
print(your_choice)
print("Computer Choice :")
computer_choice = random.choice([rock, paper, scissors])
print(computer_choice)

if computer_choice == your_choice:
    print("It's a draw match")
elif (computer_choice == rock and your_choice == scissors) or (computer_choice == scissors and your_choice == paper) or (computer_choice == paper and your_choice == rock):
    print("You lose...")
else:
    print("You won...")