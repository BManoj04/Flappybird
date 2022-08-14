from turtle import Turtle
SCORE = 0
POSITION = (-370, 250)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score") as score:
            self.high_score = int(score.read())
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(POSITION)

    def increase(self):
        global SCORE
        SCORE += 1
        if SCORE > self.high_score:
            self.high_score = SCORE
        with open("high_score", "w") as scr:
            scr.write(f"{self.high_score}")

    def show(self):
        self.clear()
        self.write(f"Score = {SCORE} High score = {self.high_score}", align="left", font=("Courier", 20, "normal"))

    def game_ends(self):
        self.high_score = int(self.high_score) - 1
        with open("high_score", "w") as scr:
            scr.write(f"{self.high_score}")
