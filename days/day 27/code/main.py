# Mile to Km converted
from tkinter import *

window = Tk()
window.title("Mile to Km")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())  # Takes the string entered in the input and turns it into a float
    km = miles * 1.609
    result.config(text=f'{km:.3f}')  # Change the text of the 'result' label to the conversion result


PADDING_X = 10
PADDING_Y = 5

# Label
equal = Label(text="is equal to")
equal.grid(column=0, row=1)
equal.config(padx=PADDING_X, pady=PADDING_Y)

result = Label(text="0")
result.grid(column=1, row=1)
result.config(padx=PADDING_X, pady=PADDING_Y)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=PADDING_X, pady=PADDING_Y)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=PADDING_X, pady=PADDING_Y)

# Input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)
button.config(padx=PADDING_X, pady=PADDING_Y)



window.mainloop()