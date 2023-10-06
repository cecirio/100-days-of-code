import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("azure3")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")


game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

# Detect car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_running = False

# Detect if player has reached the finish line
    if player.reached_finish_line():
        player.go_to_start()
        car_manager.speed_increase()
        scoreboard.increase_level()
        scoreboard.update_level()


screen.exitonclick()
