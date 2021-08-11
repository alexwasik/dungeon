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

f = open('map.txt', 'r')

while(True):
    tempLine = f.readline()

    if tempLine == "":
        break

    temparr = []
    for t in tempLine:
        temparr.append(t)

    config.myarr.append(temparr)

f.close()


Enemy.populateBaddies()
Functions.drawMap()
Functions.drawInfoBox(Player.printPlayerData())
Functions.drawBaddieInfoBox('')


turtle.onkey(Controls.up, 'Up')
turtle.onkey(Controls.left, 'Left')
turtle.onkey(Controls.down, 'Down')
turtle.onkey(Controls.right, 'Right')
turtle.onkey(Controls.attack, 'a')

turtle.listen()
turtle.mainloop()
