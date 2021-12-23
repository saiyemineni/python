from turtle import Turtle, Screen

timmy = Turtle()

# for _ in range(3):
#     timmy.forward(100)
#     timmy.left(120)

# for _ in range(4):
#     timmy.pencolor('coral')
#     timmy.forward(100)
#     timmy.left(90)

# for _ in range(5):
#     timmy.pencolor('blue')
#     timmy.forward(100)
#     timmy.left(72)

# for _ in range(6):
#     timmy.pencolor('orange')
#     timmy.forward(100)
#     timmy.left(60)

# for _ in range(7):
#     timmy.pencolor('green')
#     timmy.forward(100)
#     timmy.left(51.5)

# for _ in range(8):
#     timmy.pencolor('purple')
#     timmy.forward(100)
#     timmy.left(45)

# for _ in range(9):
#     timmy.pencolor('yellow')
#     timmy.forward(100)
#     timmy.left(40)

# for _ in range(10):
#     timmy.pencolor('pink')
#     timmy.forward(100)
#     timmy.left(36)
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# timmy.speed(1)
def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for _ in range(number_of_sides):
        timmy.forward(100)
        timmy.right(angle)

for no_of_sides in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(no_of_sides)






screen = Screen()
screen.exitonclick()