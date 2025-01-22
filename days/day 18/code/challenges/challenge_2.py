# Draw a dashed line
import turtle as t

turtle = t.Turtle()
screen = t.Screen()

for _ in range(10):
    turtle.forward(10)  # Move the turtle forward by the specified distance
    turtle.penup()  # Pull the pen up – no drawing when moving
    turtle.forward(10)
    turtle.pendown()  # Pull the pen down – drawing when moving


screen.exitonclick()