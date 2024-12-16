# Draw a Spirograph
import turtle as t
from random import randint, choice

turtle = t.Turtle()
t.colormode(255)
screen = t.Screen()

turtle.pensize()
turtle.speed(50)

def random_color():
    """Creates a random RGB color"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color

for angle in range(0, 360, 4):
    turtle.color(random_color())
    turtle.setheading(angle)
    turtle.circle(100)

screen.exitonclick()