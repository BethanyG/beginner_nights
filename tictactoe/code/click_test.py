import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")


def h1(x, y):
    tess.goto(x, y)


wn.onclick(h1)
tess.forward(100)
tess.circle(100)
tess.backward(50)
tess.circle(40)
tess.backward(50)
tess.circle(40)
tess.backward(100)
tess.circle(100)
tess.right(90)
tess.forward(100)
tess.circle(100)
wn.mainloop()