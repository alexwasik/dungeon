import turtle
import config
import Functions
import Controls
import Enemy
import Player

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
screen.bgcolor(config.bgcolor)

turtle.hideturtle()


def openMap(mapNum=0):
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


openMap()
Enemy.populateBaddies()
Functions.drawMap()
Functions.drawScoreInfoBox()
Functions.drawInfoBox(Player.printPlayerData())
Functions.drawBaddieInfoBox('')


# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)


turtle.onkey(Controls.up, 'Up')
turtle.onkey(Controls.left, 'Left')
turtle.onkey(Controls.down, 'Down')
turtle.onkey(Controls.right, 'Right')
turtle.onkey(Controls.equip, 'e')

turtle.listen()
turtle.mainloop()
