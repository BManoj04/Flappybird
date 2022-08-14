from turtle import Screen
from bird import Bird
from time import sleep
from wall import Wall
from score import Score

screen = Screen()
screen.addshape("bird3.gif")
screen.title("FLAPPY BIRD")
screen.tracer(0)
bird = Bird()
wall = Wall()
score = Score()

wall.hideturtle()
screen.bgpic("flappybirdbg.png")
screen.setup(800, 600)
screen.bgcolor("black")
screen.listen()
screen.onkey(bird.move, "Up")

game = True
while game:
    sleep(0.1)
    wall.create_wall()
    bird.fall()
    screen.update()
    wall.wall_move()
    score.show()

    for f in wall.wall1l:
        for se in wall.wall2l:
            if f.distance(bird) + se.distance(bird) == 580:
                score.increase()
            if f.distance(bird) + se.distance(bird) == 580 and (f.distance(bird) < 249 or se.distance(bird)) < 249:
                game = False
                score.game_ends()
    if bird.ycor() > 300 or bird.ycor() < -300:
        game = False
screen.exitonclick()
