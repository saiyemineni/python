import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()
timmy.speed('fastest')
screen.bgcolor('black')
timmy.color('white')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for i in range(2, 361, 2):

    timmy.circle(100)
    timmy.setheading(i)

for i in range(2, 361, 2):

    timmy.circle(50)
    timmy.setheading(i)

for i in range(2, 361, 2):

    timmy.circle(150)
    timmy.setheading(i)

for i in range(2, 361, 2):
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90) 
    timmy.setheading(i)

for i in range(2, 361, 2):
    for _ in range(4):
        timmy.forward(400)
        timmy.left(90) 
    timmy.setheading(i)

timmy.color('black')

for i in range(2, 361, 2):
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90) 
    timmy.setheading(i)






screen.exitonclick()