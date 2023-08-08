from turtle import Turtle, Screen
import random 

# SCREEN SETUP
lets_race = False
screen = Screen() 
screen.setup(width=500, height=400)
screen.title("Teenage Mutant Ninja Turtle Race!")
screen.bgcolor("grey")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["blue", "red", "purple", "orange"]
y_coordinates = [-100, -50, 50, 100]
all_tmnts = []

# FINISH LINE
gap_size = 20
t = Turtle(shape="square")
t.penup()

# WHITE SQUARES ROW 1
t.color("white")
for i in range(10):
    t.goto(230, (170 - (i * gap_size * 2)))
    t.stamp()

# WHITE SQUARES ROW 2
for i in range(10):
    t.goto(230 - gap_size, (210 - gap_size) - (i * gap_size * 2))
    t.stamp()

# BLACK SQUARES ROW 1
t.color("black")
for i in range(10):
    t.goto(230, (190 - (i * gap_size * 2)))
    t.stamp()

# BLACK SQUARES ROW 2
for i in range(10):
    t.goto(230 - gap_size, (190 - gap_size) - (i * gap_size * 2))
    t.stamp()


# TEENAGE MUTANT NINJA TURTLES!
for ninja_turtle in range(0, 4):
    tmnt = Turtle(shape="turtle")
    tmnt.color(colors[ninja_turtle])
    tmnt.penup()
    tmnt.goto(x=-230, y=y_coordinates[ninja_turtle])
    all_tmnts.append(tmnt)


if user_bet:
    lets_race = True

# RACE!
while lets_race:
    for tmnt in all_tmnts:
        if tmnt.xcor() > 210:
            lets_race = False
            winner_color = tmnt.pencolor()
            if winner_color == user_bet:
                print(f"You have won! The {winner_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winner_color} turtle is the winner!")
        travel_distance = random.randint(0, 10)
        tmnt.forward(travel_distance)

screen.exitonclick()
