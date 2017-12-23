import turtle

BG = turtle.Screen()
BG.bgcolor("crimson")

tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(4)                 # set the width of her pen

turtle.write("Hello", move=False, align="left", font=("Arial", 8, "normal"))

tess.forward(50)
#tess.left(120)

BG.exitonclick()                # wait for a user click on the canvas

