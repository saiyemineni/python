from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape('turtle')
timmy.color('coral')

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)


# for i in range(5):
#     timmy.forward(100)
#     for i in range(100):
#         timmy.forward(i)
#         timmy.left(60)

# for i in range(10):
#     timmy.forward(100)
#     timmy.right(45)
# timmy.circle(100)
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()
