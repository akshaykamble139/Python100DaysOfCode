from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
is_race_on = False
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_Turtles = []
if user_bet:
    is_race_on = True

for index in range(6):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(colors[index])
    tim.goto(-230,y_position[index])
    all_Turtles.append(tim)

while is_race_on:
    for turtle in all_Turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def move_clockwise():
#     tim.right(10)
#
#
# def move_counter_clockwise():
#     tim.left(10)
#
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards,"w")
# screen.onkey(move_backwards,"s")
# screen.onkey(move_counter_clockwise,"d")
# screen.onkey(move_clockwise,"a")
# screen.onkey(clear_screen,"c")

screen.exitonclick()