from turtle import Screen
import time
from snake import *
from food import *
from scoreboard import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_is_on = True

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

print(f"score is {scoreboard.score}")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_the_snake()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Collision with the wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset()

    # Collision with the tail
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()

screen.exitonclick()
