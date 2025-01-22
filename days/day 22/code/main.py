from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def game():
    instructions.clear()  # Delete game instructions

    # Create the players
    player_1 = Paddle(x_pos=-350)
    player_2 = Paddle(x_pos=350)

    # Create the ball
    ball = Ball()

    # Create the scoreboard
    scoreboard = Scoreboard()

    # Player 1 moves
    screen.onkey(fun=player_1.move_up, key="w")
    screen.onkey(fun=player_1.move_down, key="s")
    # Player 2 moves
    screen.onkey(fun=player_2.move_up, key="Up")
    screen.onkey(fun=player_2.move_down, key="Down")

    screen.tracer(1)  # Set delay for update drawings

    # Main loop
    game_over = False
    while not game_over:
        time.sleep(ball.move_speed)  # Define the speed of ball
        screen.update()  # Refresh the screen for smooth animation
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if (ball.distance(player_1) < 60 and ball.xcor() < -330) or (
                ball.distance(player_2) < 60 and ball.xcor() > 330):
            ball.bounce_x()

        # Detect point
        if ball.xcor() > 400:
            scoreboard.player1_point()
            ball.reset_position()

        if ball.xcor() < -400:
            scoreboard.player2_point()
            ball.reset_position()

        # Detects if someone won
        if scoreboard.player1_score == 3 or scoreboard.player2_score == 3:
            ball.hideturtle()
            instructions.write(arg=f"{scoreboard.compare_score()} won🎉🎉", align="center", font=("arial", 30, "normal"))
            game_over = True

# Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)

# Instructions for the game
INSTRUCTIONS_DETAILS = """
In this game, the player who scores 3 points first wins.

Player 1 must use the 'w' and 's' keys, while player 2 must use the 'up' and 'down' keys.

With each hit of the ball on the paddles, the speed of the ball increases by two times.

Press 'space' to start the game.
"""

instructions = Turtle()
instructions.hideturtle()
instructions.color("white")
instructions.write(arg=INSTRUCTIONS_DETAILS, align="center", font=("arial", 10, "normal"))


# Set up key listeners for controlling the paddles
screen.listen()
screen.onkey(fun=game, key="space")  # Start the game

screen.exitonclick()