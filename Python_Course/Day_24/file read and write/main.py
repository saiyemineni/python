# file = open('new_file.txt')
# contents = file.read()

# print(contents)

# file.close()

#Reading the file 

with open('my_file.txt') as file:
    contents = file.read()
    print(contents)


#Writing to the file
# 'w' means writable
# 'a' means append
with open('new_file.txt', mode='w') as file:
    file.write("new line")
