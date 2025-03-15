from turtle import Turtle

MOVE_DISTANCE=10
class Snake:
    def __init__(self):
        self.snakes=list()
        self.current_position=(0,0)
        self.head=None
        for i in range(3):
            self.snakes.append(Turtle(shape='square'))
            self.snakes[i].color('white')
            self.snakes[i].penup()
            self.snakes[i].shapesize(0.5)
            self.snakes[i].goto(x=-i * 10, y=0)
            if i==0:
                self.head=self.snakes[i]

    def add_segment(self):
        new_segment=Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.shapesize(0.5)
        new_position=self.snakes[-1].pos()
        new_segment.goto(*new_position)
        self.snakes.append(new_segment)

    def move_forward(self):
        for i in range(len(self.snakes)):
            prev_position = self.current_position
            self.current_position = self.snakes[i].pos()
            if i > 0:
                self.snakes[i].goto(*prev_position)
            else:
                self.snakes[i].forward(MOVE_DISTANCE)

    def turn_right(self):
        for snake in self.snakes:
            snake.right(90)

    def turn_left(self):
        for snake in self.snakes:
            snake.left(90)
    def up(self):
        if self.snakes[0].heading()==0:
            self.turn_left()
        elif self.snakes[0].heading()==180:
            self.turn_right()
    def down(self):
        if self.snakes[0].heading()==0:
            self.turn_right()
        elif self.snakes[0].heading()==180:
            self.turn_left()
    def left(self):
        if self.snakes[0].heading()==90:
            self.turn_left()
        elif self.snakes[0].heading()==270:
            self.turn_right()
    def right(self):
        if self.snakes[0].heading()==90:
            self.turn_right()
        elif self.snakes[0].heading()==270:
            self.turn_left()