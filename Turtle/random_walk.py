import turtle
import random
jimmy=turtle.Turtle()
turtle.colormode(255)
def change_direction():
    directions=[0,90,180,270]
    jimmy.setheading(random.choice(directions))

def change_color():
    jimmy.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
jimmy.speed(7)
jimmy.pensize(5)
for i in range(200):
    change_color()
    jimmy.forward(20)
    change_direction()
my_screen=turtle.Screen()
my_screen.exitonclick()
