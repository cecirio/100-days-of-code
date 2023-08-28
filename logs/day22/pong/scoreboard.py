from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(self.score, align="center", font=("Courier", 50, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=("Courier", 50, "bold"))
