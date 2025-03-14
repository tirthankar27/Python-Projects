from turtle import Turtle,Screen

from sympy.core.logic import fuzzy_bool

jimmy=Turtle()
my_screen=Screen()

def move_forward():
    jimmy.forward(10)
def move_backward():
    jimmy.back(10)
def turn_left():
    jimmy.left(4)
def turn_right():
    jimmy.right(4)

my_screen.listen()
my_screen.onkey(key='w',fun=move_forward)
my_screen.onkey(key='s',fun=move_backward)
my_screen.onkey(key='a',fun=turn_left)
my_screen.onkey(key='d',fun=turn_right)
my_screen.exitonclick()
