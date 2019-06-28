#!/bin/python3
"""
Created on Mon Apr  9 23:20:54 2018
@author: bethanygarcia
"""
import turtle
import random
import math

# This is importing the color lists from the colorlist *file*
# NOTE the *alias* - I've renamed colorlist to *cl*
import colorlist as cl
from time import sleep

# math.tau doesn't work here, so we made our own tau
tau = 6.283185307179586

# Makes window
window = turtle.Screen()

# Makes Turtle instance
taylor = turtle.Turtle()


# Draws the starting color choices for the user
def make_color_charts(colorInfo):
    title_start = (-190, 160)
    colors_start = (-100, 173)

    for item in colorInfo:
        taylor.speed(0)
        taylor.pencolor('#000000')
        taylor.penup()
        taylor.goto(title_start)
        taylor.write(item[0], font=("Handlee", 18, "bold"))
        taylor.penup()
        taylor.goto(colors_start)

        for color in item[1]:
            taylor.pendown()
            taylor.pencolor(color)
            taylor.dot(11)
            taylor.penup()
            taylor.setheading(0)
            taylor.forward(10)

        title_start = (title_start[0], title_start[1] - 15)
        colors_start = (colors_start[0], colors_start[1] - 15)


# Draws the shape menu for the user
def make_shape_charts(drawing_types):
    title_start = (-170, 170)

    for item in drawing_types:
        taylor.speed(0)
        taylor.penup()
        taylor.goto(title_start)
        taylor.write(item, move=False, align="left", font=('Handlee', 20, "normal"))
        taylor.penup()

        title_start = (title_start[0], title_start[1] - 15)


def on_text_click(event):
    x_coordinate, y_coordinate = event.x, event.y
    print(f'x_coordinate={x_coordinate}, y_coordinate={y_coordinate}')

    if (x_coordinate <= -170) and (y_coordinate >= 280 and y_coordinate <= 300):
        turtle.onscreenclick(lambda x_coordinate, y_coordinate: turtle.bgcolor('red'))


def shape_spiral_left(palette):
    for number in range(179):
        taylor.shape('blank')
        taylor.pensize(1)
        taylor.pencolor(palette[number % 6])
        # pencolor(random.choice(colors_10))
        taylor.width(number / 100 + 1)
        taylor.forward(number)
        taylor.left(33.4)


def shape_spiral_right(palette):
    for number in range(179):
        taylor.pencolor(palette[number % 7])
        taylor.width(number / 100 + 1)
        taylor.backward(number)
        taylor.right(33.4)


def one_shape_mosaic(palette, number_sides, size, number_iterations):
    for iteration in range(0, number_iterations):
        taylor.pencolor(random.choice(palette))
        for j in range(0, number_sides):
            taylor.forward(size)
            taylor.forward(size / 2)
            taylor.left(360 / number_sides)
        taylor.left(360 / number_iterations)


def two_shape_mosaic(color_1, num_sides1, size1, color_2, num_sides2, size2, number_iterations):
    for i in range(0, number_iterations):
        taylor.pencolor(color_1)
        for j in range(0, num_sides1):
            taylor.forward(size1)
            taylor.left(360 / num_sides1)
            taylor.pencolor(color_2)
        for k in range(0, num_sides2):
            taylor.forward(size2)
            taylor.left(360 / num_sides2)

        taylor.left(360 / number_iterations)


