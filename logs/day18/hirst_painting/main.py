import turtle
import random

turtle.colormode(255)

"""
import colorgram

# Extract 25 colors from jpg image.
colors = colorgram.extract("image.jpg", 25)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]


tim = turtle.Turtle()
tim.speed("fastest")
tim.up()
tim.hideturtle()

def starting_position():
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)


def row_start():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


starting_position()


for row in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    row_start()


screen = turtle.Screen()
screen.exitonclick()
