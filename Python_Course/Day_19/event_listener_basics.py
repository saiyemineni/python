import turtle as t

timmy = t.Turtle()

timmy_1 = t.Turtle()
screen = t.Screen()

def move_forward():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')



screen.exitonclick()