def spirograph(R, r, d, repeats, drawing_type, palette, proportion=1):
    screen = turtle.Screen()
    theta = 0.2
    tau = 6.283185307179586
    steps = repeats * int(6 * tau / theta)
    angle = 0
    drawing_type = drawing_type
    proportion = proportion
    screen.bgcolor("#FFFFFF")

    spiro = turtle.Turtle()
    spiro.hideturtle()
    screen.tracer(0)
    spiro.pensize()

    pen = turtle.Turtle()
    pen.hideturtle()
    screen.tracer(0)
    pen.speed(0)
    pen.pensize(1)

    pen.penup()
    pen.goto(R - r + d, 0)
    pen.pendown()

    for _ in range(0, steps):
        spiro.clear()
        spiro.penup()
        spiro.setheading(0)
        spiro.goto(0, -R)
        spiro.color('#614747')
        spiro.pendown()
        spiro.circle(R)

        angle += theta
        x = (R - r) * math.cos(angle)
        y = (R - r) * math.sin(angle)

        spiro.penup()
        spiro.goto(x, y - r)
        spiro.color('#614747')
        spiro.pendown()
        spiro.circle(r)
        # spiro.shapesize(5, 4, 1)
        spiro.penup()
        spiro.goto(x, y)
        spiro.dot(6)

        x, y = x_y_parameters(R, r, d, angle, drawing_type, proportion)

        spiro.pendown()
        spiro.goto(x, y)
        spiro.dot(12)
        pen.goto(spiro.pos())
        pen.color(palette[int(angle) % 7])
        spiro.getscreen().update()
        sleep(0.05)

    sleep(0.5)
    spiro.color('#FFFFFF')
    spiro.clear()
    spiro.getscreen().update()


# Math for the different spiro shapes
def x_y_parameters(R, r, d, angle, drawing_type, proportion):
    x = None
    y = None

    if drawing_type == 'Hypotrochoid':
        x = (R - r) * math.cos(angle) + proportion * d * math.cos(((R - r) / r) * angle)
        y = (R - r) * math.sin(angle) - proportion * d * math.sin(((R - r) / r) * angle)

    if drawing_type == 'Hypocycloid':
        x = (R - r) * math.cos(angle) + proportion * r * math.cos(((R - r) / r) * angle)
        y = (R - r) * math.sin(angle) - proportion * r * math.sin(((R - r) / r) * angle)

    if drawing_type == 'Epicycloid':
        x = (R + r) * math.cos(angle) - proportion * r * math.cos(((R + r) / r) * angle)
        y = (R + r) * math.sin(angle) - proportion * r * math.sin(((R + r) / r) * angle)

    if drawing_type == 'Epitrochoid':
        x = (R + r) * math.cos(angle) - proportion * d * math.cos(((R + r) / r) * angle)
        y = (R + r) * math.sin(angle) - proportion * d * math.sin(((R + r) / r) * angle)

    if drawing_type == 'Cycloid':
        x = r * (angle - math.sin(angle))
        y = r * (1 - math.cos(angle))


    return x, y


# Draws color choices and asks for user input
names = ['palette 1', 'palette 2', 'palette 3', 'palette 4', 'palette 5', 'palette 6']
colors = [cl.colors_5, cl.colors_8, cl.colors_11, cl.colors_6, cl.colors_7, cl.colors_2]
colorInfo = zip(names, colors)
make_color_charts(colorInfo)
user_choice = input("Please enter a color palette number: ")

palette_dict = {1: cl.colors_5, 2: cl.colors_8, 3: cl.colors_11, 4: cl.colors_6, 5: cl.colors_7, 6: cl.colors_2}

palette = palette_dict[int(user_choice)]

taylor.reset()

# lists drawing types, and asks for user choice
drawing_types = ['1: left spiral', '2: right spiral', '3: Single shape mosaic', '4: Dual shape mosaic', '5: Spirographs']
drawing_numbers = [1, 2, 3, 4, 5]
make_shape_charts(drawing_types)
shape_type = input("Please enter drawing number: ")

# Depending on what the user chooses, calls that drawing function with colors
if shape_type == '1':
    taylor.reset()
    shape_spiral_left(cl.colors_1)

if shape_type == '2':
    taylor.reset()
    shape_spiral_right(palette)

