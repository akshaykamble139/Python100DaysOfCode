import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

tim = Player()
score = Scoreboard()
cars = CarManager()

screen.onkeypress(tim.move_up,"Up")
screen.onkeypress(score.game_reset,"space")

game_is_on = True
count = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if not score.can_game_be_restarted:
        if tim.turtle_is_stopped:
            tim.turtle_restarted()
        cars.move()
        if count % 6 == 0:
            cars.add_new_cars()

    count += 1

    for car in cars.car_list:
        if tim.distance(car) < 20:
            score.game_over()
            tim.game_over()

    if tim.ycor() > 280:
        tim.position_reset()
        score.level_up()
        cars.increase_speed()

