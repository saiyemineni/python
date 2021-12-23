from typing import Text
import pandas as pd
import random
import tkinter

current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(card_title, text= "French", fill= "black")
    canvas.itemconfig(card_text, text=current_card["French"], fill= "black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English", fill= "white")
    canvas.itemconfig(card_text, text=current_card["English"], fill= "white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# french_words_list = data["French"].to_list()
# english_words_list = data["English"].to_list()
# word_pairs = {}

# for i in range(len(french_words_list)):
#     word_pairs[french_words_list[i]] = english_words_list[i] 


# def random_choice():
#     french, english = random.choice(list(word_pairs.items()))
#     print(french, english)
    

BACKGROUND_COLOR = "#B1DDC6"

window = tkinter.Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width= 800, height= 526)
card_front_image = tkinter.PhotoImage(file="images\card_front.png")
card_back_image = tkinter.PhotoImage(file="images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40,"italic"))
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row= 0, column= 0, columnspan=2)

cross_image = tkinter.PhotoImage(file="images\wrong.png")
unknow_button = tkinter.Button(image=cross_image, highlightthickness=0, command= next_card)
unknow_button.grid(row= 1, column= 0)

check_image = tkinter.PhotoImage(file="images\\right.png")
known_button = tkinter.Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row= 1, column= 1)


next_card()

window.mainloop()