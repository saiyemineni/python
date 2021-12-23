import random
import my_module
random_integer = random.randint(1,10)
print(random_integer)
print(my_module.pi)

random_float = random.random()
random_float = random_float * 5
print(random_float)

love_score = random.randint(1,100)
print(f"your love score is {love_score}")

#dice
dice = random.randint(1,6)
print(f"The number on the dice is {dice}")