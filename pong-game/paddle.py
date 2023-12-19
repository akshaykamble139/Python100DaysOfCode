from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.left(90)
        self.shapesize(1.0, 5.0)
        self.penup()
        self.goto(position)
        self.color("white")
        self.speed(0)


    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
