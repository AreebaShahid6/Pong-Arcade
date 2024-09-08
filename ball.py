from turtle import Screen, Turtle
import time

# Ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.x_move = 10  # Initialize x-axis movement speed
        self.y_move = 10
        self.mov_speed = 0.1  # Initialize movement speed

    def mov(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # Reverse the direction of the y-axis movement

    def bounce_x(self):
        self.x_move *= -1  # Reverse the direction of the x-axis movement
        self.mov_speed *= 0.9  # Increase speed slightly after hitting a paddle

    def reset_position(self):
        self.goto(0, 0)  # Reset ball to center
        self.mov_speed = 0.1  # Reset speed
        self.bounce_x()  # Change direction to start moving



