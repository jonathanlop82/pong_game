from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle()
paddle_1.goto(350,0)

paddle_2 = Paddle()
paddle_2.goto(-350, 0)

game_over = False

while not(game_over):
    screen.update()

    screen.listen()

    screen.onkeypress(paddle_1.move_up,"Up")
    screen.onkeypress(paddle_1.move_down,"Down")

    screen.onkeypress(paddle_2.move_up,"a")
    screen.onkeypress(paddle_2.move_down,"s")




screen.exitonclick()