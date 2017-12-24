import turtle

#class MyTurtle(turtle.Turtle):
 #   def __init__(self, )
BG = turtle.Screen()
BG.bgcolor("crimson")


turtle.write("Hello", move=False, align="left", font=("Arial", 8, "normal"))

turtle.circle(40)
turtle.down()
turtle.right(90)
turtle.forward(30)
BG.exitonclick()                # wait for a user click on the canvas

