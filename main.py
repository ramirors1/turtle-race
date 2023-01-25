import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=700, height=500)
user_bet = screen.textinput(title="Place your bet.", prompt="Which turtle will win? Pick a color.")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [150, 100, 50, 0, -50, -100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-340, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 320:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congrats, you won! {winning_color} turtle is the winner.")
            else:
                print(f"You lost.  {winning_color} turtle won the race.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()