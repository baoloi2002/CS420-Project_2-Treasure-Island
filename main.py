import MapGenerator
from AgentP import Agent
import random

################################################################################################################
def Hint_1(isTrue):
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
    return res

def Hint_2(isTrue):
    res = []
    for u in range(4):
        x = random.randint(1, numRegion)
        if x == regionMap[Tx][Ty]:
            continue
        res.append(x)
    if isTrue:
        res.append(regionMap[Tx][Ty])
    else:
        pass
    return res

def Hint_3(isTrue):
    res = []
    for u in range(2):
        x = random.randint(1, numRegion)
        while x == regionMap[Tx][Ty]:
            x = random.randint(1, numRegion)
        res.append(x)
    if isTrue:
        pass
    else:
        res.append(regionMap[Tx][Ty])
    return res

def Hint_4(isTrue):
    # large rectangle > 7
    W = H = 8
    if isTrue:
        xL = max(Tx - W, 0)
        xR = xL + W - 1
        yL = max(Ty - H, 0)
        yR = yL + W - 1
    else:
        if Tx + W < N:
            xL = Tx + 1
            xR = xL + W - 1
        else:
            xR = Tx - 1
            xL = xR - W + 1

        if Ty + W < M:
            yL = Ty + 1
            yR = yL + W - 1
        else:
            yR = Ty - 1
            yL = yR - W + 1
    
    return [[xL, yL], [xR, yR]]

def Hint_5(isTrue):
    # small rectangle < 7
    W = H = 5
    if isTrue:
        if Tx + W < N:
            xL = Tx + 1
            xR = xL + W - 1
        else:
            xR = Tx - 1
            xL = xR - W + 1

        if Ty + W < M:
            yL = Ty + 1
            yR = yL + W - 1
        else:
            yR = Ty - 1
            yL = yR - W + 1
    else:
        xL = max(Tx - W, 0)
        xR = xL + W - 1
        yL = max(Ty - H, 0)
        yR = yL + W - 1
    
    return [[xL, yL], [xR, yR]]

def Hint_6(isTrue):
    if isTrue:
        if abs(Ax-Tx)**2 + abs(Ay-Ty)**2 < abs(Px-Tx)**2 + abs(Py-Ty)**2:
            return "YOU"
        else:
            return "PIRATE"
    else:
        if abs(Ax-Tx)**2 + abs(Ay-Ty)**2 >= abs(Px-Tx)**2 + abs(Py-Ty)**2:
            return "YOU"
        else:
            return "PIRATE"

def Hint_7(isTrue):
    
    if isTrue:
        if random.randint(0, 1):
            return ["ROW", Tx]
        else:
            return ["COL", Ty]
    else:
        if random.randint(0, 1):
            u = random.randint(0, N-1)
            while u == Tx:
                u = random.randint(0, N-1)
            return ["ROW", u]
        else:
            u = random.randint(0, M-1)
            while u == Ty:
                u = random.randint(0, M-1)
            return ["COL", u]
    
def Hint_8(isTrue):
    if isTrue:
        if random.randint(0, 1):
            u = random.randint(0, N-1)
            while u == Tx:
                u = random.randint(0, N-1)
            return ["ROW", u]
        else:
            u = random.randint(0, M-1)
            while u == Ty:
                u = random.randint(0, M-1)
            return ["COL", u]
    else:
        if random.randint(0, 1):
            return ["ROW", Tx]
        else:
            return ["COL", Ty]

def Hint_9(isTrue):
    if isTrue:
        pass
    else:
        pass

def Hint_10(isTrue):
    if isTrue:
        pass
    else:
        pass

def Hint_11(isTrue):
    if isTrue:
        pass
    else:
        pass

def Hint_12(isTrue):
    if isTrue:
        pass
    else:
        pass

def Hint_13(isTrue):
    if isTrue:
        pass
    else:
        pass

def Hint_14(isTrue):
    if isTrue:
        pass
    else:
        pass

def Hint_15(isTrue):
    if isTrue:
        pass
    else:
        pass



