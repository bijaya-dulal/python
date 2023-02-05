from turtle import Turtle, Screen
'''use 
f bottom for forward move
b for backward
u for penup
d for pendown
l for left turn
r for right 
c for clear your screen
'''

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def penup():
    tim.penup()


def pendown():
    tim.pendown()


def move_backward():
    tim.backward(20)


def turn_left():
    heading = tim.heading() + 10
    tim.setheading(heading)


def turn_right():
    heading = tim.heading() - 10
    tim.setheading(heading)


def clear_draw():
    tim.reset()


screen.listen()
screen.onkey(move_backward, "b")
screen.onkey(move_forward, "f")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.onkey(clear_draw, "c")
screen.onkey(penup, "u")
screen.onkey(pendown, "d")

screen.exitonclick()
