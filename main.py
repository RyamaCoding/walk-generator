from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["Blue", "Red", "Orange", "Green", "Purple", "Yellow"]

def draw_random(steps):
    angle = [0, 90, 180, 270]
    for _ in range(steps):
        tim.forward(30)
        tim.right(random.choice(angle))

for _ in range(10):
    tim.speed("fastest")
    tim.pensize(15)
    tim.color(random.choice(colors))
    draw_random(_)


screen = Screen()
screen.exitonclick()

