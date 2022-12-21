from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POS = (210, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1

    def print_level(self):
        self.clear()
        self.goto(LEVEL_POS)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


