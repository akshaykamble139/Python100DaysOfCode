from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.can_game_be_restarted = False
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto((-275, 265))
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def game_over(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
        self.can_game_be_restarted = True

    def game_reset(self):
        if self.can_game_be_restarted:
            self.level = 1
            self.goto((-275, 265))
            self.update()
            self.can_game_be_restarted = False

    def level_up(self):
        self.level += 1
        self.update()

