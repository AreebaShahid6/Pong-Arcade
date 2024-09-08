from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x_position, 0)
        self.speed("fastest")

    def go_up(self):
        y = self.ycor()
        if y < 250:
            self.sety(y + 20)

    def go_down(self):
        y = self.ycor()
        if y > -250:
            self.sety(y - 20)