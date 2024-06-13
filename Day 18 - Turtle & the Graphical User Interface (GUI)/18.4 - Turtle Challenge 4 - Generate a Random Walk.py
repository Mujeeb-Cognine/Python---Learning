import random
from turtle import Turtle

tim = Turtle()

colors = ["burlywood", "green", "navy", "dark goldenrod", "slate blue", "crimson", "medium spring green", "deep pink",
          "cornflower blue", "dark magenta", "powder blue"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
