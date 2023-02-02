from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)

all_turtles = []
is_race_on = False
colors = ["orange", "pink","blue","black","red", "gray",]
for position in range(6):
    tim = Turtle("turtle")
    tim.penup()
    tim.color(colors[position])
    tim.goto(x=-245, y=-170+(position*50))
    all_turtles.append(tim)

user_bet = screen.textinput(title="make your bet", prompt="which colour will win?")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
       if turtle.xcor()>240:
         is_race_on = False
         if user_bet == turtle.pencolor():
           print(f"you win. The {turtle.pencolor()} win the race")
         else:
            print(f"you lose.The {turtle.pencolor()} win the race ")
          
       
       
       distance = random.randint(0,10)
       turtle.forward(distance)


screen.exitonclick()