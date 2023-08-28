from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
scoreboard_l = Scoreboard((-100, 200))
scoreboard_r = Scoreboard((100, 200))

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


game_running = True
while game_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
    
    #Detect collision with l_paddle
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    #Detect miss r_paddle
    if ball.xcor() > 400:
        ball.ball_reset()
        scoreboard_l.increase_score()

    #Detect miss l_paddle
    if ball.xcor() < -400:
        ball.ball_reset()
        scoreboard_r.increase_score()


screen.exitonclick()
