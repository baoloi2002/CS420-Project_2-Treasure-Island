
# import turtle library
import turtle
import random
from tkinter import *  # Python 3
from PIL import Image, ImageTk
import cv2
import numpy as np


# mountain draw
def mountainDraw(i, j):
    pass

# treasure Draw
def treasureDraw(i, j):
    pass

# prison Draw
def prisonDraw(i, j):
    pass

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
def main(scWidth, scHeight, row, col, region, special, boundary):


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
    boundaryMap = boundary
    
    leftCorner = 0
    topCorner = 0

    colorMap = [(255, 204, 204), (255, 204, 153), (255, 255, 102), (153, 255, 51), (0, 255, 0),
                (0, 204, 102), (0, 153, 153), (255, 51, 51), (192, 192, 192), (96, 96, 96),
                (255, 0, 127), (255, 204, 255), (102, 102, 255), (51, 255, 153), (51, 51, 0),
                (255, 230, 102)]
    
    #random.shuffle(colorMap)
    colorMap = [(0, 0, 102)] + colorMap

    image = np.zeros((mapHeight, mapWidth, 3), np.uint8)

    mapDrawer()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite("test.png", image)
