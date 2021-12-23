import tkinter
from tkinter.constants import END

window = tkinter.Tk()
window.title("my GUI")
window.minsize(width= 500, height= 300)
window.config(padx= 20, pady= 20)

#label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24,"bold"))
my_label.grid(column= 0, row= 0)
my_label.config(padx= 20, pady= 20)

my_label['text'] = "New Label"
my_label.config(text="New Label")

#Button
def button_clicked():
    print("I go clicked")
    print(type(input_text.get()))
    my_label.config(text=input_text.get())

my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

my_button2 = tkinter.Button(text="Click Me", command=button_clicked)
my_button2.grid(column=2, row=0)


# Entry
input_text = tkinter.Entry(width=30)
input_text.grid(column=3, row=3)

window.mainloop()