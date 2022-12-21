import pandas as pd

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()

answer_state = "Florida"
if answer_state in states:
    #print(answer_state)
    print(data["x"][data.state == answer_state].values)