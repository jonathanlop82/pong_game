from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score


def run():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    screen.listen()

    paddle_1 = Paddle()
    paddle_1.goto(350, 0)


    paddle_2 = Paddle()
    paddle_2.goto(-350,0)

    ball = Ball()

    score_player_1 = Score("Player 1")
    score_player_1.goto(200, 230)
    score_player_1.write_score()

    score_player_2 = Score("Player 2")
    score_player_2.goto(-200, 230)
    score_player_2.write_score()

    game_over = False

    while not game_over:
        screen.update()
        ball.move()

        screen.onkeypress(paddle_1.move_up, "Up")
        screen.onkeypress(paddle_1.move_down, "Down")
        screen.onkeypress(paddle_2.move_up, "a")
        screen.onkeypress(paddle_2.move_down, "s")

        #Detect collision with the paddle
        if paddle_1.distance(ball) < 50 and ball.xcor() > 330:
            ball.move_speed -= 0.01
            if ball.heading() == 315:
                ball.setheading(225)
            else:
                ball.setheading(135)

        if paddle_2.distance(ball) < 50 and ball.xcor() < -330:
            ball.move_speed -= 0.01
            if ball.heading() == 225:
                ball.setheading(315)
            else:
                ball.setheading(45)

        # Detect the ball pass the paddle
        if ball.xcor() > 350:
            ball.setheading(135)
            ball.goto(0, 0)
            score_player_2.sum_point()
            ball.move_speed = 0.08
        elif ball.xcor() < -350:
            ball.setheading(45)
            ball.goto(0,0)
            score_player_1.sum_point()
            ball.move_speed = 0.08

        if score_player_1.count == 5:
            score_player_1.game_over()
            game_over = True
        elif score_player_2.count == 5:
            score_player_2.game_over()
            game_over = True

    screen.exitonclick()


if __name__ == "__main__":
    run()
