try:
    file = open("a_file.txt")
    my_dict = {"key": "value"}
    print(my_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt", mode='a')
    file.write("something!")
except KeyError as error_message:
    print(f"that key {error_message} doesn't exists")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

