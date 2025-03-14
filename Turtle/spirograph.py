import turtle
import random

jimmy = turtle.Turtle()
jimmy.speed(0)
turtle.colormode(255)
def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    jimmy.pencolor((r, g, b))


for i in range(120):
    change_color()
    jimmy.circle(100)
    jimmy.left(3)
my_screen = turtle.Screen()
my_screen.exitonclick()
