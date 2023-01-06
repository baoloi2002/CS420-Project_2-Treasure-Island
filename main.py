import MapGenerator
from AgentP import Agent
import random
import Visualization

################################################################################################################
def Hint_1(isTrue):
    global LOG
    res = []
    for u in range(15):
        x = random.randint(0, N-1)
        y = random.randint(0, M-1)
        if x == Tx and y == Ty: continue
        res.append([x, y])
    if isTrue:
        pass
    else:
        res.append([Tx, Ty])
    LOG.append(str(len(res)))
    for u in res:
        LOG.append(str(u[0]) + " " + str(u[1]))
    return res

def Hint_2(isTrue):
    global LOG
    res = []
    for u in range(4):
        x = random.randint(0, numRegion-1)
        if x == regionMap[Tx][Ty]:
            continue
        res.append(x)
    if isTrue:
        res.append(regionMap[Tx][Ty])
    else:
        pass
    LOG.append(str(len(res)))
    tmp = ""
    for u in res:
        tmp = tmp + " " + str(u)
    LOG.append(tmp)
    return res

def Hint_3(isTrue):
    global LOG
    res = []
    for u in range(2):
        x = random.randint(0, numRegion-1)
        while x == regionMap[Tx][Ty]:
            x = random.randint(0, numRegion-1)
        res.append(x)
    if isTrue:
        pass
    else:
        res.append(regionMap[Tx][Ty])
    LOG.append(str(len(res)))
    tmp = ""
    for u in res:
        tmp = tmp + " " + str(u)
    LOG.append(tmp)
    return res

def Hint_4(isTrue):
    global LOG
    # large rectangle > 7
    W = H = 8
    if isTrue:
        while True:
            xL = random.randint(0, N-W)
            yL = random.randint(0, M-H)
            xR = min(xL + H-1, N-1)
            yR = min(yL + W-1, M-1)
            if xL <= Tx and Tx <= xR and yL <= Ty and Ty <= yR:
                break
    else:
        while True:
            xL = random.randint(0, N-W)
            yL = random.randint(0, M-H)
            xR = min(xL + H-1, N-1)
            yR = min(yL + W-1, M-1)
            if xL <= Tx and Tx <= xR and yL <= Ty and Ty <= yR:
                continue
            break
    xR = min(xR, N-1)
    yR = min(yR, M-1)
    LOG.append(str(xL) + " " + str(yL))
    LOG.append(str(xR) + " " + str(yR))
    return [[xL, yL], [xR, yR]]

def Hint_5(isTrue):
    global LOG
    # small rectangle < 7
    W = H = 5
    if isTrue:
        while True:
            xL = random.randint(0, N-W)
            yL = random.randint(0, M-H)
            xR = min(xL + H-1, N-1)
            yR = min(yL + W-1, M-1)
            if xL <= Tx and Tx <= xR and yL <= Ty and Ty <= yR:
                continue
            break
    else:
        while True:
            xL = random.randint(0, N-W)
            yL = random.randint(0, M-H)
            xR = min(xL + H-1, N-1)
            yR = min(yL + W-1, M-1)
            if xL <= Tx and Tx <= xR and yL <= Ty and Ty <= yR:
                break
    xR = min(xR, N-1)
    yR = min(yR, M-1)
    LOG.append(str(xL) + " " + str(yL))
    LOG.append(str(xR) + " " + str(yR))
    
    return [[xL, yL], [xR, yR]]

def Hint_6(isTrue):
    global LOG
    res = ""
    if isTrue:
        if abs(Ax-Tx)**2 + abs(Ay-Ty)**2 < abs(Px-Tx)**2 + abs(Py-Ty)**2:
            res = "YOU"
        else:
            res = "PRISON"
    else:
        if abs(Ax-Tx)**2 + abs(Ay-Ty)**2 >= abs(Px-Tx)**2 + abs(Py-Ty)**2:
            res = "YOU"
        else:
            res = "PRISON"
    LOG.append(res)
    return res

def Hint_7(isTrue):
    global LOG
    res = []
    if isTrue:
        if random.randint(0, 1):
            res = ["ROW", Tx]
        else:
            res = ["COL", Ty]
    else:
        if random.randint(0, 1):
            u = random.randint(0, N-1)
            while u == Tx:
                u = random.randint(0, N-1)
            res = ["ROW", u]
        else:
            u = random.randint(0, M-1)
            while u == Ty:
                u = random.randint(0, M-1)
            res = ["COL", u]
    LOG.append(res[0])
    LOG.append(res[1])
    return res
    
