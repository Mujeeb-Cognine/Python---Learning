import random
import turtle as t

tim = t.Turtle()
t.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(500):
    tim.color(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(directions))
