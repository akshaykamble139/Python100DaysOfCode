# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
# for item in colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
x = -250
y = -250
timmy.speed(0)
timmy.hideturtle()

for i in range(10):
    timmy.penup()
    timmy.setpos(x, y)
    for _ in range(10):
        timmy.pendown()
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
    x = -250
    y += 50




screen = t.Screen()
screen.exitonclick()
