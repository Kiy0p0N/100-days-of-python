import math
from tkinter import *

# Constants for colors, font, and time durations
PINK = "#e2979c"
RED = "#e7305b"
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_NAME = 'Courier'
WORK_MIN = 25  # Work session duration in minutes
SHORT_BREAK_MIN = 5  # Short break duration in minutes
LONG_BREAK_MIN = 20  # Long break duration in minutes
reps = 0  # Keeps track of the number of work/break sessions
timer = None  # Variable to store the timer reference


def reset_timer():
    """Stops the timer, resets the UI, and clears the checkmarks."""
    window.after_cancel(timer)  # Cancels the running timer
    title.config(text="Timer", fg=GREEN)  # Resets the title text and color
    check.config(text='')  # Clears checkmarks
    canvas.itemconfig(timer_text, text="00:00")  # Resets the timer display
    global reps
    reps = 0  # Resets session count


def start_count():
    """Starts a new Pomodoro cycle, alternating between work and breaks."""
    global reps
    reps += 1  # Increments the session count

    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine session type: work, short break, or long break
    if reps % 8 == 0:  # Every 8th session is a long break
        count_down(long_break_sec)
        title.config(text='Break', fg=RED)
    elif reps % 2 == 0:  # Every 2nd session is a short break
        count_down(short_break_sec)
        title.config(text='Break', fg=PINK)
    else:  # Otherwise, it's a work session
        count_down(work_sec)
        title.config(text='Work', fg=GREEN)


def count_down(count):
    """Counts down the given time in seconds and updates the UI."""
    count_min = math.floor(count / 60)  # Get minutes
    count_sec = count % 60  # Get remaining seconds

    # Format time to always display two digits
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Update timer display
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Call count_down every second
    else:
        start_count()  # Start the next session automatically

        # Display checkmarks for completed work sessions
        marks = ''
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += '✔'
        check.config(text=marks)


# UI Setup
window = Tk()
window.title("Pomodoro")  # Window title
window.config(padx=100, pady=100, background=YELLOW)  # Set window padding and background color

# Timer Label
title = Label(text="Timer")
title.config(font=(FONT_NAME, 40, 'bold'), fg=GREEN, background=YELLOW)
title.grid(column=1, row=0)

# Canvas for displaying the timer and image
canvas = Canvas(width=320, height=320, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='image/tomato.png')  # Load image
canvas.create_image(160, 160, image=tomato_img)  # Display image in the center
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(160, 170, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Label for checkmarks
check = Label()
check.config(font=(FONT_NAME, 15, 'bold'), fg=GREEN, background=YELLOW)
check.grid(column=1, row=3)

# Start button
start_button = Button(text="Start", command=start_count)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Run the Tkinter event loop
window.mainloop()