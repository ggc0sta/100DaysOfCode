import colorgram
import pandas
import turtle as t
import random


def get_colors(image="painting.png", num_of_colors=10):
    colors = colorgram.extract(image, num_of_colors)
    color_list = []
    for _ in range(num_of_colors):
        color = colors[_].rgb
        rgb = (color.r, color.g, color.b)
        color_list.append(rgb)
    return color_list

painting_colors = get_colors()

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

# setting coordinates
tim.setx(-200)
tim.sety(-300)


def draw_dotted_line():
    for _ in range(10):
        tim.dot(20, random.choice(painting_colors))
        if _ < 9:
            tim.forward(50)


def up_and_left():
    tim.setheading(90)
    tim.forward(50)
    tim.left(90)
    for _ in range(10):
        if _ < 9:
            tim.forward(50)
    tim.left(180)


for _ in range(10):
    draw_dotted_line()
    up_and_left()

screen = t.Screen()
screen.exitonclick()


