from typing_extensions import get_origin
from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")

if difficulty_level == "easy":
    no_of_attempts = 10
else :
    no_of_attempts = 5

actual_number = random.randint(1, 100)

for i in range(no_of_attempts):
    guess_number = int(input("Make a guess: "))
    if guess_number > actual_number:
        print("Too high")
        print("Guess again.")
    elif guess_number < actual_number:
        print("Too Low")
        print("Guess again.")
    else:
        print(f"You have guessed it correctly, the number is {actual_number}")
        break
    print(f"You have {no_of_attempts-(i+1)} attempts remaining")