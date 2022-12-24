import MapGenerator
import AgentP
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
        if x == regionMap[Tx][Ty]:
            continue
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
        yR = yR + W - 1
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
        yR = yR + W - 1
    
    return [[xL, yL], [xR, yR]]

def Hint_6(isTrue):
    if isTrue:
        pass
    else:
        pass

def Hint_7(isTrue):
    if isTrue:
        pass
    else:
        pass
    
def Hint_8(isTrue):
    if isTrue:
        pass
    else:
        pass

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
def doSTH():
    pass

def Reveal():
    pass

def hintCreate(isTrue):
    hint = random.randint(1, 15)
    if hint == 1:
        return [hint, Hint_1(isTrue)]
    if hint == 2:
        return [hint, Hint_2(isTrue)]
    if hint == 3:
        return [hint, Hint_3(isTrue)]
    if hint == 4:
        return [hint, Hint_4(isTrue)]
    if hint == 5:
        return [hint, Hint_5(isTrue)]
    if hint == 6:
        return [hint, Hint_6(isTrue)]
    if hint == 7:
        return [hint, Hint_7(isTrue)]
    if hint == 8:
        return [hint, Hint_8(isTrue)]
    if hint == 9:
        return [hint, Hint_9(isTrue)]
    if hint == 10:
        return [hint, Hint_10(isTrue)]
    if hint == 11:
        return [hint, Hint_11(isTrue)]
    if hint == 12:
        return [hint, Hint_12(isTrue)]
    if hint == 13:
        return [hint, Hint_13(isTrue)]
    if hint == 14:
        return [hint, Hint_14(isTrue)]
    if hint == 15:
        return [hint, Hint_15(isTrue)]
    return [16, [0, 0]]

def startGame():
    global agent
    agent = AgentP()
    # Before Pirate Out (N turns)
    hintList = []
    for i in range(N):        
        if i == pirateReveal:
            agent.getInformation(Reveal())
        if i == 0:
            hintList.append(True)
            agent.getInformation(hintCreate(True))
            doSTH(agent.makeMove())
            doSTH(agent.makeMove())
        else:
            hintList.append(random.choice([True, False]))
            agent.getInformation(hintCreate(hintList[-1]))
            doSTH(agent.makeMove())
            doSTH(agent.makeMove())

    # After Pirate Out

def input():
    global N, M, regionMap, specialMap, pirateReveal, pirateFree, numRegion, Tx, Ty, boundaryMap, status
    with open("Map.txt", "r") as f:
        N, M = [int(u) for u in f.readline().split()]
        pirateReveal = int(f.readline()) -1
        pirateFree = int(f.readline()) -1
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
                regionMap[i][j] = tmp[j][0]



if __name__ == '__main__':
    MapGenerator.main(16)
    input()
    startGame()