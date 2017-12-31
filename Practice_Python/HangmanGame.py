import turtle
BG = turtle.Screen()
BG.bgcolor("lightgreen")
BG.title("Hangnam Game")


def draw_frame():
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
    frame.circle(35)


def question_format():
    word = turtle.Turtle()
    word.hideturtle()
    word.penup()
    word.goto(200, 220)
    word.color("blue")
    word.write("Question: Who is Tri currently have a crush on right now?", move=False, align="right", font=("Time New Roman", 15, "normal"))


def first_spot():
    first = turtle.Turtle()


def text_input():
    x = ""
    turtle.textinput("Letter go here: ", x)
    if(x == "N"):

    else if (x ==  "G")

    else if(x == "A")

draw_frame()
question_format()
BG.mainloop()





