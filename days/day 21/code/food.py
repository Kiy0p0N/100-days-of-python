from turtle import  Turtle
from random import  randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh_pos()

    def refresh_pos(self):
        """Send the food to a new random location"""
        random_x = randint(-280, 280)
        random_y = randint(-280, 270)
        self.goto(x=random_x, y=random_y)
