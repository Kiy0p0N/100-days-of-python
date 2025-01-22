from turtle import Turtle

FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.att_level()

    def att_level(self):
        """Update the level."""
        self.clear()
        self.goto(x=-260, y=260)
        self.level += 1
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        """Display the game over message."""
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER!", align="center", font=FONT)