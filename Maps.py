import turtle
import config
import Functions
import Enemy
import Player


def setNewPosition():
    found = False
    for i in range(len(config.myarr)):
        print('i' + str(i))
        for idx, item in enumerate(config.myarr[i]):
            print('item' + str(item), 'idx' + str(idx))
            if item == '1':
                print(i, str(idx))
                config.row = i
                config.col = idx
                found = True
                break
        if found:
            break


def openMap(mapNum=0):
    config.myarr = []
    turtle.clear()
    f = open('maps/map%s' % mapNum + '.txt', 'r')

    while(True):
        tempLine = f.readline()

        if tempLine == "":
            break

        temparr = []
        for t in tempLine:
            temparr.append(t)

        config.myarr.append(temparr)

    f.close()
    setNewPosition()
    Functions.drawMap()
    Enemy.populateBaddies()
    Functions.drawScoreInfoBox()
    Functions.drawInfoBox(Player.printPlayerData())
    Functions.drawBaddieInfoBox('')
