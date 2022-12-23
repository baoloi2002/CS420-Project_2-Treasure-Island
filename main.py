import MapGenerator
import AgentP









def hintCreate():
    pass

def startGame():
    agent = AgentP()
    # Before Pirate Out (N turns)
    for i in range(N):
        if i == 0:
            pass
        else:
            pass
        if i == pirateReveal:
            pass


def input():
    global N, M, regionMap, specialMap, pirateReveal, pirateFree, numRegion, Tx, Ty, boundaryMap
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
                regionMap[i][j] = tmp[j][0]



if __name__ == '__main__':
    MapGenerator.main(16)
    input()
    startGame()