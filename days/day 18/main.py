# The Hirst Painting Project
import turtle as t
from random import randint

turtle = t.Turtle()
t.colormode(255)
screen = t.Screen()

turtle.hideturtle()
turtle.penup()

turtle.setheading(235)
turtle.forward(250)
current_position = turtle.position()

def random_color():
    """Creates a random RGB color"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color

for y in range(10):
    for x in range(10):
        turtle.dot(20, random_color())
        turtle.teleport(turtle.position()[0] + 40)  # Makes the turtle teleport to the next point on the x-axis

    turtle.teleport(current_position[0], turtle.position()[1] + 40)  # Makes the turtle teleport to the next point on the y-axis



screen.exitonclick()