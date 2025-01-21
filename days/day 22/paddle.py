from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x=x_pos, y=0)

    def move_up(self):
        """Move the paddle up."""
        self.forward(20)

    def move_down(self):
        """Move the paddle down."""
        self.forward(-20)