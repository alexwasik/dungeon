import turtle
import config
from tkinter.messagebox import askyesno


def drawSquare(x, y, side, color):
    turtle.up()
    turtle.goto(x, y)
    if (not color == 'none'):
        turtle.color(color)
        turtle.begin_fill()
        for x in range(4):
            turtle.forward(side)
            turtle.right(90)
        turtle.end_fill()


def drawMap():
    x = -400
    y = 300
    originalX = -400
    side = 20

    turtle.tracer(0, 0)
    for arr in config.myarr:
        for value in arr:
            if (value == '0'):
                drawSquare(x, y, side, "black")
            elif (value == "1"):
                drawSquare(x, y, side, "yellow")
            elif (value == "2"):
                drawSquare(x, y, side, "white")
            elif (value == "3"):
                drawSquare(x, y, side, "blue")
            elif (value == "\n"):
                drawSquare(x, y, side, "none")
            else:
                drawSquare(x, y, side, "red")
            x += side
        y -= side
        x = originalX
    turtle.update()


def drawInfoBox(info):
    FONT_SIZE = 16
    FONT = ('Courier', FONT_SIZE, 'bold')
    X = -300
    Y = -180
    count = 0
    for i in info:
        if i == '\n':
            count += 1

    textbox = turtle.Turtle()
    textbox.hideturtle()
    textbox.color('grey')
    textbox.shape('square')
    textbox.shapesize(stretch_wid=5, stretch_len=20)
    textbox.penup()
    textbox.goto(X, Y)
    textbox.stamp()
    textbox.color('black')
    # center vertically based on font size
    if (count >= 2):
        textbox.goto(X, Y - FONT_SIZE/.3)
    else:
        textbox.goto(X, Y - FONT_SIZE/2)
    textbox.write(info, align='center', font=FONT)
    turtle.update()


def drawBaddieInfoBox(baddieInfo):
    FONT_SIZE = 16
    FONT = ('Courier', FONT_SIZE, 'bold')
    X = 160
    Y = -180

    textbox = turtle.Turtle()
    textbox.hideturtle()
    textbox.color('grey')
    textbox.shape('square')
    textbox.shapesize(stretch_wid=5, stretch_len=20)
    textbox.penup()
    textbox.goto(X, Y)
    textbox.stamp()
    textbox.color('black')
    # center vertically based on font size
    textbox.goto(X, Y - FONT_SIZE/2)
    textbox.write(baddieInfo, align='center', font=FONT)
    turtle.update()


def checkWin():
    if (config.nextTile == '3'):
        print("You Win")
        turtle.bye()


def showAttackPrompt(baddieInfo):
    answer = askyesno(title='Attack?', message=baddieInfo["name"] + ' with HP ' + str(
        baddieInfo["hp"]) + '\nDo you want to attack?')
    if (answer):
        config.attackState = 'war'
