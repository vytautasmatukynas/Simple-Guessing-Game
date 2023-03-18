import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")
img = "blank_states_img.gif"

# import .gif file as shape
screen.addshape(img)
# set turtle shape
turtle.shape(img)

# # gets coordinates of mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# # keeps screen open
# turtle.mainloop()


data = pd.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states) + 1:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} "
                                          f"is correct", prompt="What is this state name?").title()
                                          # .title() capitalize string, like "kazkas".title() = "Kazkas"

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    else:
        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            # hide turte
            t.hideturtle()
            # don't draw anything on move
            t.penup()

            state_data = data[data.state == answer_state]
            # moves turtle to this location
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)

