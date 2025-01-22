from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
STARTING_MOVE_DISTANCE = 10

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        """Create a new car"""
        car = Turtle()
        car.shape("square")
        car.color(choice(COLORS))
        car.turtlesize(stretch_len=2, stretch_wid=1)
        car.setheading(180)
        car.penup()
        car.goto(x=320, y=randint(-240, 240))

        self.all_cars.append(car)

    @staticmethod
    def move_left(car):
        """Move's the car to left."""
        car.forward(STARTING_MOVE_DISTANCE)