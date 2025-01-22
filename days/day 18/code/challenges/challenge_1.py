# Draw a square
import turtle as t

turtle = t.Turtle()
screen = t.Screen()

for _ in range(4):
    turtle.forward(100)  # Move the turtle forward by the specified distance
    turtle.right(90)  # Turn turtle right by angle units


screen.exitonclick()