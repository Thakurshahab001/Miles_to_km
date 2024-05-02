from tkinter import *

# Create the main window
windows = Tk()
windows.title("Miles To Km Conversion")
windows.config(padx=20, pady=20)

def conversion():
    miles = float(miles_input.get())
    kilometers = round(miles * 1.609344)
    kilometere_result_label.config(text=f"{kilometers}")

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometere_result_label = Label(text=0)
kilometere_result_label.grid(column=1, row=1)

kilometere_label = Label(text="Km")
kilometere_label.grid(column=2, row=1)

button = Button(text="Calculate", command=conversion)
button.grid(column=1, row=2)

windows.mainloop()
