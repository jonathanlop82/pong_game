from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")

    def move_up(self):
        x = self.xcor()
        y = self.ycor() + 20
        if self.ycor() < 240:
            self.goto(x,y)

    def move_down(self):
        x = self.xcor()
        y = self.ycor() - 20
        if self.ycor() > -240:
            self.goto(x,y)