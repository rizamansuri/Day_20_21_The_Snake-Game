# BismillahirRahmanirRahim
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(".....Riza's Snake Game.....")
screen.tracer(0)  # Turning off the animation

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True
while is_game_on:  # To make the snake move automatically
    screen.update()  # After the 3 blocks are created then only the screen will be updated
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_tail()
        score.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()
    # Detect collision with tail
    for segment in snake.snake_size[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
