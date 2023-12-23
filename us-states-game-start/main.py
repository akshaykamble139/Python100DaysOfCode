import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(f"{len(guessed_states)}/50 Correct States", "What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state not in guessed_states and len(data[data["state"] == answer_state]) == 1:
        state_data = data[data["state"] == answer_state]

        x_cor = state_data.x.to_list()[0]
        y_cor = state_data.y.to_list()[0]
        tim.goto(x_cor,y_cor)
        tim.write(answer_state,align="center",font=("Arial",8,"normal"))

        guessed_states.append(answer_state)
        print(len(guessed_states))

states_missed = []
for state in all_states:
    if state not in guessed_states:
        states_missed.append(state)

states_dict = {
    "States": states_missed
}

missed = pandas.DataFrame(states_dict)

missed.to_csv("states_to_learn.csv")
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()



# screen.exitonclick()