def Hint_8(isTrue):
    global LOG
    res = []
    if isTrue:
        if random.randint(0, 1):
            u = random.randint(0, N-1)
            while u == Tx:
                u = random.randint(0, N-1)
            res = ["ROW", u]
        else:
            u = random.randint(0, M-1)
            while u == Ty:
                u = random.randint(0, M-1)
            res = ["COL", u]
    else:
        if random.randint(0, 1):
            res = ["ROW", Tx]
        else:
            res = ["COL", Ty]
    LOG.append(res[0])
    LOG.append(res[1])
    return res

def Hint_9(isTrue):
    global LOG
    boundary = []
    notBound = []
    k = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(Tx-1, Tx+2):
        for j in range(Ty-1, Ty+2):
            if i < 0 or j < 0 or i >= N or j >= M: continue
            if regionMap[i][j] not in boundary:
                boundary.append(regionMap[i][j])
    for i in range(N):
        for j in range(M):
            if regionMap[i][j] not in boundary and regionMap[i][j] not in notBound:
                for z in k:
                    v = [i+z[0], j+z[1]]
                    if v[0] < 0 or v[0] >= N or v[1] < 0 or v[1] >= M: continue
                    if regionMap[v[0]][v[1]] in boundary:
                        notBound.append(regionMap[i][j])
                    
    res = []
    if isTrue:
        res.append(random.choice(boundary))
        for u in notBound:
            boundary.append(u)
        boundary = list(set(boundary))
        while len(res) < 2 and len(boundary) > 1:
            u = random.randint(0, numRegion-1)
            if u in res: continue
            if u not in boundary: continue
            res.append(u)
            break
    else:
        boundary = list(set(boundary))
        while len(res) < 2 and numRegion - len(boundary) > 0:
            u = random.randint(0, numRegion-1)
            if u in boundary: continue
            res.append(u)
            boundary.append(u)
    if len(res) == 0:
        LOG.append("")
    elif len(res) == 1:
        LOG.append(str(res[0]))
    else:
        LOG.append(str(res[0]) + " " + str(res[1]))
        
    return res

def Hint_10(isTrue):
    global LOG
    res =[]
    res.append(regionMap[Tx][Ty])
    k = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for z in k:
        if Tx+z[0] <0 or Tx+z[0]>=N or Ty+z[1] <0 or Ty+z[1]>=M:
            continue
        v = [Tx+z[0], Ty+z[1]]
        if regionMap[v[0]][v[1]] != regionMap[Tx][Ty] and regionMap[v[0]][v[1]] != 0:
            res.append(regionMap[v[0]][v[1]])

    tmp  = False   
    # LOG.append(str(res[0]))

    if (len(res)>=2):
        tmp = True
    if not isTrue:
        tmp = not tmp
    LOG.append(str(tmp))
    return tmp

def Hint_11(isTrue):
    global LOG
    tmp  = False
    for i in range(Tx-3, Tx+4):
        if tmp: break
        for j in range(Ty-3, Ty+4):
            if i < 0 or j < 0 or i >= N or j >= M: continue
            if regionMap[i][j] ==0:
                tmp = True
                break

    if not isTrue:
        tmp = not tmp
    LOG.append(str(tmp))
    return tmp

