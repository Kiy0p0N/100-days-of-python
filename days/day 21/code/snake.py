from turtle import Turtle

# Constants for the starting position of the snake and direction values
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions for the snake's body segments
UP = 90     # Up direction in degrees
DOWN = 270  # Down direction in degrees
LEFT = 180  # Left direction in degrees
RIGHT = 0   # Right direction in degrees

class Snake:
    def __init__(self):
        self.segments = []  # List to hold all segments of the snake
        self.create_snake()  # Initialize the snake by creating its body
        self.head = self.segments[0]  # The first segment is the snake's head

    def create_snake(self):
        """Create the snake's body using the starting positions"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds the segment to the end of the list"""
        segment = Turtle("square")  # Create a square-shaped segment
        segment.color("white")  # Set the color of the segment to white
        segment.penup()  # Disable drawing when the segment moves
        segment.goto(position)  # Move the segment to its initial position
        self.segments.append(segment)  # Add the segment to the snake's body

    def new_segment(self):
        """Create a new segment"""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """Send the current snake off the screen, and create a new one in its starting position to restart the game."""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def move(self):
        """Move the snake wherever its head is pointing"""
        # Move each segment to the position of the previous segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(x=new_x, y=new_y)  # Move the current segment to the previous position
        self.head.forward(20)  # Move the head forward by 20 units

    def up(self):
        # Change the snake's direction to up if it's not currently moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the snake's direction to down if it's not currently moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change the snake's direction to left if it's not currently moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change the snake's direction to right if it's not currently moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
