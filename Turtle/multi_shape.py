from turtle import Turtle,Screen
import random
jimmy=Turtle()

def change_color():
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
    random.shuffle(colors)
    jimmy.color(random.choice(colors))

for i in range(0,8):
    angle=180-((i+3-2)*180)/(i+3)
    change_color()
    for j in range(i+3):
        jimmy.forward(100)
        jimmy.right(angle)
my_screen=Screen()
my_screen.exitonclick()
