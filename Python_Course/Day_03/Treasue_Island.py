print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to Treasue Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You are at crossland, where do you want to got? 'left' or 'right'. \n").lower()

if choice1 == "left":
    choice2 = input('you\'ve come to a lake, there is an island in the middle of the lake. Type \'wait\' to wait for boat,type \'swim\' to swim across \n').lower()
    if choice2 == 'wait':
        #Game will continue
        choice3 = input('You\'ve entered the island unharmed.There is house with 3 doors. One red, one yellow and one blue.\n').lower()
        if choice3 == 'red':
            print("It is a room full of fire, Game Over..!")
        elif choice3 == 'yellow':
            print("You found the treasure, you won the game")
        elif choice3 == 'blue':
            print("Room full of monsters, Game Over!")
        else:
            print("you choose the room that doesn't exist, Game over!")
    else:
        print("You got attacked buy crocodile, Game Over!")

else:
    print("Game Over!")

