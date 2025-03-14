import turtle
import random

jimmy=turtle.Turtle()
my_screen=turtle.Screen()
turtle.colormode(255)
jimmy.speed(0)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    jimmy.pencolor((r, g, b))

jimmy.penup()
jimmy.back(50)
for i in range(10):
    for j in range(10):
        jimmy.pendown()
        change_color()
        jimmy.dot(10)
        jimmy.penup()
        jimmy.forward(20)
    jimmy.left(90)
    jimmy.forward(20)
    jimmy.right(90)
    jimmy.back(200)
my_screen.exitonclick()
