import turtle
import random
import numpy as np
from tkinter.messagebox import askyesno

turtle.screensize(1000, 500)

myarr = []
col = 1
row = 1
nextTile = 0
nextPosition = [0, 0]
attackState = 'peaceful'
baddie1 = {
    "type": "baddie",
    "name": "Baddie 1",
    "hp": 5,
    "position": {
        "x": 0,
        "y": 0
    },
}
baddie2 = {
    "type": "baddie",
    "name": "Baddie 2",
    "hp": 6,
    "position": {
        "x": 0,
        "y": 0
    },
}
player = {
    "type": "player",
    "hp": 10,
    "position": {
        "x": 0,
        "y": 0
    },
}

turtle.hideturtle()

f = open('map.txt', 'r')

while(True):
    tempLine = f.readline()
    print(tempLine)

    if tempLine == "":
        break

    temparr = []
    for t in tempLine:
        temparr.append(t)

    myarr.append(temparr)

f.close()


def populateBaddies():
    global myarr
    global baddie1
    global baddie2

    numBaddies = random.randint(1, 3)
    print('numBaddies', numBaddies)
    numArrays = len(myarr)

    r1 = random.randint(1, numArrays-2)
    r2 = random.randint(1, numArrays-2)

    indices1 = [i for i, x in enumerate(myarr[r1]) if x == "0"]
    indices2 = [i for i, x in enumerate(myarr[r2]) if x == "0"]
    randIndex1 = random.choice(indices1)
    randIndex2 = random.choice(indices2)

    myarr[r1][randIndex1] = "@"
    baddie1["position"]["x"] = r1
    baddie1["position"]["y"] = randIndex1

    myarr[r2][randIndex2] = "@"
    baddie2["position"]["x"] = r2
    baddie2["position"]["y"] = randIndex2


populateBaddies()


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
    x = -300
    y = 60
    originalX = -300
    side = 30

    turtle.tracer(0, 0)
    for arr in myarr:
        for value in arr:
            if (value == '0'):
                drawSquare(x, y, side, "green")
            elif (value == "1"):
                drawSquare(x, y, side, "yellow")
            elif (value == "2"):
                drawSquare(x, y, side, "red")
            elif (value == "3"):
                drawSquare(x, y, side, "blue")
            elif (value == "\n"):
                drawSquare(x, y, side, "none")
            else:
                drawSquare(x, y, side, "black")
            x += side
        y -= side
        x = originalX
    turtle.update()


drawMap()


def up():
    global myarr
    global row
    global col
    global nextTile
    global nextPosition

    nextTile = myarr[row-1][col]
    nextPosition = [row-1, col]
    if (myarr[row-1][col] == '0'):
        myarr[row][col] = '0'
        row -= 1
        myarr[row][col] = '1'
        turtle.clear()
        drawMap()
    else:
        checkWin()
        checkEnemy()


def down():
    global myarr
    global row
    global col
    global nextTile
    global nextPosition

    nextTile = myarr[row+1][col]
    nextPosition = [row+1, col]
    if (myarr[row+1][col] == '0'):
        myarr[row][col] = '0'
        row += 1
        myarr[row][col] = '1'
        turtle.clear()
        drawMap()
    else:
        checkWin()
        checkEnemy()


def left():
    global myarr
    global row
    global col
    global nextTile
    global nextPosition

    nextTile = myarr[row][col-1]
    nextPosition = [row, col-1]
    if (myarr[row][col-1] == '0'):
        myarr[row][col] = '0'
        col -= 1
        myarr[row][col] = '1'
        turtle.clear()
        drawMap()
    else:
        checkWin()
        checkEnemy()


def right():
    global myarr
    global row
    global col
    global nextTile
    global nextPosition

    nextTile = myarr[row][col+1]
    nextPosition = [row, col+1]
    if (myarr[row][col+1] == '0'):
        myarr[row][col] = '0'
        col += 1
        myarr[row][col] = '1'
        turtle.clear()
        drawMap()
    else:
        checkWin()
        checkEnemy()


def checkWin():
    if (nextTile == '3'):
        print("You Win")
        turtle.bye()


def checkEnemy():
    if (nextTile == '@'):
        print('baddie ahead')
        baddie1Position = []
        baddie2Position = []
        for key, value in baddie1["position"].items():
            print(key, value)
            baddie1Position.append(value)
        print('baddie1', baddie1Position)
        for key, value in baddie2["position"].items():
            print(key, value)
            baddie2Position.append(value)
        print('baddie2', baddie2Position)

        if (np.array_equal(baddie1Position, nextPosition)):
            print('baddie in position')
            attack(baddie1)
        elif (np.array_equal(baddie2Position, nextPosition)):
            print('baddie in position')
            attack(baddie2)


def attack(baddie):
    global baddie1
    global baddie2

    print('attack')

    def baddieDead():
        global attackState
        global myarr

        print(baddie["name"] + " is dead")
        myarr[nextPosition[0]][nextPosition[1]] = '0'
        attackState = 'peaceful'
        turtle.clear()
        drawMap()

    if (attackState == 'peaceful'):
        showAttackPrompt(baddie)

    if (attackState == 'war'):
        if (baddie["hp"] == 0):
            baddieDead()
        elif(baddie["hp"] > 0):
            baddie["hp"] -= 1
            print("baddie hp", baddie["hp"])
            if (baddie["hp"] == 0):
                baddieDead()


def showAttackPrompt(baddieInfo):
    global attackState

    answer = askyesno(title='Attack?', message=baddieInfo["name"] + ' with HP ' + str(
        baddieInfo["hp"]) + '\nDo you want to attack?')
    if (answer):
        attackState = 'war'


turtle.onkey(up, 'Up')
turtle.onkey(left, 'Left')
turtle.onkey(down, 'Down')
turtle.onkey(right, 'Right')
turtle.onkey(attack, 'a')

turtle.listen()
turtle.mainloop()
