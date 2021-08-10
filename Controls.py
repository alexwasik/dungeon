import turtle
import config
import Functions
import Enemy


def infoBoxDefault():
    Functions.drawInfoBox('you are alive')


def up():
    config.nextTile = config.myarr[config.row - 1][config.col]
    config.nextPosition = [config.row - 1, config.col]
    if (config.myarr[config.row - 1][config.col] == '0'):
        config.myarr[config.row][config.col] = '0'
        config.row -= 1
        config.myarr[config.row][config.col] = '1'
        turtle.clear()
        Functions.drawMap()
        infoBoxDefault()
    else:
        Functions.checkWin()
        Enemy.checkEnemy()


def down():
    config.nextTile = config.myarr[config.row+1][config.col]
    config.nextPosition = [config.row+1, config.col]
    if (config.myarr[config.row+1][config.col] == '0'):
        config.myarr[config.row][config.col] = '0'
        config.row += 1
        config.myarr[config.row][config.col] = '1'
        turtle.clear()
        Functions.drawMap()
        infoBoxDefault()
    else:
        Functions.checkWin()
        Enemy.checkEnemy()


def left():
    config.nextTile = config.myarr[config.row][config.col-1]
    config.nextPosition = [config.row, config.col-1]
    if (config.myarr[config.row][config.col-1] == '0'):
        config.myarr[config.row][config.col] = '0'
        config.col -= 1
        config.myarr[config.row][config.col] = '1'
        turtle.clear()
        Functions.drawMap()
        infoBoxDefault()
    else:
        Functions.checkWin()
        Enemy.checkEnemy()


def right():
    config.nextTile = config.myarr[config.row][config.col+1]
    config.nextPosition = [config.row, config.col+1]
    if (config.myarr[config.row][config.col+1] == '0'):
        config.myarr[config.row][config.col] = '0'
        config.col += 1
        config.myarr[config.row][config.col] = '1'
        turtle.clear()
        Functions.drawMap()
        infoBoxDefault()
    else:
        Functions.checkWin()
        Enemy.checkEnemy()


def attack(baddie):
    print('attack')
    thisBaddie = baddie
    Functions.drawInfoBox(
        str(baddie["name"]) + "\n" + "HP: " + str(baddie["hp"]))

    def baddieDead():
        config.myarr[config.nextPosition[0]][config.nextPosition[1]] = '0'
        config.attackState = 'peaceful'
        turtle.clear()
        Functions.drawMap()
        Functions.drawInfoBox(thisBaddie["name"] + " is dead")

    if (config.attackState == 'peaceful'):
        Functions.showAttackPrompt(thisBaddie)

    if (config.attackState == 'war'):
        if (thisBaddie["hp"] == 0):
            baddieDead()
        elif(thisBaddie["hp"] > 0):
            thisBaddie["hp"] -= 1
            print("baddie hp", thisBaddie["hp"])
            Functions.drawInfoBox(
                str(thisBaddie["name"]) + "\n" + "HP: " + str(thisBaddie["hp"]))
            if (baddie["hp"] == 0):
                baddieDead()
