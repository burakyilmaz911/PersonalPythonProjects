import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The winning color was {winning_color}")

            else:
                print(f"Sorry, you lost. The winning color was {winning_color}")

        if turtle.pencolor() == user_bet:
            slow_distance = random.randint(1, 9)
            turtle.forward(slow_distance)
        else:
            rand_distance = random.randint(1, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
