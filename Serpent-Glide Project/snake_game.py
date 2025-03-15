import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen=Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor('black')
my_screen.title("Serpent Glide")
my_screen.tracer(0,0)
my_screen.listen()
serpent=Snake()
food=Food()
my_score=ScoreBoard()

my_screen.onkey(key="Up",fun=serpent.up)
my_screen.onkey(key="Down",fun=serpent.down)
my_screen.onkey(key="Left",fun=serpent.left)
my_screen.onkey(key="Right",fun=serpent.right)

is_game_on=True
current_position=(0,0)
while is_game_on:
    my_score.scoreboard()
    my_screen.update()
    time.sleep(0.1)
    if serpent.snakes[0].xcor()>280 or serpent.snakes[0].xcor()<-280 or serpent.snakes[0].ycor()>280 or serpent.snakes[0].ycor()<-280:
        is_game_on = False
        my_score.game_over()
    serpent.move_forward()
    if serpent.snakes[0].distance(food) < 10:
        food.update_position()
        serpent.add_segment()
        my_score.update_score()
    for segment in serpent.snakes[1:]:
        if serpent.head.distance(segment)<5:
            is_game_on=False
            my_score.game_over()
            break

my_screen.exitonclick()
