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
    word.goto(310, 220)
    word.color("blue")
    word.write("Question: Who is Tri currently have a crush on right now?", move=False, align="right", font=("Time New Roman", 15, "normal"))


def first_spot():
    first = turtle.Turtle()
    first.hideturtle()
    first.color("black")
    first.pensize(6)
    first.penup()
    first.goto(100, 100)
    first.pendown()
    first.begin_fill()
    first.forward(30)


def got_first_spot_right():
    word = turtle.Turtle()
    word.hideturtle()
    word.penup()
    word.goto(100, 130)
    word.color("red")
    word.write("N", move=False, align="right", font=("Time New Roman", 15, "normal"))

answer = "NGA"

def text_input():
    x = ""
    answer = "NGA"
    turtle.textinput("Enter the letter here: ", x)
    if x == answer[0]:
        print("sdfdsf")
        spot1 = "N"
        got_first_spot_right()
    elif x == answer[1]:
        spot2 = "G"
    elif x == answer[2]:
        spot3 = "A"
    else
        cint


draw_frame()
ScrolledText.frame

    question_format()
first_spot()
text_input()

BG.mainloop()





