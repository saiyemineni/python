###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

# import colorgram
# rgb_colors = []

# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)
timmy.speed('fastest')

color_list = color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

no_of_dots = 100
timmy.hideturtle()
timmy.setheading(225)
timmy.penup()
timmy.forward(300)
timmy.pendown()
timmy.setheading(0)

for j in range(1, no_of_dots+1):
    timmy.dot(15, random.choice(color_list))
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    if j % 10 == 0:
        timmy.setheading(90)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.setheading(180)
        timmy.penup()
        timmy.forward(500)
        timmy.pendown()
        timmy.setheading(0)



screen.exitonclick()




