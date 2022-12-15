# import turtle library
import turtle
import random 
# importing "heapq" to implement heap queue
import heapq

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

# smooth land
def smoothLand():
    global regionMap    
    vis = [[False for j in range(N)] for i in range(N)]
    k = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    lst = []
    for i in range(N):
        for j in range(N):
            if regionMap[i][j] == 0: continue
            if vis[i][j]: continue
            lst.append([i, j])
            que = []
            que.append([i,j])
            vis[i][j] = True
            while len(que) > 0:
                u = que.pop(0)
                for z in k:
                    v = [u[0]+z[0], u[1]+z[1]]
                    if vis[v[0]][v[1]]: continue
                    if regionMap[v[0]][v[1]] == 0: continue
                    vis[v[0]][v[1]] = True
                    que.append(v)
    random.shuffle(lst)
    for i in range(len(lst)-1):
        u = lst[i]
        v = lst[i+1]
        while u[0] != v[0] or u[1] != v[1]:
            uu = abs(u[0] - v[0])
            vv = abs(u[1] - v[1])
            if uu >= vv:
                if u[0] < v[0]:
                    u[0] += 1
                else:
                    u[0] -= 1
            else:
                if u[1] < v[1]:
                    u[1] += 1
                else:
                    u[1] -= 1
            regionMap[u[0]][u[1]] = 1

# create land
def createLand():
    global regionMap
    que = []
    que.append([[N//2, N//2], 0.99])
    rateDown = 1 - (64/N)*2/100
    k = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    vis = [[False for j in range(N)] for i in range(N)]
    cLim = 15 - 128//N
    co = [i for i in range(2, cLim+1)]

    regionMap[N//2][N//2] = 1
    vis[N//2][N//2] = True
    while len(que) > 0:
        u = que[0][0]
        r = que[0][1]
        que.pop(0)
        if random.random() <= 0.01:
            random.shuffle(que)

        for z in k:
            v = [u[0]+z[0], u[1]+z[1]]
            if v[0] < 1 or v[0] >= N-1 or v[1] < 1 or v[1] >= N-1: continue
            if vis[v[0]][v[1]]: continue
            
            if random.random() <= r:
                vis[v[0]][v[1]] = True
                que.append([v, r*rateDown])                
                regionMap[v[0]][v[1]] = int(regionMap[u[0]][u[1]])
                if len(co) > 0:
                    if random.random() <= 0.15:
                        regionMap[v[0]][v[1]] = co.pop(0)
                    
# create mountain
def createMountain():
    global specialMap
    que = []
    for i in range(N):
        for j in range(N):
            if regionMap[i][j] == 0: continue
            if random.random() <= 0.05:
                que.append([i, j])
                specialMap[i][j] = 'M'
    while len(que):
        u = que.pop(0)
        for x in range(u[0]-1, u[0]+2):
            for y in range(u[1]-1, u[1]+2):
                if regionMap[x][y] == 0: continue
                if specialMap[x][y] != '0': continue
                if random.random() <= 0.15:
                    specialMap[x][y] = 'M'
                    que.append([x, y])

# check is prison reachable treasure
def checkIsReachable(tLst, pLst):
    que = [u for u in tLst]
    vis = [[False for j in range(N)] for i in range(N)]
    k = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for u in tLst:
        vis[u[0]][u[1]] = True
    while len(que) > 0:
        u = que.pop(0)
        for z in k:
            v = [u[0] + z[0], u[1] + z[1]]
            if regionMap[v[0]][v[1]] == 0: continue
            if specialMap[v[0]][v[1]] == "M": continue
            if vis[v[0]][v[1]]: continue
            vis[v[0]][v[1]] = True
            que.append(v)

    res = []
    for u in pLst:
        if not vis[u[0]][u[1]]:
            res.append(u)
    
    return res

# create path from prison to treasure
def createPathToTreasure(st, en):
    que = [(0, st)]
    vis = [[False for j in range(N)] for i in range(N)]
    dp = [[1000000000 for j in range(N)] for i in range(N)]
    trace = [[[-1, -1] for j in range(N)] for i in range(N)]
    k = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    dp[st[0]][st[1]] = 0
    heapq.heapify(que)
    while len(que) > 0:
        u = heapq.heappop(que)[1]
        if vis[u[0]][u[1]]: continue
        # create path
        if u[0] == en[0] and u[1] == en[1]:
            while u[0] != st[0] or u[1] != st[1]:
                if specialMap[u[0]][u[1]] == 'M':
                    specialMap[u[0]][u[1]] = '0'
                u = trace[u[0]][u[1]]
            break
        # ***
        vis[u[0]][u[1]] = True
        for z in k:
            v = [u[0] + z[0], u[1] + z[1]]
            if vis[v[0]][v[1]]: continue
            if regionMap[v[0]][v[1]] == 0: continue
            w = dp[u[0]][u[1]]
            if specialMap[u[0]][u[1]] == 'M':
                w += 15
            else:
                w += 1
            if w < dp[v[0]][v[1]]:
                dp[v[0]][v[1]] = w
                trace[v[0]][v[1]] = u
                heapq.heappush(que, (w, v))





# create prison and treasure
def createPrisonTreasure():
    global specialMap
    prison = []
    treasure = []
    pN = 2 +  int(N/64 * 12)
    tN = 1

    for i in range(N):
        for j in range(N):
            if regionMap[i][j] == 0: continue
            if random.random() <= 0.2:
                if random.random() <= 0.5:
                    prison.append([i, j])
                else:
                    treasure.append([i, j])                    
    
    random.shuffle(prison)
    prison = prison[:pN]
    random.shuffle(treasure)
    treasure = treasure[:tN]

    for u in prison:
        specialMap[u[0]][u[1]] = 'P'

    for u in treasure:
        specialMap[u[0]][u[1]] = 'T'
    
    # list of prison that can't go to treasure
    lstPrison = checkIsReachable(treasure, prison)
    for u in lstPrison:
        createPathToTreasure(u, treasure[0])
    # check again
    #lstPrison = checkIsReachable(treasure, prison)
    #print(lstPrison)


# MAP GENERATOR
def mapGenerator():
    global regionMap, specialMap, boundaryMap
    # MAP with number
    regionMap = [[0 for j in range(N)] for i in range(N)]
    # Map with prison, treasure, mountain
    specialMap = [['0' for j in range(N)] for i in range(N)]
    # Map with boundary
    boundaryMap = [[0 for j in range(N)] for i in range(N)]
    # Region
    createLand()
    # smooth land
    #smoothLand()
    # create mountain
    createMountain()
    createPrisonTreasure()
    

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
                "#FF007F", "#FFCCFF", "#6666FF", "#33FF99", "#333300"]
    
    random.shuffle(colorMap)
    colorMap = ["#000066"] + colorMap


    mapGenerator()
    
    turtle.tracer(False)
    mapDrawer()
    turtle.update()

# Using the special variable 
# __name__
if __name__=="__main__":
    # screen width, height + island size
    main(1800, 900, 16)
    turtle.done()