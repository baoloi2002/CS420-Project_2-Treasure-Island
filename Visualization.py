
# import turtle library
import turtle
import random

# mountain draw
def mountainDraw(i, j):
    x = j*boxW + leftCorner
    y = topCorner - i*boxH
    xx = x + boxW-1
    yy = y - boxH+1
    turtle.pensize(2)

    turtle.penup()
    turtle.setposition(x, y)    
    turtle.color("#000000")    
    turtle.pendown()    
    turtle.goto(xx, yy)

    turtle.penup()
    turtle.setposition(x, yy)
    turtle.pendown()
    turtle.goto(xx, y)

    turtle.pensize(1)

# treasure Draw
def treasureDraw(i, j):
    x = j*boxW + leftCorner
    y = topCorner - i*boxH
    xx = x + boxW-1
    yy = y - boxH+1
    midx = (x+xx)//2
    midy = (y+yy)//2
    turtle.penup()
    turtle.setposition(midx, midy)
    turtle.pendown()
    r = min(xx-x, y-yy)
    size = [r-1, r//2, r//4]
    c = ["#FF0000", "#00FF00", "#0000FF"]
    for u in range(3):
        turtle.dot(size[u], c[u])

# prison Draw
def prisonDraw(i, j):
    x = j*boxW + leftCorner
    y = topCorner - i*boxH
    xx = x + boxW-1
    yy = y - boxH+1
    turtle.pensize(5)

    turtle.penup()
    turtle.setposition((x+xx)//2, y)    
    turtle.color("#000000")    
    turtle.pendown()    
    turtle.goto((x+xx)//2, yy)

    turtle.penup()
    turtle.setposition(x, (y+yy)//2)
    turtle.pendown()
    turtle.goto(xx, (y+yy)//2)

    turtle.pensize(1)

# boundary draw
def boundaryDraw(i, j):
    x = j*boxW + leftCorner
    y = topCorner - i*boxH
    xx = x + boxW-1
    yy = y - boxH+1
    turtle.penup()
    turtle.setposition(x, y)    
    if boundaryMap[i][j] == 1:
        turtle.color("#FF0000")
    else:
        turtle.color("#000000")
    turtle.pendown()
    turtle.goto(x, yy)
    turtle.goto(xx, yy)
    turtle.goto(xx, y)
    turtle.goto(x, y)

# land draw
def regionDraw(i, j):
    x = j*boxW + leftCorner
    y = topCorner - i*boxH
    xx = x + boxW-1
    yy = y - boxH+1
    turtle.penup()
    turtle.setposition(x, y)
    turtle.color(colorMap[regionMap[i][j]])
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x, yy)
    turtle.goto(xx, yy)
    turtle.goto(xx, y)
    turtle.goto(x, y)
    turtle.end_fill()

# speacial draw
def specialDraw(i, j):
    if specialMap[i][j] == 'T':
        treasureDraw(i, j)
    elif specialMap[i][j] == 'M':
        mountainDraw(i, j)
    elif specialMap[i][j] == 'P':
        prisonDraw(i, j)

# MAP DRAWER
def mapDrawer():
    turtle.penup()
    for i in range(N):
        for j in range(N):
            regionDraw(i, j)
            specialDraw(i, j)
            boundaryDraw(i, j)            

# MAIN
def main(scWidth, scHeight, size):
    turtle.setup(scWidth, scHeight)
    turtle.speed(0)

    global mapHeight, mapWidth, marginMapLeft, marginMapRight, marginMapTop, marginMapBot
    global regionMap, specialMap, boundaryMap, N, boxH, boxW
    global colorMap
    global leftCorner, topCorner

    N = size
    marginMapLeft = 5
    marginMapRight = 100
    marginMapTop = 5
    marginMapBot = 5
    mapHeight = scHeight - marginMapTop - marginMapBot
    mapWidth = scWidth - marginMapLeft - marginMapRight
    boxH = mapHeight // N
    boxW = mapWidth // N
    
    leftCorner = -(scWidth//2) + marginMapLeft
    topCorner = (scHeight//2) - marginMapTop

    colorMap = ["#FFCCCC", "#FFCC99", "#FFFF66", "#99FF33", "#00FF00",
                "#00CC66", "#009999", "#FF3333", "#C0C0C0", "#606060",
                "#FF007F", "#FFCCFF", "#6666FF", "#33FF99", "#333300",
                "#FFE666"]
    
    random.shuffle(colorMap)
    colorMap = ["#000066"] + colorMap

    
    turtle.tracer(False)
    mapDrawer()
    turtle.update()
