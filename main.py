from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.title("Pong")
my_screen.tracer(0)

# Create paddles, ball, and scoreboard
left_paddle = Paddle(-280)  # Paddle on the left side
right_paddle = Paddle(280)  # Paddle on the right side
ball = Ball()
score = Score()

# Define movement functions for paddles
def left_paddle_up():
    left_paddle.go_up()

def left_paddle_down():
    left_paddle.go_down()

def right_paddle_up():
    right_paddle.go_up()

def right_paddle_down():
    right_paddle.go_down()

# Key press listeners
my_screen.listen()
my_screen.onkey(left_paddle_up, "w")   # Controls for left paddle
my_screen.onkey(left_paddle_down, "s")
my_screen.onkey(right_paddle_up, "Up")   # Controls for right paddle
my_screen.onkey(right_paddle_down, "Down")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.mov_speed)  # Control the update rate based on ball speed
    my_screen.update()
    ball.mov()

    # Bounce the ball off the top and bottom edges
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Bounce the ball off the paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 260) or (ball.distance(left_paddle) < 50 and ball.xcor() < -260):
        ball.bounce_x()

    # End game if the ball crosses the left or right boundaries
    if ball.xcor() > 290:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -290:
        ball.reset_position()
        score.r_point()

my_screen.exitonclick()