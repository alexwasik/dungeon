import turtle
import config
import Functions
import Enemy
import Player


def infoBoxDefault():
    Functions.drawInfoBox(Player.printPlayerData())


def baddieInfoBoxDefault():
    Functions.drawBaddieInfoBox('')


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
        baddieInfoBoxDefault()
    elif (config.myarr[config.row - 1][config.col] == '$'):
        Functions.checkTreasure()
    else:
        Functions.checkWin()
        Enemy.checkEnemy()


def down():
    config.nextTile = config.myarr[config.row + 1][config.col]
    config.nextPosition = [config.row+1, config.col]
    if (config.myarr[config.row + 1][config.col] == '0'):
        config.myarr[config.row][config.col] = '0'
        config.row += 1
        config.myarr[config.row][config.col] = '1'
        turtle.clear()
        Functions.drawMap()
        infoBoxDefault()
        baddieInfoBoxDefault()
    elif (config.myarr[config.row + 1][config.col] == '$'):
        Functions.checkTreasure()
    else:
        Functions.checkWin()
        Enemy.checkEnemy()


def left():
    config.nextTile = config.myarr[config.row][config.col - 1]
    config.nextPosition = [config.row, config.col - 1]
    if (config.myarr[config.row][config.col - 1] == '0'):
        config.myarr[config.row][config.col] = '0'
        config.col -= 1
        config.myarr[config.row][config.col] = '1'
        turtle.clear()
        Functions.drawMap()
        infoBoxDefault()
        baddieInfoBoxDefault()
    elif (config.myarr[config.row][config.col - 1] == '$'):
        Functions.checkTreasure()
    else:
        Functions.checkWin()
        Enemy.checkEnemy()


def right():
    config.nextTile = config.myarr[config.row][config.col + 1]
    config.nextPosition = [config.row, config.col + 1]
    if (config.myarr[config.row][config.col+1] == '0'):
        config.myarr[config.row][config.col] = '0'
        config.col += 1
        config.myarr[config.row][config.col] = '1'
        turtle.clear()
        Functions.drawMap()
        infoBoxDefault()
        baddieInfoBoxDefault()
    elif (config.myarr[config.row][config.col + 1] == '$'):
        Functions.checkTreasure()
    else:
        Functions.checkWin()
        Enemy.checkEnemy()


def attack(baddie):
    thisBaddie = baddie
    weaponDamage = config.player['weapon']['damage']
    Functions.drawBaddieInfoBox(
        str(baddie["name"]) + "\n" + "HP: " + str(baddie["hp"]))

    def baddieDead():
        Functions.dropTreasure()
        config.attackState = 'peaceful'
        config.score += 5
        turtle.clear()
        Functions.drawMap()
        Functions.getLevel()
        Functions.drawScoreInfoBox()
        Functions.drawBaddieInfoBox(thisBaddie["name"] + " is dead")

    if (config.attackState == 'peaceful'):
        Functions.showAttackPrompt(thisBaddie)

    if (config.attackState == 'war'):
        if (thisBaddie["hp"] <= 0):
            baddieDead()
        elif(thisBaddie["hp"] > 0):
            thisBaddie["hp"] -= weaponDamage
            Functions.drawBaddieInfoBox(
                str(thisBaddie["name"]) + "\n" + "HP: " + str(thisBaddie["hp"]))
            if (baddie["hp"] <= 0):
                baddieDead()
        config.player['weapon']['condition'] -= 1
        Functions.drawInfoBox(Player.printPlayerData())


def equip():
    Functions.showInventory()


def pickup(item):
    if (item['name'] == 'gold'):
        config.gold += item['value']
    elif (item['name'] == 'weapon'):
        index = next((index for (index, d) in enumerate(
            config.itemDrops) if d['item']["id"] == item['item']['id']), None)
        if (index != None):
            del config.itemDrops[index]
            config.inventory.append(item['item'])
    config.myarr[config.nextPosition[0]][config.nextPosition[1]] = '0'
    turtle.clear()
    Functions.drawMap()
    Functions.drawBaddieInfoBox('picked up %s' % item['name'])
    Functions.drawInfoBox(Player.printPlayerData())
