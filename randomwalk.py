
from turtle import Turtle, Screen
import turtle

turtle.colormode(255)
import random

tim = Turtle()
tim.shape("arrow")
tim.pensize(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


x = random_color()
print(x)
# colors = ['orchid', "medium blue", "black", "blue", "red", 'yellow', "green", "maroon", "orange"]
directions = [0, 90, 180, 270]

for x in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))
screen=Screen() 
screen.exitonclick   
