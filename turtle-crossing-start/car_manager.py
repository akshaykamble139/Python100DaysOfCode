from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.add_new_cars()

    def add_new_cars(self):
        for pos in range(-240, 260, 10):
            val = random.random()
            if val > 0.97:
                car = Turtle()
                car.shape("square")
                car.penup()
                car.shapesize(1.0, 2.0)
                car.goto(280, pos)
                car.color(random.choice(COLORS))
                self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.backward(self.cars_speed)
            if car.xcor() < -320:
                self.car_list.remove(car)

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT

    def speed_reset(self):
        self.cars_speed = STARTING_MOVE_DISTANCE


