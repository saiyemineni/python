import tkinter
from tkinter.constants import END

window = tkinter.Tk()
window.title("my GUI")
window.minsize(width= 500, height= 300)

#label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24,"bold"))
my_label.place(x= 0, y= 0)

my_label['text'] = "New Label"
my_label.config(text="New Label")

#Button
def button_clicked():
    print("I go clicked")
    print(type(input_text.get()))
    my_label.config(text=input_text.get())



my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.pack()

# Entry
input_text = tkinter.Entry(width=30)
input_text.pack()

#test entry box
test_box = tkinter.Text(width= 30, height= 5)
test_box.focus()
test_box.insert(END, "Hello World!")
print(test_box.get("1.0", END))
test_box.pack()

#Spinbox
def spinebox_used():
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_= 0, to= 10, width= 5,command=spinebox_used)
spinbox.pack()

#scale 
def scale_value(num):
    print(scale.get())
scale = tkinter.Scale(from_= 0, to= 100, command=scale_value)
scale.pack()

# CheckButton
def checkbutton_used():
    print(checkstate.get())
checkstate = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="is On?", variable=checkstate, command=checkbutton_used)
# checkstate.get()
checkbutton.pack()

#Radio button
def radio_used():
    print(radio_state.get())
radio_state = tkinter.IntVar()
radio_button1 = tkinter.Radiobutton(text="Option 1", value= 1, variable=radio_state, command= radio_used)
radio_button2 = tkinter.Radiobutton(text="Option 2", value= 2, variable=radio_state, command= radio_used)
radio_button1.pack()
radio_button2.pack()

# list box
def listbox_used(event):
    print(list_box.get(list_box.curselection()))

list_box = tkinter.Listbox(height= 4)
fruits = ["orange", "Apple", "grapes", "pears"]
for item in fruits:
    list_box.insert(fruits.index(item), item)
list_box.bind("<<ListboxSelect>>", listbox_used)
list_box.pack()







window.mainloop()