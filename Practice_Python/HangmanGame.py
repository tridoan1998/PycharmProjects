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
    first.hideturtle()
    first.penup()
    first.goto(200, -100)
    first.left(10)



def text_input():
    spot1 = ""
    spot2 = ""
    spot3 = ""
    x = ""
    done = False
    while done:
        turtle.textinput("Letter go here: ", x)
        if x == "N":
            spot1 = "N"
        if x == "G":
            spot2 = "G"
        if x == "A":
            spot3 = "A"
        if spot1 == "N" and spot2 == "G" and spot3 == "A":
            done = True
        else:
            continue

draw_frame()
question_format()
first_spot()
BG.mainloop()





