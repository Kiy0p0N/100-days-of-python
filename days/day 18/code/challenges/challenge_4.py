# Generate a Random Walk
import turtle as t
from random import randint, choice

turtle = t.Turtle()
t.colormode(255)
screen = t.Screen()

turtle.pensize(10)
turtle.speed("fast")

def random_color():
    """Creates a random RGB color"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color

angles = [0, 90, 180, 270]  # Set the orientation of the turtle. 0 = north, 90 = east, 180 = south, 270 = west

for _ in range(100):
    turtle.color(random_color())
    turtle.setheading(choice(angles))
    turtle.forward(30)

screen.exitonclick()