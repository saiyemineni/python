import turtle as t
import pandas as pd
from pandas._libs import missing

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
missied_states = data.state.to_list()


screen = t.Screen()
screen.title("U.S. States Game")
image = r"C:\Users\yevenkat\Desktop\Python_Learning\Python_Course\Day_25\us-states-game-start\blank_states_img.gif"
screen.addshape(image)

guessed_state = []

t.shape(image)

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/{len(all_states)}Guess the state",prompt="what is the another state ?").title()
    print(answer)

    if answer == "Exit":
        print(len(missied_states))
        new_data = pd.DataFrame(missied_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states:
        state_coor_x = int(data[data.state == answer]['x'])
        state_coor_y = int(data[data.state == answer]['y'])
        new_turtle = t.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(state_coor_x, state_coor_y)
        new_turtle.write(answer)
        guessed_state.append(answer)
        missied_states.remove(answer)
    
# def get_mouse_click_coor(x, y):
#     print(x, y)
# t.onscreenclick(get_mouse_click_coor)
# t.mainloop()



