from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def counter_clock():
    tim.circle(10)


def clock_wise():
    tim.circle(-10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
