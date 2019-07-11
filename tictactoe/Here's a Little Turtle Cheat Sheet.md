### Here's a Little Turtle Cheat Sheet
________________________________________________



-  **Get started: ** `import turtle`
-  **Make a new turtle & give it a name (e.g, _taylor_):  ** `taylor = turtle.Turtle()`
-  **Pick a shape for the turtle cursor: ** `turtle.shape('turtle')`   
  (_you can choose from  “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”_)
_____________________________________________________
-  **Adjust visibility:**  `turtle.hideturtle()` & ` turtle.showturtle()`
-  **Adjust speed:  **`turtle.delay(0)` & `turtle.speed(0)` (_1=slowest, 10=fastest, 0=ASAP_)
-  **Move _without_ drawing:  **`turtle.penup()`
-  **Draw _while_ moving:  **`turtle.pendown()`
_____________________________________________________
-  **Change the pen color: **`turtle.pencolor("blue")` (_you can use, HEX, RGB, or name_)
-  **Change the pen size: **`turtle.pensize(10)` (_1=smallest, 10=largest_)
-  **Change the fill color: **`turtle.fillcolor('#ed4ecd')`
-  **Fill in a shape:  ** `turtle.fill(True)` (_fills object with same color as pen while drawing_)
______________________________________________________
-  **Draw a line, _x pixels long_: ** `turtle.forward(x)` & `turtle.back(x)`
-  **Make a dot of x size: ** `turtle.dot(x)` (_1=smallest, 10=largest_)
-  **Draw a circle, with _radius of x pixels_: **  `turtle.circle(x)`
-  **Draw a semi-circle with radius x & arc y: **`turtle.circle(x, y)`  
-  **Repeat a turtle pattern over & over:  ** `turtle.stamp()`
-  **Print a text message to screen:  ** `turtle.write("My message")`
_______________________________________________________
-  **Send the turtle to center of the screen (0,0): **`turtle.home( )`
-  **Send the turtle to an (x,y) coordinate: ** `turtle.goto(x, y)`
-  **Point the turtle at x angle: **`turtle.setheading(270)`
   (_common directions: 0 (east), 90 (north), 180 (west), 270 (south)_)
-  **Make a turn by x degrees: **`turtle.right(x)` & `turtle.left(x)`
________________________________________________________
-  **Erase stamp by stampid:  ** `turtle.clearstamp(stampid)`
-  **Undo last action:  ** `turtle.undo()`
-  **Erase everything & start over:  **`turtle.reset()`
-  **Close the turtle window and exit the turtle program:  ** `turtle.bye()`