# Some shapes need more user input
if shape_type == '3':
    number_sides = int(input("How many sides for your figure?"))
    size = int(input("What size would you like your figure?"))
    number_iterations = int(input("How many iterations would you like to draw?"))

    # call reset, then the drawing function
    taylor.reset()
    one_shape_mosaic(palette, number_sides, size, number_iterations)

# The 2-part mosaic takes the most choices from the user
if shape_type == '4':
    color_1 = random.choice(palette)
    color_2 = random.choice(palette)
    num_sides1 = int(input("How many sides for your first figure?"))
    num_sides2 = int(input("How many sides for your second figure?"))
    size1 = int(input("What size would you like your first figure?"))
    size2 = int(input("What size would you like your second figure?"))
    number_iterations = int(input("How many copies would you like to draw?"))

    # call reset, then the drawing function
    taylor.reset()
    two_shape_mosaic(color_1, num_sides1, size1, color_2, num_sides2, size2, number_iterations)

# This is the spirograph option, it could be customized more
if shape_type == '5':
    taylor.reset()
    title_start = (-170, 170)

    spiro_shapes = ['1:  Hypocycloid', '2:  Hypotrochoid','3:  Epicycloid', '4:  Epitrochoid', '5: Cycloid']
    spiro_types = {1:  'Hypocycloid', 2:  'Hypotrochoid',3:  'Epicycloid', 4:  'Epitrochoid', 5: 'Cycloid'}
    for item in spiro_shapes:
        taylor.speed(0)
        taylor.pencolor('#000000')
        taylor.penup()
        taylor.goto(title_start)
        taylor.write(item, font=("Handlee", 18, "bold"))
        taylor.penup()

        title_start = (title_start[0], title_start[1] - 15)

    drawing_type = spiro_types[int(input("Please enter number for Spirograph Type: "))]
    big_circle = float(input("Please enter radius of 'outer' circle: "))
    little_circle = float(input("Please enter radius of 'inner' circle: "))
    pen_length = float(input("Please enter length of drawing arm: "))
    repeats = int(input("Please enter number of cycles: "))

    # call resent, then the drawing function
    taylor.reset()
    spirograph(big_circle, little_circle, pen_length, repeats, drawing_type, palette=palette, proportion=1)

###############################################
# need to implement:  Spiro drawing types
# 'Hypocycloid'
# 'Hypotrochoid'
# 'Epicycloid'
# 'Epitrochoid'

# Different settings for spiro that draw interesting shapes
# spiro_3(98, 63, 16, 12,'Hypocycloid')
# spiro_3(98, 63, 16, 12, 'Hypotrochoid')
# spiro_3(48, 33, 0, 12, 'Epicycloid')
# spiro_3(65, 33, 100, 12, 'Epitrochoid')
# spiro_3(154, 62, 62, 4, 'Hypocycloid')
# spiro_3(90, 41, 22, 12, 'Hypotrochoid')
# spiro_3(154, 62, 62, 4, 'Hypocycloid')
# spiro_3(14, -50, 17, 6, 'Cycloid')
# spiro_3(55, 93, 32, 6, 'Epitrochoid', .45)

# more shape equations
# x = int(a * math.sin(math.radians(c * i)) + b * math.sin(math.radians(d * i)))
# y = int(a * math.cos(math.radians(c * i)) + b * math.cos(math.radians(d * i)))

# Randomizing drawing type
# drawing_type = random.choice(['Hypocycloid','Epicycloid', 'Hypotrochoid', 'Epitrochoid'])
# drawing_type = random.choice(['Hypotrachoid','Epicycloid'])
# drawing_type = random.choice(['Hypocycloid','Epicycloid', 'Hypotrochoid', 'Epitrochoid', 'Cycloid'])

# Some test calls for functions
# drawMosaic(cl.colors_11, 5, 30, 25)
# twoShapeMosaic(random.choice(colors_11),7,75,random.choice(colors_11),3,100,15)
# shape_spiral_left()


# TBD: Event Loop for continued drawing
# while True:

window.exitonclick()


