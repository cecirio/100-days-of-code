from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_level()


    def update_level(self):
        self.write(f"LEVEL:{self.level}", font=FONT)

    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()