################################################################################################################
def doSTH(action):
    global Px, Py
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if action[0] == 0:
        u = action[1]
        LOG.append("AGENT TELEPORT TO " + str(u))
        if u[0] == Tx and u[1] == Ty:
            status = "WIN"
        Ax = u[0]
        Ay = u[1]
        return
    if action[0] == 1:
        u = action[1]
        LOG.append("AGENT VERIFY HINT " + str(u) + " " + str(hintList[u]))
        agent.getVerification(hintList[u])
        return
    if action[0] == 2:
        LOG.append("AGENT ACTION 2")
        u = action[1]
        z = direction[u[0]]
        for i in range(u[1]):
            v = [Px + z[0], Py + z[1]]
            if v[0] >= 0 and v[0] < N and v[1] >= 0 and v[1] < M:
                Px += v[0]
                Py += v[1]
        # Small scan 5x5
        LOG.append("AGENT SMALL SCAN " + str(u))
        if abs(Tx - Ax) <= 2 and abs(Ty - Ay) <= 2:
            status = "WIN"
        return

    if action[0] == 3:
        LOG.append("AGENT ACTION 3")
        u = action[1]
        z = direction[u[0]]
        for i in range(u[1]):
            v = [Px + z[0], Py + z[1]]
            if v[0] >= 0 and v[0] < N and v[1] >= 0 and v[1] < M:
                Px += v[0]
                Py += v[1]

    if action[0] == 4:
        LOG.append("AGENT LARGE SCAN " + str(u))
        # Large scan 7x7
        if abs(Tx - Ax) <= 3 and abs(Ty - Ay) <= 3:
            status = "WIN"
        return

def Reveal():
    global LOG
    LOG.append("Reveal " + str(Px) + " " + str(Py))
    return [0, [Px, Py]]

def hintCreate(isTrue):
    hint = random.randint(1, 8)# 9 - 15 chưa xong
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
    LOG.append("HINT " + str(isTrue) + " " + str(res))
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


def startGame():
    global agent, LOG, status, hintList
    while True:
        Ax = random.randint(0, N-1)
        Ay = random.randint(0, M-1)
        if regionMap[Ax][Ay] == 0: continue
        if specialMap[Ax][Ay] == 'M' or specialMap[Ax][Ay] == 'P': continue 
        if Ax == Tx and Ay == Ty: continue
        break

    agent = Agent(N, M, regionMap, specialMap, Ax, Ay)# START GAME INPUT MAP and current location
    # Before Pirate Out (N turns)
    hintList = []
    for i in range(pirateFree-1):       
        LOG.append("TURN_"+str(i+1))
        if i+1 == pirateReveal:
            agent.getInformation(Reveal())
        if i == 0:
            hintList.append(True)
            agent.getInformation(hintCreate(True))
            doSTH(agent.makeMove())
            if status == "WIN": return
            doSTH(agent.makeMove())
            if status == "WIN": return
        else:
            hintList.append(random.choice([True, False]))
            agent.getInformation(hintCreate(hintList[-1]))
            doSTH(agent.makeMove())
            if status == "WIN": return
            doSTH(agent.makeMove())
            if status == "WIN": return

    # After Pirate Out
    len = shortestPath([Px, Py], [Tx, Ty])
    len = (len+1)//2

    for i in range(len):        
        LOG.append("TURN_"+str(i+pirateFree))
        if i == 0:
            LOG.append("Pirate FREE")
        if i+1 == pirateReveal:
            agent.getInformation(Reveal())
        hintList.append(random.choice([True, False]))
        agent.getInformation(hintCreate(hintList[-1]))
        doSTH(agent.makeMove())
        if status == "WIN": return
        doSTH(agent.makeMove())
        if status == "WIN": return

    # Pirate WIN
    #...
    LOG.append("PIRATE REACH THE TREASURE FIRST !!!")
    status = "LOSE"


def input():
    global N, M, regionMap, specialMap, pirateReveal, pirateFree, numRegion, Tx, Ty, boundaryMap, status, Px, Py, Ax, Ay, LOG
    LOG = []
    status = ""
    with open("Map.txt", "r") as f:
        N, M = [int(u) for u in f.readline().split()]
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
                if len(tmp[j]) == 2:
                    specialMap[i][j] = tmp[j][1]
                regionMap[i][j] = int(tmp[j][0])
    tmp = []
    for i in range(N):
        for j in range(M):
            if specialMap[i][j] == 'P':
                tmp.append((i, j))
    Px, Py = random.choice(tmp)


def output():
    with open("Log.txt", "w") as f:
        f.write(str(len(LOG)) + "\n")
        f.write(status + "\n")
        for u in LOG:
            f.write(u + "\n")


if __name__ == '__main__':
    MapGenerator.main(16)
    input()
    startGame()
    output()