import turtle
import config
import Functions
import Enemy
import Player


def infoBoxDefault():
    Functions.drawInfoBox(Player.printPlayerData())


def baddieInfoBoxDefault():
    Functions.drawBaddieInfoBox('')


def setCurrentPosition(row, col):
    config.currentPosition = [row, col]


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
    setCurrentPosition(config.row, config.col)
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
    print('attack')
    thisBaddie = baddie
    weaponDamage = config.player['weapon']['damage']
    print(weaponDamage)
    Functions.drawBaddieInfoBox(
        str(baddie["name"]) + "\n" + "HP: " + str(baddie["hp"]))

    def baddieDead():
        Functions.drawBaddieInfoBox(thisBaddie["name"] + " is dead")
        Functions.dropTreasure()
        config.attackState = 'peaceful'
        turtle.clear()
        Functions.drawMap()

    if (config.attackState == 'peaceful'):
        Functions.showAttackPrompt(thisBaddie)

    if (config.attackState == 'war'):
        if (thisBaddie["hp"] <= 0):
            baddieDead()
        elif(thisBaddie["hp"] > 0):
            thisBaddie["hp"] -= weaponDamage
            print("baddie hp", thisBaddie["hp"])
            Functions.drawBaddieInfoBox(
                str(thisBaddie["name"]) + "\n" + "HP: " + str(thisBaddie["hp"]))
            if (baddie["hp"] <= 0):
                baddieDead()


def equip():
    print('equip')
    Functions.showInventory()


def pickup(item):
    print('pickup', item)
    if (item['name'] == 'gold'):
        config.gold += item['value']
    elif (item['name'] == 'weapon'):
        index = next((index for (index, d) in enumerate(
            config.itemDrops) if d['item']["id"] == item['item']['id']), None)
        del config.itemDrops[index]
        print('itemDrops pickup', config.itemDrops)
        config.inventory.append(item['item'])
        # remove from itemDrops
        index = next((index for (index, d) in enumerate(
            config.itemDrops) if d['item']["id"] == item['item']['id']), None)
        if (index != None):
            del config.itemDrops[index]
        print('itemDrops pickup', config.itemDrops)
    config.myarr[config.nextPosition[0]][config.nextPosition[1]] = '0'
    print('position',
          config.nextPosition)
    turtle.clear()
    Functions.drawMap()
    Functions.drawBaddieInfoBox('picked up %s' % item['name'])
    Functions.drawInfoBox(Player.printPlayerData())
