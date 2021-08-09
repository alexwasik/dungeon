import turtle;

myarr = []
col = 1
row = 1
turtle.hideturtle()

f = open('map.txt', 'r')

while(True):
  tempLine = f.readline()

  if tempLine == "":
    break

  temparr = []
  for t in tempLine:
    temparr.append(t)

  myarr.append(temparr)


f.close()

def drawSquare(x, y, side, color):
  turtle.up()
  turtle.goto(x,y)
  if (not color == 'none'):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(4):
      turtle.forward(side)
      turtle.right(90)
    turtle.end_fill()

def drawMap():
  x = -120
  y = 60
  originalX = -120
  side = 10

  turtle.tracer(0,0)
  for arr in myarr:
    for value in arr:
      if (value == '0'):
        drawSquare(x, y, side, "green")
      elif (value == "1"):
        drawSquare(x, y, side, "yellow")
      elif (value == "2"):
        drawSquare(x, y, side, "red")
      elif (value == "\n"):
        drawSquare(x, y, side, "none")
      else:
        drawSquare(x, y, side, "black")
      x+=side
    y-=side
    x = originalX
  turtle.update()

drawMap()

def up():
  global myarr
  global row
  global col

  if (myarr[row-1][col] == '0'):
    myarr[row][col] = '0'
    row -= 1
    myarr[row][col] = '1'
  turtle.clear()
  drawMap()

def down():
  global myarr
  global row
  global col

  if (myarr[row+1][col] == '0'):
    myarr[row][col] = '0'
    row += 1
    myarr[row][col] = '1'
  turtle.clear()
  drawMap()

def left():
  global myarr
  global row
  global col

  if (myarr[row][col-1] == '0'):
    myarr[row][col] = '0'
    col -= 1
    myarr[row][col] = '1'
  turtle.clear()
  drawMap()

def right():
  global myarr
  global row
  global col

  if (myarr[row][col+1] == '0'):
    myarr[row][col] = '0'
    col += 1
    myarr[row][col] = '1'
  turtle.clear()
  drawMap()

turtle.onkey(up, 'w')
turtle.onkey(left, 'a')
turtle.onkey(down, 's')
turtle.onkey(right,'d')

turtle.listen()
turtle.mainloop()  
