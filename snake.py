from turtle import Turtle
from food import Food

INITIAL_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Food):
    def __init__(self):  # Create basic 3 blocked snake
        self.snake_size = []
        self.create_snake()
        self.head = self.snake_size[0]

    def create_snake(self):
        for snake in INITIAL_POS:
            self.add_segment(snake)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_size.append(segment)

    def reset_snake(self):
        for old_snake_box in self.snake_size:
            old_snake_box.goto(1000, 1000)
        self.snake_size.clear()
        self.create_snake()
        self.head = self.snake_size[0]

    def extend_tail(self):
        self.add_segment(self.snake_size[-1].position())

    def move(self):  # Make the snake move forward
        for seg_num in range(len(self.snake_size) - 1, 0, -1):
            prev_xcor = self.snake_size[seg_num - 1].xcor()
            prev_ycor = self.snake_size[seg_num - 1].ycor()
            # Making the last snake box to goto the position of second last snake box
            self.snake_size[seg_num].goto(prev_xcor, prev_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # north

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  # south

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)  # west

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)  # east
