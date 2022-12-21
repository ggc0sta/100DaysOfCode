from turtle import Turtle
FONT = "Courier"
FONT_SIZE = 80

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()

        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=(FONT, FONT_SIZE, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=(FONT, FONT_SIZE, 'normal'))
