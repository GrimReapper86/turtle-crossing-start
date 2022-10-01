from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level = {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()
