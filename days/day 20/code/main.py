from turtle import Screen
from snake import Snake
import time

# Set up the screen for the Snake game
screen = Screen()
screen.setup(width=600, height=600)  # Set screen dimensions to 600x600
screen.bgcolor("black")  # Set background color to black
screen.title("My Snake Game")  # Set window title
screen.tracer(0)  # Turn off automatic screen updates for smoother animations

# Create the snake object
snake = Snake()

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

# Close the game window when the user clicks
screen.exitonclick()
