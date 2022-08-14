from turtle import Turtle
import random
wall_frequency = 0


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.wall1l = []
        self.wall2l = []

    def create_wall(self):

        global wall_frequency
        wall_frequency += 1
        if wall_frequency == 50:
            wall_frequency = 0
            wall1 = Turtle("square")
            wall2 = Turtle("square")
            wall1.color("#009933")
            wall2.color("#009933")
            wall1.penup()
            wall2.penup()
            wall1.shapesize(stretch_wid=24, stretch_len=1)
            wall2.shapesize(stretch_wid=24, stretch_len=1)
            self.wall1l.append(wall1)
            self.wall2l.append(wall2)
            r = random.randint(60, 520)

            wall1.goto(380, r)
            wall2.goto(380, r - 580)

    def wall_move(self):

        for wa in self.wall1l:
            wa.backward(10)

        for wa in self.wall2l:
            wa.backward(10)
