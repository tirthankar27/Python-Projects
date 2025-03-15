import time
from turtle import Turtle,Screen
from snake import Snake

my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor('black')
my_screen.title("Serpent Glide")
my_screen.tracer(0)
my_screen.listen()
serpent=Snake()

my_screen.onkey(key="Up",fun=serpent.up)
my_screen.onkey(key="Down",fun=serpent.down)
my_screen.onkey(key="Left",fun=serpent.left)
my_screen.onkey(key="Right",fun=serpent.right)

is_game_on=True
current_position=(0,0)
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    if serpent.snakes[0].xcor()>280 or serpent.snakes[0].xcor()<-280 or serpent.snakes[0].ycor()>280 or serpent.snakes[0].ycor()<-280:
        is_game_on = False
        break
    serpent.move_forward()

my_screen.exitonclick()
