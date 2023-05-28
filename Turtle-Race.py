import random
import turtle
from turtle import Turtle, Screen


def timmy():
    tim = Turtle()
    tim.speed("fastest")
    tim.hideturtle()
    tim.penup()
    tim.goto(x=230, y=190)
    tim.pendown()
    tim.pensize(2)
    tim.setheading(270)
    while tim.ycor() > -180:
        tim.forward(10)
        tim.penup()
        tim.forward(5)
        tim.pendown()
        tim.forward(10)


screen = Screen()
screen.setup(width=500, height=400)
timmy()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

initial_position = -125
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(1.3)
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=initial_position)
    all_turtles.append(new_turtle)
    initial_position += 50

user_bet = turtle.textinput(title="Make your bet", prompt="Which tutle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() < 210:
                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)
            else:
                is_race_on = False
                winner = turtle

if user_bet.lower() == winner.pencolor():
    print(f"You guessed correctly! the winner is: the {winner.pencolor()} turtle!")
else:
    print(f"You guessed wrong! the winner is: the {winner.pencolor()} turtle!")

screen.exitonclick()
