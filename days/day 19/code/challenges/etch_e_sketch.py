from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.listen()

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def turn_right():
    turtle.right(10)

def turn_left():
    turtle.right(-10)

def clear_screen():
    screen.resetscreen()

screen.onkeypress(key="d", fun=move_forward)
screen.onkeypress(key="a", fun=move_backward)
screen.onkeypress(key="w", fun=turn_right)
screen.onkeypress(key="s", fun=turn_left)
screen.onkeypress(key="c", fun=clear_screen)

screen.exitonclick()