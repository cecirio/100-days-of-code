from turtle import Turtle
STARTING_POSITION = (0, -280)
TRAVEL_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("DarkGreen")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    
    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def up(self):
        self.forward(TRAVEL_DISTANCE)


    def reached_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
