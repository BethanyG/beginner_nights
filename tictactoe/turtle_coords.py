#!/bin/python3

import turtle
import math


# Makes window
window = turtle.Screen()

#Make Taylor Instance
taylor = turtle.Turtle()

#Set Shape & Speed
taylor.shape('turtle')
taylor.speed(8)

#Set Color & Width of Pen
taylor.color('#f08504')
taylor.width(5)

#Get to the Starting Position
taylor.penup()
taylor.goto(-150, 150)

#Get Ready to Draw
taylor.pendown()


#Bounding Square (300 x 300)
def bounding_square():
    for _ in range(4):
        taylor.forward(300)
        taylor.right(90)

bounding_square()

#taylor.forward(300)
#taylor.right(90)
#taylor.forward(300)
#taylor.right(90)
#taylor.forward(300)
#taylor.right(90)


#Set a New Color & Width for the Coordinate Lines
taylor.color('#8d024a')
taylor.width(5)
taylor.penup()


taylor.goto(-50, 150)
taylor.pendown()
taylor.right(90)
taylor.forward(300)
taylor.penup()
taylor.goto(50, 150)
taylor.pendown()
taylor.forward(300)
taylor.penup()
taylor.goto(-150, 50)
taylor.left(90)
taylor.pendown()
taylor.forward(300)
taylor.penup()
taylor.goto(-150, -50)
taylor.pendown()
taylor.forward(300)
taylor.penup()
taylor.goto(-150, 150)

'''
#determing general coordinates
taylor.goto(-150, 150) #origin of border
taylor.color('#1592cc')
taylor.goto(-100, 100)  #left top center
taylor.pendown()
taylor.dot(10)
taylor.penup()
taylor.goto(0, 100) #center top center
taylor.pendown()
taylor.dot(10)
taylor.penup()
taylor.goto(100, -100) #right bottom center
taylor.pendown()
taylor.dot(10)
taylor.penup()
taylor.goto(100, 0) #center right center
taylor.pendown()
taylor.dot(10)
taylor.penup()
taylor.goto(0, 0) #center center
taylor.pendown()
taylor.dot(10)
taylor.penup()
taylor.goto(-100, 0) #center left center
taylor.pendown()
taylor.dot(10)
taylor.penup()
taylor.goto(100, 100) #right top center
taylor.pendown()
taylor.dot(10)
taylor.penup()
taylor.goto(-100, -100) #left bottom center
taylor.pendown()
taylor.dot(10)
taylor.penup()
taylor.goto(0, -100) #center bottom center
taylor.pendown()
taylor.dot(10)
taylor.penup()
'''



###------------TOP ROW--------------------###
#x = (-100, 0, 100)
#y = (55, 55, 55)


def draw_o(x, y):
    taylor.goto(x, y)
    taylor.dot(10)
    taylor.pensize(5)
    taylor.pendown()
    taylor.circle(45)
    taylor.penup()

def draw_x(x1, y1, x2, y2):
    #left corner
    taylor.goto(x1, y1)
    taylor.setheading(90)
    taylor.right(135)
    taylor.forward(10)
    taylor.pendown()
    taylor.forward(120)
    taylor.penup()

    #right corner
    taylor.goto(x2, y2)
    taylor.setheading(90)
    taylor.left(135)
    taylor.forward(10)
    taylor.pendown()
    taylor.forward(120)
    taylor.penup()


xy_1 = ((-150, 150, -50, 150), (-50, 150, 50, 150), (50, 150, 150, 150))
xy_2 = ((-150, 50, -50, 50), (-50, 50, 50, 50), (50, 50, 150, 50))
xy_3 = ((-150, -50, -50, -50), (-50, -50, 50, -50), (50, -50, 150, -50))

for item in xy_1:
    draw_x(*item)

for item in xy_2:
    draw_x(*item)

for item in xy_3:
    draw_x(*item)

#determining coordinates for Os
taylor.goto(-150, 150) #origin of border
taylor.setheading(0)
taylor.color('#51f542')

coords_1 = zip((-100, 0, 100), (55, 55, 55))  # x:left, middle, right y:top
print(coords_1)
coords_2 = zip((-100, 0, 100), (50, 50, 50))  # x:left, middle, right y:middle
print(coords_2)
coords_3 = zip((-100, 0, 100), (-50, -50, -50))  # x:left, middle, right y:bottom
print(coords_3)

for item in coords_1:
    draw_o(*item)
    where = taylor.pos()
    # Set drawing color
    taylor.color('#8d024a')
    # Write out current coordinates
    taylor.write(str(where) + "  ", align="left", font=("Handlee", 20))

#for item in coords_2:
#    draw_o(*item)

#for item in coords_3:
#    draw_o(*item)

