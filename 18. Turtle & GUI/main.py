import turtle as t
import random

t.colormode(255)
tim = t.Turtle()  # Turtle object saved inside timmy
screen = t.Screen()

tim.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


# # challenge 1 - Draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# # challenge 2 - draw a dotted line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# challenge 3 -
"""Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
each side has 100 in length
all shapes should be drawn in sequence """


#
# for shapes in range(3, 11):
#     angle = 360/shapes
#
#     # choosing a random color
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.pencolor(r, g, b)
#     for side in range(shapes):
#         tim.forward(100)
#         tim.right(angle)


# Challenge 4. Random walk
# colors = ["orange", "deep sky blue", "medium orchid", "light salmon", "teal", "crimson"]
# tim.speed("fastest")
# tim.pensize(10)
#
# for _ in range(200):
#     color = random.choice(colors)
#     tim.pencolor(color)
#     directions = [0, 90, 180, 270]
#     direction = random.choice(directions)
#     tim.setheading(direction)
#     tim.forward(30)


# Challenge 4.2. Randomized colors


# tim.speed("fastest")
# tim.pensize(10)
#
# for _ in range(200):
#     tim.pencolor(random_color())
#     directions = [0, 90, 180, 270]
#     direction = random.choice(directions)
#     tim.setheading(direction)
#     tim.forward(30)

# Challenge 5 - Draw a Spirograph
# Each circle has a radius of 100
tim.speed("fastest")
size_of_gap = 5
steps = int(360/size_of_gap)
for _ in range(steps):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)


# To keep screen visible
screen.exitonclick()


