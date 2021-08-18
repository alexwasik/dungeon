import turtle
import config
import Controls
import Maps

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
screen.bgcolor(config.bgcolor)

turtle.hideturtle()

Maps.openMap()

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