game_pieces = {
    '1_O': (-100, 55),   '2_O': (0, 55),   '3_O': (100, 55),
    '4_O': (-100, -45),  '5_O': (0, -45),  '6_O': (100, -45),
    '7_O': (-100, -145), '8_O': (0, -145), '9_O': (100, -145),
    '1_X': (-150, 150, -50, 150),
    '2_X': (-50, 150, 50, 150),
    '3_X': (50, 150, 150, 150),
    '4_X': (-150, 50, -50, 50),
    '5_X': (-50, 50, 50, 50),
    '6_X': (50, 50, 150, 50),
    '7_X': (-150, -50, -50, -50),
    '8_X': (-50, -50, 50, -50),
    '9_X': (50, -50, 150, -50)
}


'''
taylor.goto(-100, 55)  #left top square
taylor.pendown()
taylor.circle(45)
taylor.penup()

taylor.goto(0, 55) #center top square
taylor.pendown()
taylor.circle(45)
taylor.penup()

taylor.goto(100, 55) #right top square
taylor.pendown()
taylor.circle(45)
taylor.penup()

###------------CENTER ROW--------------------###
#x = (-100, 0, 100)
#y = -45

taylor.goto(-100, -45) #center left square
taylor.pendown()
taylor.circle(45)
taylor.penup()

taylor.goto(0, -45) #center center square
taylor.pendown()
taylor.circle(45)
taylor.penup()

taylor.goto(100, -45) #right center square
taylor.pendown()
taylor.circle(45)
taylor.penup()




###------------BOTTOM ROW--------------------###
#x = (-100, 0, 100)
#y = -145

taylor.goto(-100, -145) #left bottom square
taylor.pendown()
taylor.circle(45)
taylor.penup()

taylor.goto(0, -145) #center bottom square
taylor.pendown()
taylor.circle(45)
taylor.penup()

taylor.goto(100, -145) #right bottom square
taylor.pendown()
taylor.circle(45)
taylor.penup()



#determing coordinates for Xs
taylor.goto(-150, 150) #origin of border
taylor.color('#f5f242')
taylor.pensize(8)

###------------TOP ROW--------------------###
#x = ((-150, -50), (-50, 50), (50, 150))
#y = 150

xy = ((-150, 150, -50, 150), (-50, 150, 50, 150), (50, 150, 150, 150))

#X in top LEFT square
taylor.goto(-150, 150)  #left corner
taylor.setheading(90)
taylor.right(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

taylor.goto(-50, 150)  #right corner
taylor.setheading(90)
taylor.left(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()


#X in top CENTER square
taylor.goto(-50, 150) #left corner
taylor.setheading(90)
taylor.right(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

taylor.goto(50, 150) #right corner
taylor.setheading(90)
taylor.left(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

#X in top RIGHT square
taylor.goto(50, 150) #left corner
taylor.setheading(90)
taylor.right(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

taylor.goto(150, 150) #right corner
taylor.setheading(90)
taylor.left(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()



###---------------BOTTOM ROW----------------###
#x = ((-150, -50), (-50, 50), (50, 150))
#y = -50

#X in bottom left square
taylor.goto(-150, -50) #left corner
taylor.setheading(90)
taylor.right(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

taylor.goto(-50, -50) #right corner
taylor.setheading(90)
taylor.left(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()


#X in bottom center square
taylor.goto(-50, -50) #left corner
taylor.setheading(90)
taylor.right(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

taylor.goto(50, -50) #right corner
taylor.setheading(90)
taylor.left(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

#X in bottom right square
taylor.goto(50, -50) #left corner
taylor.setheading(90)
taylor.right(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

taylor.goto(150, -50) #right corner
taylor.setheading(90)
taylor.left(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()


###---------------CENTER ROW----------------###
#x = ((-150, -50), (-50, 50), (50, 150))
#y = 50

#X center left square
taylor.goto(-150, 50) #left corner
taylor.setheading(90)
taylor.right(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

taylor.goto(-50, 50) #right corner
taylor.setheading(90)
taylor.left(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()


#X in center square
taylor.goto(-50, 50) #left corner
taylor.setheading(90)
taylor.right(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

taylor.goto(50, 50) #right corner
taylor.setheading(90)
taylor.left(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()


#X in center right square
taylor.goto(50, 50) #left corner
taylor.setheading(90)
taylor.right(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()

taylor.goto(150, 50) #right corner
taylor.setheading(90)
taylor.left(135)
taylor.forward(10)
taylor.pendown()
taylor.forward(120)
taylor.penup()
'''









#Get the Current Coordinates of the turtle
where = taylor.pos()

#Set drawing color
taylor.color('#8d024a')

#Write out current coordinates
taylor.write(str(where) + "  ", align="left", font=("Handlee", 20))

window.exitonclick()