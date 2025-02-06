from turtle import Screen
from state import State
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.title('Brazil States Game')
screen.setup(width=800, height=800)
image = './image/mapa-brasil.gif'  # Path to the image file
screen.bgpic(image)

scoreboard = Scoreboard()

game_over = False
while not game_over:
    sleep(1)
    answer_state = screen.textinput(title=f"{scoreboard.correct_answer}/27", prompt="What's another state's name?")

    if answer_state == "EXIT":
        game_over = True

    if State.check_state(answer_state):
        state = State(answer_state)
        scoreboard.state_in_list(answer_state)
        game_over = scoreboard.victory()

screen.exitonclick()