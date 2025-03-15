from tkinter import *
import pandas as pd
import random

# Background color for the application
BACKGROUND_COLOR = "#B1DDC6"

# Variables to store the current flashcard and the dataset
current_card = {}
data_dict = {}

# Attempt to load words that need to be learned
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # If the file doesn't exist, load the original dataset
    original_data = pd.read_csv("data/pt-br_en.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    # If the file exists, use its data
    data_dict = data.to_dict(orient="records")


def next_card():
    """Displays a new flashcard with an English word."""
    global current_card, flip_timer

    # Cancel the previous flip timer to prevent multiple flips
    window.after_cancel(flip_timer)

    # Select a random card from the dataset
    current_card = random.choice(data_dict)

    # Update the UI to display the English word
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)

    # Schedule the card flip after 5 seconds
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    """Flips the flashcard to reveal the Portuguese translation."""
    canvas.itemconfig(card_title, text="Portuguese", fill="white")
    canvas.itemconfig(card_word, text=current_card["Portuguese BR"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def is_know():
    """Removes the known word from the dataset and moves to the next card."""
    data_dict.remove(current_card)
    next_card()

    # Save the updated word list back to the CSV file
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)


# UI Setup
# Create the main application window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Timer to flip the card after 5 seconds
flip_timer = window.after(5000, func=flip_card)

# Create a canvas for displaying the flashcards
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="image/card_front.png")
card_back_img = PhotoImage(file="image/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)

# Add text elements to display the word and language title
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Create buttons for incorrect and correct answers
wrong_img = PhotoImage(file="image/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="image/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=is_know)
right_btn.grid(row=1, column=1)

# Display the first flashcard
next_card()

# Run the Tkinter event loop
window.mainloop()