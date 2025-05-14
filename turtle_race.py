from turtle import  Turtle, Screen
import random

is_race_on = False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Betting",prompt="place color of turtle you betting on")
print(user_bet)
all_turtles = []

color=["black","green","orange","blue","brown","red"]
turtle_position=[-100,-70,-40,-10,20,50]

for turtle_index in range(0,6):
    Mageba=Turtle(shape="turtle")
    Mageba.color(color[turtle_index])
    Mageba.penup()
    Mageba.goto(x=-230,y=turtle_position[turtle_index])
    all_turtles.append(Mageba)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)






screen.exitonclick()