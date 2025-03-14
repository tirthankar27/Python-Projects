from turtle import Turtle,Screen
jimmy=Turtle()
jimmy.penup()
jimmy.back(100)
for i in range(10):
    jimmy.pendown()
    jimmy.forward(10)
    jimmy.penup()
    jimmy.forward(10)
my_screen=Screen()
my_screen.exitonclick()
