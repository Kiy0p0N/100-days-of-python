from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=800, height=400)  # Creates a canvas that is 800 pixels wide and 400 pixels tall

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
competing_turtles = {}  # Dictionary to store objects created by the Turtle class
y_position = -100

def move_forward():
    """Returns a random value, from 1 to 10"""
    return randint(1, 10)

for color in rainbow_colors:  # For loop for creating turtle objects according to the number of colors in "rainbow_colors" list
    turtle = Turtle(shape="turtle")
    turtle.color(color)  # Sets the color of the turtle according to the color of the current loop loop
    competing_turtles[color] = turtle  # Creates a key with the name of the current color and adds the created turtle as a value

    current_turtle = competing_turtles[color]
    current_turtle.penup()
    current_turtle.goto(x=-380, y=y_position)  # Move the turtle to the starting position
    y_position += 40  # Add 40 more to "y_position" so that the turtles are not on top of each other

user_bet = screen.textinput(title="Bet on the winner", prompt="Which turtle will win the race? Red, orange, yellow, green, blue or purple?")
winner = False
turtle_winner = None

while not winner:
    for turtle in competing_turtles:
        competing_turtles[turtle].forward(move_forward())

        if competing_turtles[turtle].xcor() >= 370:  # If a turtle reaches coordinate x => 370, it wins and the game ends
            turtle_winner = turtle
            winner = True
            break

if turtle_winner == user_bet:
    print(f"You've won! The {turtle_winner} turtle is the winner!")
else:
    print(f"You've lost! The {turtle_winner} turtle is the winner!")

screen.exitonclick()