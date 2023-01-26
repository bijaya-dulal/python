import random
from turtle import Turtle,Screen
tim=Turtle()
tim.shape("turtle")
colors = ['orchid', "medium blue", "black", "blue", "red", 'yellow', "green", "maroon", "orange"]
directions = [0, 90, 180, 270]
def draw_shape(num_side):
    tim.color(random.choice(colors))
    angle = 360 / num_side
    for n in range(num_side):
        tim.forward(100)
        tim.right(angle)


for polygon in range(3, 11):
   draw_shape(polygon)

screen = Screen()
screen.exitonclick()
