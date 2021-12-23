programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    }


# print(programming_dictionary['Bug'])
# To add a new item to the dictionary
programming_dictionary["Loop"] = "The action of doing things over and over"

for key in programming_dictionary:
    print(key, programming_dictionary[key])