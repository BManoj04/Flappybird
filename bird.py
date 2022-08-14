from turtle import Turtle
FALL_DISTANCE = 8
MOVE = 30
POSITION = (-100, 0)


class Bird(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("bird3.gif")
        self.color("yellow")
        self.penup()
        self.shapesize(20, 20)
        self.goto(POSITION)

    def fall(self):
        ycor = self.ycor() - FALL_DISTANCE
        self.goto(-100, ycor)

    def move(self):
        ycor = self.ycor() + MOVE
        self.goto(-100, ycor)

    def det_col(self):
        if self.ycor() > 300 or self.ycor() < -300:
            return False
