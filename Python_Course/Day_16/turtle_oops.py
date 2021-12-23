# from turtle import Turtle,Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('coral')
# timmy.forward(100)
# timmy.left(45)
# timmy.forward(100)
# timmy.right(45)
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Names', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Pokemon Type', ['Electric', 'Water', 'Fire'])
print(table.align)
table.align = 'l'
print(table.align)
print(table)
