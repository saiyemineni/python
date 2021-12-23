def greet():
    print("Hello sai")
    print("How do you do?")
    print("Isn't the weather nice today ?")

# greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today ?")

# greet_with_name("sai")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location} ?")

greet_with("sai", "Hyderabad")
greet_with("Hyderabad", "Sai")
greet_with(location="Hyderabad", name= "Sai")

