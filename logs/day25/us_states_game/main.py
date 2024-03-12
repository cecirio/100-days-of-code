import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

import pandas
states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").capitalize()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        break
    elif answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = states_data[states_data.state == answer_state]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(answer_state) # t.write(state_row.state.item()) May also be used
