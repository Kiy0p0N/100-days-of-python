from turtle import Turtle

ALIGN = "center"
FONT_STYLE = ("Courier", 20, "normal")

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg="Score: 0", move=False, align=ALIGN, font=FONT_STYLE)

    def refresh_score(self):
        """Update the score"""
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT_STYLE)

    def game_over(self):
        """Displays 'game over' message"""
        self.goto(0, 0)
        self.write(arg="GAME OVER!", move=False, align=ALIGN, font=FONT_STYLE)