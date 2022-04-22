from tkinter import *

def miles_km_conversion():
    conversion = round(float(input.get()) * 1.609344)
    result.config(text=conversion)

window = Tk()
window.minsize(width=300, height=100)
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

# Labels
miles = Label(text="Miles")
miles.grid(column=4, row=2)

km = Label(text="Km")
km.grid(column=4, row=3)

equal = Label(text="is equal to")
equal.grid(column=2, row=3)

result = Label(text="0")
result.grid(column=3, row=3)

# Button
calculate = Button(text="Calculate", command=miles_km_conversion)
calculate.grid(column=3, row=4)

# Entry
input = Entry()
input.grid(column=3, row=2)

window.mainloop()