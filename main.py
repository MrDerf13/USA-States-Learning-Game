import pandas
import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
turtle.penup()

states_data = pandas.read_csv("50_states.csv")
state_list = states_data["state"].to_list()

pen = Turtle()
pen.penup()
pen.hideturtle()

states_guessed = []
while len(states_guessed) < 50:
    state_guess = turtle.textinput(f"{len(states_guessed)}/50 States Correct", "What's a state name?").title()

    if state_guess == "Exit":
        states_to_learn = [state for state in state_list if state not in states_guessed]
        ser = pandas.Series(states_to_learn)
        ser.to_csv("states_to_learn.csv")
        break

    if state_guess in state_list:
        states_guessed.append(state_guess)
        state_x = states_data[states_data.state == state_guess]["x"].item()
        state_y = states_data[states_data.state == state_guess]["y"].item()
        pen.goto(int(state_x), int(state_y))
        pen.write(f"{state_guess}")

    else:
        pass
