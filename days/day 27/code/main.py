# Importing everything from the Tkinter module (not recommended for larger projects)
from tkinter import *

# Creating the main application window
window = Tk()
window.title("Mile to Km")  # Setting the window title
window.config(padx=20, pady=20)  # Adding padding around the window for better layout

# Function to convert miles to kilometers
def miles_to_km():
    miles = float(miles_input.get())  # Get the input value and convert it to a float
    km = miles * 1.609  # Convert miles to kilometers using the conversion factor
    result.config(text=f'{km:.3f}')  # Update the result label with the formatted conversion result

# Constants for padding
PADDING_X = 10
PADDING_Y = 5

# Creating and positioning labels
equal = Label(text="is equal to")  # Label for the conversion statement
equal.grid(column=0, row=1)  # Placing it in the grid
equal.config(padx=PADDING_X, pady=PADDING_Y)  # Applying padding

result = Label(text="0")  # Label to display the conversion result
result.grid(column=1, row=1)  # Placing it in the grid
result.config(padx=PADDING_X, pady=PADDING_Y)  # Applying padding

miles_label = Label(text="Miles")  # Label for the miles input field
miles_label.grid(column=2, row=0)  # Placing it in the grid
miles_label.config(padx=PADDING_X, pady=PADDING_Y)  # Applying padding

km_label = Label(text="Km")  # Label for the kilometer result
km_label.grid(column=2, row=1)  # Placing it in the grid
km_label.config(padx=PADDING_X, pady=PADDING_Y)  # Applying padding

# Creating and positioning the input field
miles_input = Entry(width=10)  # Input field for entering miles
miles_input.grid(column=1, row=0)  # Placing it in the grid

# Creating and positioning the button
button = Button(text="Calculate", command=miles_to_km)  # Button to trigger conversion
button.grid(column=1, row=2)  # Placing it in the grid
button.config(padx=PADDING_X, pady=PADDING_Y)  # Applying padding

# Running the Tkinter event loop to keep the window open
window.mainloop()