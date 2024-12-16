# Drawing Different Shapes
import turtle as t
from random import choice
from colors import colors

turtle = t.Turtle()
screen = t.Screen()

def shape_draw(shape):
    """Divide the value of one complete turn, 360°, by the number of sides to obtain the internal angle of the shape to create the corresponding shape"""
    angle = 360 / shape
    for _ in range(shape):
        turtle.forward(100)
        turtle.right(angle)

for i in range(3, 11):
    turtle.color(choice(colors))  # Each loop chooses a random color
    shape_draw(i)


screen.exitonclick()