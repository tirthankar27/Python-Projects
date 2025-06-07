from turtle import Turtle
import pandas as pd
from patsy.state import center


class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_turtle(self,filtered_data):
        self.goto(filtered_data.iloc[0]['x'], filtered_data.iloc[0]['y'])
        self.write(filtered_data.iloc[0]['state'])
    def print_msg(self,msg):
        self.goto(-20,0)
        self.write(msg,align='center',font=('Arial',24,'normal'))