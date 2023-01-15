from turtle import Turtle, Screen
from random import randrange


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color: ")
turtles = []
winner = ""
finish = 240
is_race_on = True


def start():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    names = ["red", "orange", "yellow", "green", "blue", "purple"]

    name = 0
    y_line = -150

    for color in colors:
        names[name] = Turtle()
        names[name].shape("turtle")
        names[name].color(color)
        names[name].penup()
        names[name].goto(x=-230, y=y_line)
        turtles.append(names[name])

        name += 1
        y_line += 60

def start_race():

    for turtle in turtles:
        turtle.forward(randrange(100))
        if turtle.xcor() > 200:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Congrats, u won!! The winner is {turtle.pencolor()}")
                exit()
            else:
                print(f"The winner is: {turtle.pencolor()}, u lost, sad")
                exit()



screen.listen()
screen.onkey(key="space", fun=start)
screen.onkey(key="s", fun=start_race)


screen.exitonclick()