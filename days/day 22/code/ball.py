from turtle import Turtle
from random import choice

Y_DIRECTIONS = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = choice(Y_DIRECTIONS)
        self.move_speed = 0.1

    def move(self):
        """Moves the ball to the new coordinate."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """Reverses the horizontal side the ball was heading towards."""
        self.x_move *= -1
        self.move_speed *= 0.5

    def bounce_y(self):
        """Reverses the vertical direction the ball was heading towards."""
        self.y_move *= -1

    def reset_position(self):
        """Moves the ball to its starting position, with and resets its attributes to their initial values."""
        self.teleport(0, 0)
        self.y_move = choice(Y_DIRECTIONS)
        self.move_speed = 0.1
        self.bounce_x()