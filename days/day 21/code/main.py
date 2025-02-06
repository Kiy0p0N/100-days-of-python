from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen for the Snake game
screen = Screen()
screen.setup(width=600, height=600)  # Set screen dimensions to 600x600
screen.bgcolor("black")  # Set background color to black
screen.title("My Snake Game")  # Set window title
screen.tracer(0)  # Turn off automatic screen updates for smoother animations

snake = Snake()  # Create the snake object
food = Food()  # Create the food object
scoreboard = Scoreboard()  # Create the score object

# Set up key listeners for controlling the snake
screen.listen()  # Allow the screen to detect key presses
screen.onkey(snake.up, "Up")  # Move snake up when the "Up" arrow key is pressed
screen.onkey(snake.down, "Down")  # Move snake down when the "Down" arrow key is pressed
screen.onkey(snake.left, "Left")  # Move snake left when the "Left" arrow key is pressed
screen.onkey(snake.right, "Right")  # Move snake right when the "Right" arrow key is pressed

# Main game loop
game_over = False  # Initialize game_over flag
while not game_over:
    screen.update()  # Refresh the screen for smooth animation
    time.sleep(0.1)  # Pause briefly to control the game speed

    snake.move()  # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_pos()
        scoreboard.score += 1
        snake.new_segment()
        scoreboard.refresh_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with snake body
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Close the game window when the user clicks
screen.exitonclick()