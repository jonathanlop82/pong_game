from turtle import Turtle

class Score(Turtle):

    def __init__(self,player_name):
        super().__init__()
        self.player_name = player_name
        self.color('white')
        self.penup()
        #self.goto(0, 270)
        self.hideturtle()
        self.count = 0
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"{self.count}", False, align='center', font=('Courier', 60, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"{self.player_name} WIN", False, align='center', font=('Courier', 40, 'normal'))

    def sum_point(self):
        self.count += 1
        self.write_score()
