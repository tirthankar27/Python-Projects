from turtle import Turtle,Screen

jimmy=Turtle()
jimmy.shape("turtle")
jimmy.pendown()
for i in range(0,4):
    jimmy.forward(100)
    jimmy.left(90)
my_screen=Screen()
my_screen.exitonclick()
