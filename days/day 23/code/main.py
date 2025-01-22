import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def game():
    instructions.clear()  # Delete the instructions

    # Create a player
    player = Player()
    # Create a car manager
    car_manager = CarManager()
    # Create a scoreboard
    scoreboard = Scoreboard()

    screen.onkey(fun=player.move_up, key="Up")

    speed = 0.3  # Sets how fast the cars are, the lower the value, the higher the speed
    c_car = 0  # Variable for car creation control
    game_over = False
    while not game_over:
        time.sleep(speed)  # Control the speed
        screen.update()

        # Creates a car after four loop iterations
        if c_car == 4:
            car_manager.create_car()
            c_car = 0  # Returns to zero to create a new car only after 4 more laps

        # Get each car in the car list
        for car in car_manager.all_cars:
            car_manager.move_left(car)

            # If the distance between the player and the car are less than 25, it is game over
            if int(player.distance(car)) < 25:
                scoreboard.game_over()
                game_over = True

            # If the car's x-coordinate is less than -320, it is already off-screen
            if car.xcor() <= -320:
                car_manager.all_cars.remove(car)  # It is removed from the car list so it no longer needs to be moved with each loop iteration

        # If the player reaches the finish line (ycor: 280)
        if player.check_finish_line():
            scoreboard.att_level()  # Update current level
            player.return_pos()  # Return to the starting position
            speed *= 0.9  # Increase speed

        c_car += 1

# Create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

# Initial instructions
instructions = Turtle()
instructions.hideturtle()
instructions.penup()
instructions.write(arg="""
Welcome to the Turtle Crossing game!
Just use the 'Up' key to control the turtle.
Press 'space' to start.
""", align="center", font=("Courier", 15, "bold"))

# Listen for click events
screen.listen()
screen.onkey(fun=game, key="space")  # Start the game

screen.exitonclick()