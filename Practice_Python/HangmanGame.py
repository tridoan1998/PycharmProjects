import turtle

#class MyTurtle(turtle.Turtle):
 #   def __init__(self, )
BG = turtle.Screen()
BG.bgcolor("lightgreen")

BG.title("Hangnam Game")


turtle.write("Hello", move=False, align="right", font=("Time New Roman", 15, "normal"))

#BG.delay(50)

frame = turtle.Turtle()
frame.left(90)
frame.forward(270)
frame.right(90)
frame.forward(180)
frame.right(90)
frame.forward(70)
frame.right(90)
frame.circle(40 )
BG.exitonclick()                # wait for a user click on the canvas

