import turtle
import config
import random
import string
from math import floor
from tkinter.messagebox import askyesno
from tkinter import *
from tkinter.ttk import *
import Controls
import Player
import Maps


def generateId():
    strings = string.ascii_lowercase
    return ''.join(random.choice(strings) for _ in range(8))


def getLevel():
    divisible = 100 % config.score
    if (divisible == 100):
        config.level += 1


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
            elif (value == "$"):
                drawSquare(x, y, side, "orange")
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
    textbox.shapesize(stretch_wid=10, stretch_len=20)
    textbox.penup()
    textbox.goto(X, Y)
    textbox.stamp()
    textbox.color('black')
    # center vertically based on font size
    if (count >= 2):
        textbox.goto(X, Y - FONT_SIZE/.275)
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


def drawScoreInfoBox():
    FONT_SIZE = 16
    FONT = ('Courier', FONT_SIZE, 'bold')
    X = 160
    Y = -180

    textbox = turtle.Turtle()
    textbox.hideturtle()
    textbox.color('grey')
    textbox.shape('square')
    textbox.shapesize(stretch_wid=5, stretch_len=10)
    textbox.penup()
    textbox.goto(X, Y)
    textbox.stamp()
    textbox.color('black')
    # center vertically based on font size
    textbox.goto(X, Y - FONT_SIZE/2)
    textbox.write("Score: " + "\n" + str('Level: %s' %
                  getLevel()), align='center', font=FONT)
    turtle.update()


def drawScoreInfoBox():
    FONT_SIZE = 16
    FONT = ('Courier', FONT_SIZE, 'bold')
    X = 495
    Y = 400

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
    textbox.goto(X, Y - FONT_SIZE/.9)
    textbox.write("Score: %s" % config.score + "\n" + "Level: %s" %
                  config.level, align='center', font=FONT)
    turtle.update()


def checkWin():
    if (config.nextTile == '3'):
        config.map += 1
        Maps.openMap(config.map)


def checkItemLocation():
    if (config.itemDrops):
        items = config.itemDrops
        for i in range(len(items)):
            if (items[i]['position'] == config.nextPosition):
                return {'item': items[i]['item'], 'exists': True}

    return False


def checkTreasure():
    exists = checkItemLocation()

    if (config.nextTile == '$' and not bool(exists)):
        dropOptions = ['weapon', 'gold']
        weaponsList = config.weapons
        randomDrop = random.choices(
            dropOptions, weights=(20, 80), k=1)[0]
        if (randomDrop == 'weapon'):
            weaponsListLen = len(weaponsList)

            def divideWeights():
                MAX = 100
                KNUCKS = 60
                remainder = MAX - KNUCKS
                lengthRange = weaponsListLen-1
                results = []
                total = remainder
                for i in range(lengthRange):
                    if (i == lengthRange-1):
                        results.append(remainder)
                    elif (i == 0):
                        results.append(KNUCKS)
                    else:
                        left = floor(remainder / 1.75)
                        remainder -= left
                        total += left
                        results.append(left)
                return results
            weights = divideWeights()
            availableWeapons = weaponsList[1:]
            randomWeapon = random.choices(
                availableWeapons, weights=tuple(weights), k=1)[0]
            drop = randomWeapon
            drop['condition'] = random.randint(30, 100)
            drop['id'] = generateId()
            dropItem = {
                "item": drop,
                "position": config.nextPosition
            }
            config.itemDrops.append(dropItem)
            showItemPickupPrompt(drop, False)

        elif (randomDrop == 'gold'):
            amount = random.randint(1, 10)
            item = {
                'name': 'gold',
                'value': amount
            }
            Controls.pickup(item)
    else:
        showItemPickupPrompt(exists['item'], exists['exists'])


def dropTreasure():
    config.myarr[config.nextPosition[0]][config.nextPosition[1]] = '$'


def showAttackPrompt(baddieInfo):
    answer = askyesno(title='Attack?', message=baddieInfo["name"] + ' with HP ' + str(
        baddieInfo["hp"]) + '\nDo you want to attack?')
    if (answer):
        config.attackState = 'war'


def showItemPickupPrompt(item, exists=False,):
    def printItemInfo():
        return(
            'Pick Up? \n\n' +
            str(item['name']) + '\n' +
            'Condition: ' + str(item['condition']) + '\n'
        )

    answer = askyesno(title='Pick up?',
                      message=printItemInfo()
                      )
    if (answer):
        Controls.pickup({"name": "weapon", "item": item})
    else:
        if (not exists):
            print('did not pick up drops', config.itemDrops)


def getWeaponData(weapon):
    match = [x for x in config.weapons if x['code_name'] == weapon]
    return match[0]


def showInventory():

    FONT_SIZE = 16
    FONT = ('Courier', FONT_SIZE, 'bold')
    root = Tk()
    root.title('Inventory')
    root.geometry("250x200")
    root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
    root.config(background='grey', width=200, height=150)
    var = IntVar(root)
    label = Label(root, font=FONT)

    def handleSelection(event=None):
        inventoryItem = inventory[var.get()]
        config.player['weapon']['name'] = inventoryItem['name']
        config.player['weapon']['damage'] = getWeaponData(
            inventoryItem['code_name'])['damage']
        config.player['weapon']['condition'] = inventoryItem['condition']
        turtle.clear()
        drawMap()
        drawInfoBox(Player.printPlayerData())
        root.destroy()

    def handleCancelSelection():
        root.destroy()

    root.bind('<Return>', handleSelection)
    inventory = config.inventory

    if (config.inventory):
        for i in range(len(inventory)):
            Radiobutton(root, text=str(inventory[i]['name'] + '\n' + 'Condition: ' +
                                       str(inventory[i]['condition'])), variable=var,
                        value=i).pack(anchor=W)
    else:
        Label(root, text='Inventory is empty', font=FONT).pack()

    if (config.inventory):
        B1 = Button(root, text="OK", command=handleSelection)
        B1.bind('<Return>', handleSelection)
        B1.pack(anchor=W, side=BOTTOM)

    B2 = Button(root, text="Cancel", command=handleCancelSelection)
    B2.pack(anchor=W, side=BOTTOM)
    label.pack()