def Hint_12(isTrue):
    global LOG
    lst = []
    lst.append([[0, 0], [N-1, M//2]])
    lst.append([[0, 0], [N//2, M-1]])
    lst.append([[N//2, 0], [N-1, M-1]])
    lst.append([[0, M//2], [N-1, M-1]])
    random.shuffle(lst)
    res = []
    if isTrue:
        for u in lst:
            if u[0][0] <= Tx and Tx <= u[1][0] and u[0][1] <= Ty and Ty <= u[1][1]:
                continue
            res = u
            break
    else:
        for u in lst:
            if u[0][0] <= Tx and Tx <= u[1][0] and u[0][1] <= Ty and Ty <= u[1][1]:
                res = u
                break
    LOG.append(str(res[0][0]) + " " + str(res[0][1]))
    LOG.append(str(res[1][0]) + " " + str(res[1][1]))
    return res

def Hint_13(isTrue):
    global LOG
    direction = ['W', 'E', 'N', 'S', 'SE', 'SW', 'NE', 'NW']
    point = random.choice(["CENTER", "PRISON"])
    res = []
    u = []
    if point == "CENTER":
        u = [N//2, M//2]
    else:
        u = [Px, Py]
    res.append(u)
    LOG.append(str(u[0]) + " " + str(u[1]))
    lst = []
    X = Tx - u[0]
    Y = Ty - u[1]
    if X >= 0:
        if Y >= 0:
            lst.append('SE')
            if Y <= X:
                lst.append('S')
            if Y >= X:
                lst.append('E')

        if Y <= 0:
            lst.append('SW')
            if -Y <= X:
                lst.append('S')
            if -Y >= X:
                lst.append('W')
    if X <= 0:
        if Y >= 0:
            lst.append('NE')
            if Y <= -X:
                lst.append('N')
            if Y >= -X:
                lst.append('E')
        if Y <= 0:
            lst.append('NW')
            if -Y <= -X:
                lst.append('N')
            if -Y >= -X:
                lst.append('W')

    lst = list(set(lst))
    if isTrue:
        res.append(random.choice(lst))
    else:
        tmp = []
        for v in direction:
            if v not in lst:
                tmp.append(v)
        res.append(random.choice(tmp))
    LOG.append(res[1])
    return res

def Hint_14(isTrue):
    global LOG
    res = []
    if isTrue:
        xL = Tx - random.randint(2, 10)
        yL = Ty - random.randint(2, 10)
        xR = Tx + random.randint(2, 10)
        yR = Ty + random.randint(2, 10)
        
        xL = max(0, xL)
        yL = max(0, yL)
        xR = min(xR, N-1)
        yR = min(yR, M-1)

        res.append([[xL, yL], [xR, yR]])     

        if abs(Tx - xL) > abs(Tx - xR):
            xL += 1
            yL += 1
            xR -= 1
            yR = Ty-1
        else:
            xL = Tx+1
            yL += 1
            xR -= 1
            yR -= 1


        res.append([[xL, yL], [xR, yR]])     

    else:
        if random.randint(0, 1):
            xL = Tx - random.randint(0, 5)
            yL = Ty - random.randint(0, 5)
            xR = Tx + random.randint(0, 5)
            yR = Ty + random.randint(0, 5)
            xL = max(1, xL)
            yL = max(1, yL)
            xR = min(xR, N-2)
            yR = min(yR, M-2)

            res.append([[xL, yL], [xR, yR]])     

            xL -= random.randint(0, 5)
            yL -= random.randint(0, 5)
            xR += random.randint(0, 5)
            yR += random.randint(0, 5)

            xL = max(0, xL)
            yL = max(0, yL)
            xR = min(xR, N-1)
            yR = min(yR, M-1)

            res.append([[xL, yL], [xR, yR]])        

        else:
            xL = Tx+1
            yL = Ty+1
            xR = xL + random.randint(2, 10) 
            yR = yL + random.randint(2, 10) 
            xR = min(xR, N-1)
            yR = min(yR, M-1)

            res.append([[xL, yL], [xR, yR]])      
            xL += 1
            yL += 1
            xR = random.randint(xL, xR)
            yR = random.randint(yL, yR)
            res.append([[xL, yL], [xR, yR]])    
    if res[0][0][0] > res[0][1][0]:
        res[0][0][0], res[0][1][0] = res[0][1][0], res[0][0][0]
    if res[0][0][1] > res[0][1][1]:
        res[0][0][1], res[0][1][1] = res[0][1][1], res[0][0][1]
    if res[1][0][0] > res[1][1][0]:
        res[1][0][0], res[1][1][0] = res[1][1][0], res[1][0][0]
    if res[1][0][1] > res[1][1][1]:
        res[1][0][1], res[1][1][1] = res[1][1][1], res[1][0][1]
    LOG.append(str(res[0][0][0]) + " " + str(res[0][0][1])) 
    LOG.append(str(res[0][1][0]) + " " + str(res[0][1][1])) 
    LOG.append(str(res[1][0][0]) + " " + str(res[1][0][1])) 
    LOG.append(str(res[1][1][0]) + " " + str(res[1][1][1])) 
    return res
        

def Hint_15(isTrue):
    global LOG
    res = []
    for i in range(N):
        for j in range(M):
            if specialMap[i][j] == 'M':
                if regionMap[i][j] not in res:
                    res.append(regionMap[i][j])
    
    tmp = False
    if regionMap[Tx][Ty] in res:
        tmp = True
 
    if not isTrue:
        tmp = not tmp
    LOG.append(str(tmp))
    return res



################################################################################################################
def doSTH(action):
    direction = {0: 'N', 1: 'S', 2: 'W', 3: 'E'}
    LOG.append("AGENT")
    global Ax, Ay, status
    k = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if action[0] == 0:
        u = action[1]
        LOG.append("TELEPORT")
        LOG.append(str(u[0]) + " " + str(u[1]))

        #if u[0] == Tx and u[1] == Ty:
        #    status = "WIN"
        Ax = u[0]
        Ay = u[1]
        return 0

    if action[0] == 1:
        u = action[1]
        LOG.append("VERIFY")
        LOG.append(str(u))
        LOG.append(str(hintList[u-1]))
        agent.getVerification([u,hintList[u-1]])
        return 1

    if action[0] == 2:
        u = action[1]
        z = k[u[0]]
        LOG.append("2 MOVE " + str(u[1]) + " steps, direction " + direction[u[0]] )
        LOG.append(str(z))
        LOG.append(str(u[1]))
        for i in range(u[1]):
            v = [Ax + z[0], Ay + z[1]]
            if v[0] >= 0 and v[0] < N and v[1] >= 0 and v[1] < M:
                Ax = v[0]
                Ay = v[1]
        # Small scan 5x5
        LOG.append("SMALL SCAN")
        if abs(Tx - Ax) <= 2 and abs(Ty - Ay) <= 2:
            status = "WIN"
        return 1

    if action[0] == 3:
        u = action[1]
        z = k[u[0]]
        LOG.append("3 MOVE " + str(u[1]) + " steps, direction " + direction[u[0]] )
        LOG.append(str(z))
        LOG.append(str(u[1]))
        for i in range(u[1]):
            v = [Ax + z[0], Ay + z[1]]
            if v[0] >= 0 and v[0] < N and v[1] >= 0 and v[1] < M:
                Ax = v[0]
                Ay = v[1]
        return 1

    if action[0] == 4:
        LOG.append("LARGE SCAN")
        # Large scan 7x7
        if abs(Tx - Ax) <= 3 and abs(Ty - Ay) <= 3:
            status = "WIN"
        return 1
    
    print("WRONG ACTION")
    return 10

def Reveal():
    global LOG
    LOG.append("Reveal " + str(Px) + " " + str(Py))
    return [0, [Px, Py]]

def hintCreate(isTrue):
    hint = random.randint(1, 15)
    LOG.append("HINT " + str(len(hintList)))
    LOG.append(str(hint))
    res = [16, [0, 0]]
    if hint == 1:
        res =  [hint, Hint_1(isTrue)]
    if hint == 2:
        res =  [hint, Hint_2(isTrue)]
    if hint == 3:
        res =  [hint, Hint_3(isTrue)]
    if hint == 4:
        res =  [hint, Hint_4(isTrue)]
    if hint == 5:
        res =  [hint, Hint_5(isTrue)]
    if hint == 6:
        res =  [hint, Hint_6(isTrue)]
    if hint == 7:
        res =  [hint, Hint_7(isTrue)]
    if hint == 8:
        res =  [hint, Hint_8(isTrue)]
    if hint == 9:
        res =  [hint, Hint_9(isTrue)]
    if hint == 10:
        res =  [hint, Hint_10(isTrue)]
    if hint == 11:
        res =  [hint, Hint_11(isTrue)]
    if hint == 12:
        res =  [hint, Hint_12(isTrue)]
    if hint == 13:
        res =  [hint, Hint_13(isTrue)]
    if hint == 14:
        res =  [hint, Hint_14(isTrue)]
    if hint == 15:
        res =  [hint, Hint_15(isTrue)]
    return res

def shortestPath(s, t): # BFS to find shortest path
    que = []
    vis = [[False for j in range(M)] for i in range(N)]
    k = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    que.append(list([s, 0]))
    vis[s[0]][t[0]]
    while len(que) > 0:
        u, w = que.pop(0)

        for z in k:
            v = [u[0] + z[0], u[1] + z[1]]
            if regionMap[v[0]][v[1]] == 0: continue
            if specialMap[v[0]][v[1]] == "M" or specialMap[v[0]][v[1]] == "P": continue
            if vis[v[0]][v[1]]: continue
            vis[v[0]][v[1]] = True
            if v[0] == t[0] and v[1] == t[1]:
                return w+1
            que.append(list([v, w+1]))
    # Something went wrong
    return -1


def getPlayerMaskToLOG():
    global LOG, agent
    LOG.append("MASK")
    LOG.append(str(Ax) + " " + str(Ay))
    a = agent.getMASK()
    for i in range(N):
        tmp = ""
        for j in range(M):
            if len(tmp) > 0:
                tmp += " "
            tmp += str(a[i][j])
        LOG.append(tmp)


def startGame():
    global agent, LOG, status, hintList, Ax, Ay
    while True:
        Ax = random.randint(0, N-1)
        Ay = random.randint(0, M-1)
        if regionMap[Ax][Ay] == 0: continue
        if specialMap[Ax][Ay] == 'M' or specialMap[Ax][Ay] == 'P': continue 
        if Ax == Tx and Ay == Ty: continue
        break

    agent = Agent(N, M, regionMap, specialMap, Ax, Ay)# START GAME INPUT MAP and current location
    LOG.append("START")
    LOG.append("AGENT: " + str(Ax) + " " + str(Ay))
    # Before Pirate Out (N turns)
    hintList = []
    for i in range(pirateFree-1):    
        turn = 2   
        LOG.append("TURN "+str(i+1) + "**********************************************************")
        if i+1 == pirateReveal:
            agent.getInformation(Reveal())
        if i == 0:
            hintList.append(True)
            agent.getInformation(hintCreate(True))

            while turn > 0:
                turn -= doSTH(agent.makeMove())
                getPlayerMaskToLOG()
                if status == "WIN": return
        else:
            hintList.append(random.choice([True, False]))
            agent.getInformation(hintCreate(hintList[-1]))

            while turn > 0:
                turn -= doSTH(agent.makeMove())
                getPlayerMaskToLOG()
                if status == "WIN": return
                
    # After Pirate Out
    len = shortestPath([Px, Py], [Tx, Ty])
    len = (len+1)//2

    for i in range(len):        
        turn = 2
        LOG.append("TURN "+str(i+pirateFree) + " : " + str(len-i-1) + " turns left to pirate to the treasure " + "**********************************************************")
        if i == 0:
            LOG.append("FREE PIRATE")
        if i+1 == pirateReveal:
            agent.getInformation(Reveal())
        hintList.append(random.choice([True, False]))
        agent.getInformation(hintCreate(hintList[-1]))
        while turn > 0:
            turn -= doSTH(agent.makeMove())
            getPlayerMaskToLOG()
            if status == "WIN": return
    

    # Pirate WIN
    #...
    status = "LOSE"


def input():
    global N, M, regionMap, specialMap, pirateReveal, pirateFree, numRegion, Tx, Ty, boundaryMap, status, Px, Py, Ax, Ay, LOG
    LOG = []
    status = ""
    with open("Map.txt", "r") as f:
        M, N = [int(u) for u in f.readline().split()]
        pirateReveal = int(f.readline()) 
        pirateFree = int(f.readline()) 
        numRegion = int(f.readline())
        Tx, Ty = [int(u) for u in f.readline().split()]
        # MAP with number
        regionMap = [[0 for j in range(M)] for i in range(N)]
        # Map with prison, treasure, mountain
        specialMap = [[' ' for j in range(M)] for i in range(N)]
        # Map with boundary
        boundaryMap = [[0 for j in range(M)] for i in range(N)]

        for i in range(N):
            s = f.readline().replace(" ", "")
            s = s.replace("\n", "")
            tmp = [u for u in s.split(";")]
            for j in range(M):
                if tmp[j][-1] not in "0123456789":
                    specialMap[i][j] = tmp[j][-1]
                    regionMap[i][j] = int(tmp[j][:len(tmp[j])-1])
                else:
                    regionMap[i][j] = int(tmp[j])
                    
    tmp = []
    for i in range(N):
        for j in range(M):
            if specialMap[i][j] == 'P':
                tmp.append((i, j))
    Px, Py = random.choice(tmp)


def output():
    global LOG
    LOG.append(status)
    for i in range(len(LOG)):
        LOG[i] = str(LOG[i])
    with open("Log.txt", "w") as f:
        f.write(str(len(LOG)) + "\n")
        f.write(status + "\n")
        for u in LOG:
            f.write(str(u) + "\n")


if __name__ == '__main__':
    MapGenerator.main(32)
    input()
    startGame()
    output()
    Visualization.main(LOG)
