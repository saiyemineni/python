import tkinter

window = tkinter.Tk()
window.title("Miles to KM Converter")
window.minsize(width= 100, height= 100)
window.config(padx= 20, pady= 20)

def convert_miles_to_Km():
    miles = int(input_text.get())
    km = miles * 1.609
    converted_km.config(text=f"{round(km, 2)}")

input_text = tkinter.Entry(width= 10)
input_text.grid(column=2, row= 0)

label_miles = tkinter.Label(text="Miles")
label_miles.config(padx=10, pady=10)
label_miles.grid(column=3, row= 0)

label_equal = tkinter.Label(text="equals to ")
label_equal.config(padx=10, pady=10)
label_equal.grid(column=1, row= 1)

converted_km = tkinter.Label()
converted_km.config(padx=10, pady=10)
converted_km.grid(column=2, row= 1)

label_km = tkinter.Label(text="KM")
label_km.config(padx=10, pady=10)
label_km.grid(column=3, row= 1)

calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_Km)
calculate_button.grid(column= 2, row= 2)








window.mainloop()