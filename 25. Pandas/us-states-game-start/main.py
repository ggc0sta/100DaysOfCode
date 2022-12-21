import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(width=725, height=491)

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()


def print_state(answer):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    state_data = data[data["state"] == answer]
    x = int(state_data["x"])
    y = int(state_data["y"])
    state_name = state_data["state"].item()

    t.goto(x, y)
    t.write(state_name)


correct_states = []

while len(correct_states) <= 50:
    answer_state = screen.textinput(title=f"Guess the State {len(correct_states)}/{len(states)}",
                                    prompt="What's another US state?").title()
    if answer_state in states:
        print_state(answer_state)
        correct_states.append(answer_state)
    elif answer_state == "Exit":
        states_to_learn = []
        for state in states:
            if state not in correct_states:
                states_to_learn.append(state)
        pd.DataFrame(states_to_learn).to_csv("States to Learn.csv")
        break

screen.exitonclick()
