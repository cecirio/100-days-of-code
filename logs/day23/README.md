# Day 23 - The Turtle Crossing Capstone Project
## Turtle Crossing Game

![](turtle_crossing.gif)

## Excersises
### Step 1: Setup the Main Screen
- Setup a screen with a width of 600px and a height of 600px.
- Make sure the screen window remains open until it is clicked to close it.
- Use the tracer() method to skip turtle creation animations and use the update() method to refresh the screen afterwards.

**Code**
<details><summary></summary>
<p>

```Python
import time
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("azure4")
screen.tracer(0)

game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
```

</p>
</details>

#

### Step 2: Create the Player Behaviour
- Create a new file named player.py to add the Player class.
- Create a turtle player object that starts at the bottom of the screen.
- Make the turtle player listen for the "Up" keypress to move the turtle north.

**Code**
<details><summary>player.py</summary>
<p>

```Python
from turtle import Turtle
STARTING_POSITION = (0, -280)
TRAVEL_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("DarkGreen")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)


    def up(self):
        self.forward(TRAVEL_DISTANCE)
```

</p>
</details>

**Code**
<details><summary>main.py</summary>
<p>

```Python
from player import Player

player = Player()

screen.listen()
screen.onkeypress(player.up, "Up")

```

</p>
</details>

#

### Step 3: Create the Car Behaviour
- Create cars that are 20px wide and 40px long.
- Make them generate randomly along the y-axis and move towards the left side of the screen.
- Leave room along the top and bottom 50px of the screen to allow for the turtle's safety zones.
- Because the random genration of cars makes it nearly impossible to play, generate the cars only every 6th time the game loop runs.

**Code**
<details><summary>car_manager.py</summary>
<p>

```Python
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
```

</p>
</details>

**Code**
<details><summary>main.py</summary>
<p>

```Python
from car_manager import CarManager

car_manager = CarManager()

game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

```

</p>
</details>

#

### Step 4: Detect When the Turtle Collides with a Car
- Use a method to determine if the distance between a car and player intersect to determine collision.
- When collision is detected between the turtle and a car, stop the game.

**Code**
<details><summary>main.py</summary>
<p>

```Python
game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_running = False
```

</p>
</details>

#

### Setp 5: Detect When the Player has Reached the Other Side
- Detect when the turtle player has reached the top edge of the screen (Finish Line).
- Once it reaches the finish line, return the turtle to its starting position.
- Increase the speed of the cars. 

**Code**
<details><summary>player.py</summary>
<p>

```Python
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.go_to_start()
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def reached_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
```

</p>
</details>

**Code**
<details><summary>main.py</summary>
<p>

```Python
game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

    if player.reached_finish_line():
        player.go_to_start()
        car_manager.speed_increase()
```

</p>
</details>

#

### Step 6: Add the Scoreboard and Game Over Sequence
- Create a scoreboard that keeps track of which level the user is on.
- Everytime the turtle player successfully crosses the road, increase the level.
- When the the turtle player is hit by a car, the GAME OVER should be displayed in the center of the screen.

**Code**
<details><summary>scoreboard.py</summary>
<p>

```Python
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
```

</p>
</details>

**Code**
<details><summary>main.py</summary>
<p>

```Python
game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_running = False

    if player.reached_finish_line():
        scoreboard.increase_level()
        scoreboard.update_level()
```

</p>
</details>

#
