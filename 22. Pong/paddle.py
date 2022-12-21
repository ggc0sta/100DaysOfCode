from turtle import Turtle
PADDLE_WIDTH = 5
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=None, stretch_len=5, outline=None)
        self.setheading(90)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def up(self):
        if self.ycor() <= 240:
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() >= -220:
            self.backward(MOVE_DISTANCE)

