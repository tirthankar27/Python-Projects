from turtle import Turtle
class ScoreBoard:
    def __init__(self):
        self.score=0
        self.writer=Turtle()
        self.writer.penup()
        self.writer.color('white')
        self.writer.goto(x=0,y=280)
        self.writer.hideturtle()
        self.writer.speed(0)
    def update_score(self):
        self.score+=1
        self.writer.clear()
        self.writer.goto(x=0, y=280)

    def game_over(self):
        self.writer.goto(0,0)
        self.writer.write("GAME OVER!", align='center', font=('Courier', 36, 'bold'))

    def scoreboard(self):
        self.writer.write(f"Score: {self.score}", align='center', font=('Courier', 12, 'bold'))