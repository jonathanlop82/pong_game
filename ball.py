from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.penup()

    def move(self):
        time.sleep(0.04)
        self.forward(10)

        if self.ycor() >= 280:
            if self.heading() == 45:
                self.setheading(315)
            else:
                self.setheading(225)

        if self.xcor() >= 380:
            if self.heading() == 315:
                self.setheading(225)
            else:
                self.setheading(135)

        if self.ycor() <= -280:
            if self.heading() == 225:
                self.setheading(135)
            else:
                self.setheading(45)

        if self.xcor() <= -380:
            if self.heading() == 225:
                self.setheading(315)
            else:
                self.setheading(45)