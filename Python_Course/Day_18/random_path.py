import turtle as t
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]
timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


timmy.speed('fastest')
timmy.pensize(15)

for _ in range(1000):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))


screen.exitonclick()