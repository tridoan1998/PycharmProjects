import turtle

BG = turtle.Screen()
BG.bgcolor("lightgreen")
BG.title("Hangnam Game")

frame = turtle.Turtle()
frame.hideturtle()
frame.color("blue", "red")
frame.pensize(2)
frame.penup()
frame.goto(-300,-100)
frame.pendown()
frame.begin_fill()
frame.left(90)
frame.forward(270)
frame.right(90)
frame.forward(180)
frame.right(90)
frame.forward(70)
frame.right(90)
frame.circle(40)

turtle.write("Hello", move=False, align="right", font=("Time New Roman", 15, "normal"))

#def frame_draw(frame):



BG.exitonclick()                # wait for a user click on the canvas

