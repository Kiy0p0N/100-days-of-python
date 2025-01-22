from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Move the player to up."""
        self.forward(MOVE_DISTANCE)

    def check_finish_line(self):
        """Checks if the player has reached the finish line."""
        return self.ycor() >= FINISH_LINE_Y

    def return_pos(self):
        """Returns to starting position."""
        self.goto(STARTING_POSITION)