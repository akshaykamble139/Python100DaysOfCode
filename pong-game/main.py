from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_paddle = Paddle((350,0))
computer_paddle = Paddle((-350,0))
scoreboard = Scoreboard()

ball = Ball()
screen.listen()

screen.onkeypress(player_paddle.up,"Up")
screen.onkeypress(player_paddle.down,"Down")

screen.onkeypress(computer_paddle.up,"w")
screen.onkeypress(computer_paddle.down,"s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ((ball.distance(player_paddle) < 50 and ball.xcor() > 335) or
            (ball.distance(computer_paddle) < 50 and ball.xcor() < -335)):
        ball.bounce_x()

    # Ball missed the right paddle
    if ball.distance(player_paddle) > 50 and ball.xcor() >= 380:
        ball.game_reset()
        scoreboard.l_point()

    # Ball missed the left paddle
    if ball.distance(computer_paddle) > 50 and ball.xcor() < -380:
        ball.game_reset()
        scoreboard.r_point()

screen.exitonclick()
