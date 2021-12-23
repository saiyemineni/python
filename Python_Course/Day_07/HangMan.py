import random
import os 
from Hangman_Art import *
from hangman_words import *


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(logo)

# # #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    os.system('cls')
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose..")

    print(" ".join(display))
    if "_" not in display:
        end_of_game = True
        print("You Win..!")
    print(stages[(len(stages)-lives)-1])