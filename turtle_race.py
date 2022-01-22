import random
from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=600, height=500)
user_guess = screen.textinput(title="Who's winning", prompt="Which colour will win the race: ")
colors = ["blue", "red", "violet", "orange", "green", "brown"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for turtle_dex in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_dex])
    turtle.penup()
    turtle.goto(x=-285, y=y_positions[turtle_dex])
    all_turtles.append(turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for c_turtle in all_turtles:
        if c_turtle.xcor() > 290:
            is_race_on = False

            winning_color = c_turtle.pencolor()
            if winning_color == user_guess:
                print(f"You Win!{winning_color} wins the Race")
            else:
                print(f"You Lose!{winning_color} wins the Race")

        random_distance = random.randint(0, 10)
        c_turtle.forward(random_distance)

screen.exitonclick()
