
# import turtle library
import turtle
import random
from tkinter import *  # Python 3
from PIL import Image, ImageTk
import cv2
import numpy as np


# mountain draw
def mountainDraw(i, j):
    global image
    x = j*boxW + leftCorner
    y = i*boxH + topCorner
    xx = x + boxW-1
    yy = y + boxH-1
    
    color = (0, 0, 0)
    image = cv2.line(image, (x, y), (xx, yy), color, 1)
    image = cv2.line(image, (x, yy), (xx, y), color, 1)


# treasure Draw
def treasureDraw(i, j):
    global image
    x = j*boxW + leftCorner
    y = i*boxH + topCorner
    xx = x + boxW-1
    yy = y + boxH-1

    midx = (x+xx)//2
    midy = (y+yy)//2
    r = min(midx-x, midy-y)
    color = (255, 0, 0)
    image = cv2.circle(image, (midx, midy), r, color, -1)
    color = (0, 255, 0)
    image = cv2.circle(image, (midx, midy), int(r/1.5), color, -1)
    color = (0, 0, 255)
    image = cv2.circle(image, (midx, midy), int(r/2.5), color, -1)

# prison Draw
def prisonDraw(i, j):
    global image
    x = j*boxW + leftCorner
    y = i*boxH + topCorner
    xx = x + boxW-1
    yy = y + boxH-1

    color = (0, 0, 0)
    image = cv2.line(image, (x, (y+yy)//2), (xx, (y+yy)//2), color, 2)
    image = cv2.line(image, ((x+xx)//2, y), ((x+xx)//2, yy), color, 2)

# boundary draw
def boundaryDraw(i, j):
    global image
    x = j*boxW + leftCorner
    y = i*boxH + topCorner
    xx = x + boxW-1
    yy = y + boxH-1
    
    start_point = (x, y)
    end_point = (xx, yy)

    if boundaryMap[i][j] == 0:
        color = (255, 255, 255)
    else:
        color = (255, 0, 0)
    

    image = cv2.rectangle(image, start_point, end_point, color, thickness=1)

# land draw
def regionDraw(i, j):
    global image
    x = j*boxW + leftCorner
    y = i*boxH + topCorner
    xx = x + boxW-1
    yy = y + boxH-1
    
    start_point = (x, y)
    end_point = (xx, yy)

    color = colorMap[regionMap[i][j]]

    image = cv2.rectangle(image, start_point, end_point, color=color, thickness=-1)
    

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
    for i in range(N):
        for j in range(M):
            regionDraw(i, j)
            specialDraw(i, j)
            boundaryDraw(i, j)            

# MAIN
def main(scWidth, scHeight, row, col, region, special, boundary, Tx, Ty, color):


    global image
    global mapHeight, mapWidth
    global regionMap, specialMap, boundaryMap, N, M, boxH, boxW
    global colorMap
    global leftCorner, topCorner

    N = row
    M = col
    mapHeight = scHeight
    mapWidth = scWidth
    boxH = mapHeight // N
    boxW = mapWidth // M

    regionMap = region
    specialMap = special
    specialMap[Tx][Ty] = 'T'
    boundaryMap = boundary
    
    leftCorner = 0
    topCorner = 0

    colorMap = color

    image = np.zeros((mapHeight, mapWidth, 3), np.uint8)

    mapDrawer()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite("test.png", image)
