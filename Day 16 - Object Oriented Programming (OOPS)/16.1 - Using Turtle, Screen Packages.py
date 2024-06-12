# https://docs.python.org/3/library/turtle.html
# Constructing Objects and Accessing their Attributes and Methods

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
