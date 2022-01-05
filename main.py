from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


def run():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    screen.listen()

    paddle_1 = Paddle()
    paddle_1.goto(350,0)

    paddle_2 = Paddle()
    paddle_2.goto(-350, 0)

    ball = Ball()

    game_over = False

    while not(game_over):
        screen.update()
        ball.move()

        screen.onkeypress(paddle_1.move_up,"Up")
        screen.onkeypress(paddle_1.move_down,"Down")
        screen.onkeypress(paddle_2.move_up,"a")
        screen.onkeypress(paddle_2.move_down,"s")


if __name__ == "__main__":
    run()
