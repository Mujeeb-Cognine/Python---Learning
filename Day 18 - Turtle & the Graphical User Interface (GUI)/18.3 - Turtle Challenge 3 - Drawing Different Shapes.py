import random
from turtle import Turtle

tim = Turtle()

colors = ["burlywood", "green", "navy", "dark goldenrod", "slate blue", "crimson", "medium spring green", "deep pink",
          "cornflower blue", "dark magenta", "powder blue"]


def draw_shape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choices(colors))
    draw_shape(shape_side_n)
