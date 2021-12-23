import random

names = input("Give me everybody's names, separated by a comma. ")
names = names.split(",")
no_of_people = len(names)
#random_member = random.choice(names)
random_member = random.randint(0,no_of_people-1)
print(f"{names[random_member]} is going to buy us the meal..")
