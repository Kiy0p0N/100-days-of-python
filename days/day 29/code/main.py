# Importing necessary modules
from tkinter import *
from tkinter import messagebox
from random import choices

def validation():
    """Validate input fields and display an error if any are empty; otherwise, save the information"""
    if website_entry.get() == '' or user_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror(title="Insufficient information", message="Please add all necessary information before saving.")
    else:
        save_information()  # Save the data if all fields are filled
        messagebox.showinfo(title="Success", message="Data saving was successful.")

def save_information():
    """
    Saves the website, username, and password information into a text file.
    The information is appended to the file without overwriting existing data.
    """
    # Formatting user information as a string for easy readability in the file
    user_information = f"""
    website: {website_entry.get()}
    user: {user_entry.get()}
    password: {password_entry.get()}
    \n
    """

    # Append the user information to 'information.txt'
    with open('information.txt', mode='a') as information:
        information.write(user_information)  # Write the formatted user information to the file

    # Clear all input fields after saving
    website_entry.delete(0, END)
    user_entry.delete(0, END)
    password_entry.delete(0, END)

def generate_password():
    """
    Generates a random password using uppercase letters, lowercase letters, digits, and symbols.
    The password will be 16 characters long.
    """
    # Dictionary of characters used for password generation
    password_chars = {
        "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",  # Uppercase letters
        "lowercase": "abcdefghijklmnopqrstuvwxyz",  # Lowercase letters
        "digits": "0123456789",  # Numbers
        "symbols": "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"  # Special characters
    }

    # Combine all the character sets into a single string
    all_password_chars = (
        password_chars["uppercase"] +
        password_chars["lowercase"] +
        password_chars["digits"] +
        password_chars["symbols"]
    )

    # Generate a random 16-character password
    password = ''.join(choices(all_password_chars, k=16))

    # Insert the generated password into the password entry field
    password_entry.insert(0, password)

# Creating the main application window
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

# Creating a canvas to display an image (padlock logo in this case)
canvas = Canvas(width=200, height=200, highlightthickness=0)
padlock_img = PhotoImage(file="image/logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# Creating and placing the "Website" label and entry field
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=50)
website_entry.grid(column=1, columnspan=2, row=1)

# Creating and placing the "Email/Username" label and entry field
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
user_entry = Entry(width=50)
user_entry.grid(column=1, columnspan=2, row=2)

# Creating and placing the "Password" label, entry field, and "Generate Password" button
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)
password_btn = Button(text="Generate Password", command=generate_password)  # Button to generate a random password
password_btn.grid(column=2, row=3)

# Creating and placing the "Add" button to save credentials
add_btn = Button(text="Add", width=43, command=validation)
add_btn.grid(column=1, columnspan=2, row=4)

# Running the Tkinter event loop to keep the window open
window.mainloop()