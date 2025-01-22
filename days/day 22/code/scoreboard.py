from turtle import Turtle

ALIGN = "center"
FONT_STYLE = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.update_score()

    def update_score(self):
        """Updates the score at each point."""
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"PLAYER 1: {self.player1_score}", align=ALIGN, font=FONT_STYLE)
        self.goto(100, 200)
        self.write(arg=f"PLAYER 2: {self.player2_score}", align=ALIGN, font=FONT_STYLE)

    def player1_point(self):
        """Adds 1 point for player 1."""
        self.player1_score += 1
        self.update_score()

    def player2_point(self):
        """Adds 1 point for player 2."""
        self.player2_score += 1
        self.update_score()

    def compare_score(self):
        """Compare player scores."""
        if self.player1_score == 3:
            return "Player 1"
        else:
            return "Player 2"