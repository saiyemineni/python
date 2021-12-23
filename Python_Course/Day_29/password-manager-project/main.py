from datetime import date
import tkinter
from tkinter import Widget, messagebox
from tkinter.constants import END, W
import random
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_entry = website_input.get().lower()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No data file found")
    else:
        if website_entry in data:
            email = data[website_entry]["email"]
            password = data[website_entry]["password"]
            messagebox.showinfo(title=f"{website_entry}", message=f"email: {email} \n password: {password}")
        else:
            messagebox.showinfo(title="Error!",message=f"No details for {website_entry} exists.")
    

    
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range (nr_numbers)]

    password_list = password_letter + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_dict = {
        website:{
            "email": username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure that you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: \nEmail/Username: {username}\n Password: {password}", )
        if is_ok:
            try:
                with open("data.json",mode='r') as file:
                    # reading the data
                    # json.dump(new_dict, file, indent= 4)
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode='w') as file:
                    json.dump(new_dict)
            else:
                # update old data with new data
                data.update(new_dict)
                with open("data.json", mode='w') as file:
                    # saving updating data
                    json.dump(data, file, indent= 4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = tkinter.Canvas(height= 200, width= 200)
image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column= 1, row= 0)

website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row= 1)

website_input = tkinter.Entry(width= 33)
website_input.grid(row= 1, column=1,)
website_input.focus()

search_button = tkinter.Button(text="search", width= 15, command=find_password)
search_button.grid(row= 1, column= 2)
username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row= 2, column= 0)

username_input = tkinter.Entry(width= 52)
username_input.grid(row= 2, column=1, columnspan= 2)
username_input.insert(0, "saiyeminei31@gmail.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(column= 0, row= 3)

password_input = tkinter.Entry(width= 33)
password_input.grid(row= 3, column= 1)

generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add",width= 44, command= save_password)
add_button.grid( row=4, column=1,columnspan= 2)






window.mainloop()