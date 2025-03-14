from turtle import Turtle,Screen
import random

is_race_on=False
my_screen=Screen()
my_screen.setup(width=500,height=400)
colors=['red','blue','orange','green','purple']

user_bet = my_screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ").lower()
if user_bet:
    is_race_on=True

turtles=list()
for i in range(5):
    turtles.append(Turtle(shape='turtle'))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x=-240,y=-160+i*80)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            is_race_on=False
            break
        turtle.forward(random.randint(0,10))

my_screen.exitonclick()
