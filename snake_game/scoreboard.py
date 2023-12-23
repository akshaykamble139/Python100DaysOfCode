from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 20, 'normal')
GAME_OVER = "GAME OVER"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        with open("data.txt") as file:
            highscore = file.read()
            self.high_score = int(highscore)
        # self.high_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGN, FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(GAME_OVER, False, ALIGN, FONT)
