from turtle import Turtle, Screen
import random
turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")

# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)


# x = 5
# step = 5
# for i in range(20):
#     turtle.forward(5)
#     turtle.teleport(x + 5)
#     x += 10


# n = 3
# for _ in range(8):
#     turtle.pencolor(random.random(), random.random(), random.random())
#     angle = 360/n
#     for i in range(n):
#         turtle.right(angle)
#         turtle.forward(100)
#     n += 1


# direction = [90, 180, 270, 360]
#
# turtle.width(20)
# turtle.speed(0)
# for _ in range(100):
#     turtle.color(random.random(), random.random(), random.random())
#     turtle.right(random.choice(direction))
#     turtle.forward(25)

turtle.speed(0)
for _ in range(72):
    turtle.color(random.random(), random.random(), random.random())
    turtle.left(5)
    turtle.circle(100)


screen = Screen()
screen.exitonclick()