from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.turtle_is_stopped = False
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        if not self.turtle_is_stopped:
            self.forward(MOVE_DISTANCE)

    def position_reset(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.turtle_is_stopped = True
        self.position_reset()

    def turtle_restarted(self):
        self.turtle_is_stopped = False

