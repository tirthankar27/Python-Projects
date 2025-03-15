from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed(0)
        random_x=random.randint(-280,280)
        random_y=random.randint(-280, 280)
        self.goto(random_x,random_y)
    def update_position(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)