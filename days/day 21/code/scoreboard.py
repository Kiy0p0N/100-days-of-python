from turtle import Turtle

ALIGN = "center"
FONT_STYLE = ("Courier", 20, "normal")

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file='data.txt') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.refresh_score()

    def refresh_score(self):
        """Update the score"""
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", move=False, align=ALIGN, font=FONT_STYLE)

    def reset(self):
        """Updates the player's high score"""
        if self.high_score < self.score:
            self.high_score = self.score
            with open(file='data.txt', mode='w') as data:
                data.write(str(self.high_score))

        self.score = 0
        self.refresh_score()
