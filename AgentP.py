class Agent:
    def __init__(self, N, M, regionMap, specialMap, Ax, Ay) -> None:
        self.N = N
        self.M = M
        self.regionMap = regionMap
        self.specialMap = specialMap
        self.Ax = Ax
        self.Ay = Ay
        self.Px = -1
        self.Py = -1

        self.isFree = False
        self.mask = [[0 for j in range(M)] for i in range(N)]
        self.hintVerified = {}
        self.hintLst = []
        self.hintMAP = {}
        self.hintSIX = []
        self.hintCnt = 0

    def find(self, tmpMask):
        cnt = 0
        for i in range(self.N):
            for j in range(self.M):
                if self.mask[i][j] == 0 and tmpMask[i][j] == 1:
                    cnt += 1
        return cnt


    def reverseMask(self, tmpMask):
        res = [[0 for j in range(self.M)] for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.M):
                if tmpMask[i][j] == 0:
                    res[i][j] = 1
        return res

    ####################################################################################################
    def Hint_1(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        for u in hint:
            a[u[0]][u[1]] = 1
        if not isTrue:
            return self.reverseMask(a)
        return a

    def Hint_2(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.M):
                if self.regionMap[i][j] not in hint:
                    a[i][j] = 1
        if not isTrue:
            return self.reverseMask(a)
        return a

    def Hint_3(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.M):
                if self.regionMap[i][j] in hint:
                    a[i][j] = 1
        if not isTrue:
            return self.reverseMask(a)
        return a

    def Hint_4(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        u = hint[0]
        v = hint[1]
        if u[0] > v[0]:
            u[0], v[0] = v[0], u[0]
        if u[1] > v[1]:
            u[1], v[1] = v[1], u[1]
        for i in range(u[0], v[0]+1):
            for j in range(u[1], v[1]+1):
                a[i][j] = 1
        if not isTrue:
            return self.reverseMask(a)
        return self.reverseMask(a)

    def Hint_5(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        u = hint[0]
        v = hint[1]
        if u[0] > v[0]:
            u[0], v[0] = v[0], u[0]
        if u[1] > v[1]:
            u[1], v[1] = v[1], u[1]
        for i in range(u[0], v[0]+1):
            for j in range(u[1], v[1]+1):
                a[i][j] = 1
        if not isTrue:
            return self.reverseMask(a)
        return a

    def distance(self, u, v):
        return abs(u[0] - v[0]) + abs(u[1] - v[1])

    def Hint_6(self, hint, isTrue):
        # always true
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.M):
                u = self.distance([i,j], [self.Ax, self.Ay])
                v = self.distance([i,j], [self.Px, self.Py])
                if hint == "YOU":
                    if u >= v:
                        a[i][j] = 1
                else:
                    if u < v:
                        a[i][j] = 1

        return a

    def Hint_7(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        if hint[0] == 'ROW':
            for i in range(self.N):
                if i != hint[1]:
                    for j in range(self.M):
                        a[i][j] = 1
        else:
            for i in range(self.M):
                if i != hint[1]:
                    for j in range(self.N):
                        a[j][i] = 1
        if not isTrue:
            return self.reverseMask(a)
        return a

    def Hint_8(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        if hint[0] == 'ROW':
            for j in range(self.M):
                a[hint[1]][j] = 1
        else:
            for j in range(self.N):
                a[j][hint[1]] = 1
        if not isTrue:
            return self.reverseMask(a)
        return a

    def Hint_9(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.M):
                isK = False
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x >= 0 and x < self.N and y >= 0 and y < self.M:
                            if self.regionMap[x][y] in hint:
                                isK = True
                if isK:
                    a[i][j] = 1
        if isTrue:
            return self.reverseMask(a)
        return a


    def Hint_10(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        return a

    def Hint_11(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        return a

    def Hint_12(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        u = hint[0]
        v = hint[1]
        if u[0] > v[0]:
            u[0], v[0] = v[0], u[0]
        if u[1] > v[1]:
            u[1], v[1] = v[1], u[1]
        for i in range(self.N):
            if u[0] <= i and i <= v[0]:
                for j in range(self.M):
                    if u[1] <= j and j <= v[1]:
                        a[i][j] = 1
        if not isTrue:
            return self.reverseMask(a)
        return a

    def Hint_13(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        direct = hint[1]
        u = hint[0]
        for i in range(self.N):
            for j in range(self.M):
                X = i - u[0]
                Y = j - u[1]
                lst = []
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
                
                if direct in lst:
                    a[i][j] = 1
        if isTrue:
            return self.reverseMask(a)
        return a

    def Hint_14(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        uX = hint[0][0]
        vX = hint[0][1]
        u = hint[1][0]
        v = hint[1][1]

        for i in range(self.N):
            for j in range(self.M):
                if ((uX[0] <= i and i < u[0]) or (v[0] < i and i <= vX[0])) and uX[1] <= j and j <= vX[1]:
                    a[i][j] = 1
                if ((uX[1] <= j and j < u[1]) or (v[1] < j and j <= vX[1])) and uX[0] <= i and i <= vX[0]:
                    a[i][j] = 1
        if isTrue:
            return self.reverseMask(a)
        return a

    def Hint_15(self, hint, isTrue):
        a = [[0 for j in range(self.M)] for i in range(self.N)]

        for i in range(self.N):
            for j in range(self.M):
                if self.regionMap[i][j] == hint:
                    a[i][j] =1 
        if isTrue:
            return self.reverseMask(a)
        return a

    ####################################################################################################
    def createMask(self, hint, isTrue):
        if hint[0] == 1:
            return self.Hint_1(hint[1], isTrue)
        if hint[0] == 2:
            return self.Hint_2(hint[1], isTrue)
        if hint[0] == 3:
            return self.Hint_3(hint[1], isTrue)
        if hint[0] == 4:
            return self.Hint_4(hint[1], isTrue)
        if hint[0] == 5:
            return self.Hint_5(hint[1], isTrue)
        if hint[0] == 6:
            return self.Hint_6(hint[1], isTrue)
        if hint[0] == 7:
            return self.Hint_7(hint[1], isTrue)
        if hint[0] == 8:
            return self.Hint_8(hint[1], isTrue)
        if hint[0] == 9:
            return self.Hint_9(hint[1], isTrue)
        if hint[0] == 10:
            return self.Hint_10(hint[1], isTrue)
        if hint[0] == 11:
            return self.Hint_11(hint[1], isTrue)
        if hint[0] == 12:
            return self.Hint_12(hint[1], isTrue)
        if hint[0] == 13:
            return self.Hint_13(hint[1], isTrue)
        if hint[0] == 14:
            return self.Hint_14(hint[1], isTrue)
        if hint[0] == 15:
            return self.Hint_15(hint[1], isTrue)
        
        a = [[0 for j in range(self.M)] for i in range(self.N)]
        return a

    def getInformation(self, hint):# [hint number, details] or [0, prison location] prison Reveal
        if hint[0] == 0:
            self.Px = hint[1][0]
            self.Py = hint[1][1]
            return

        self.hintCnt += 1
        self.hintLst.append(self.hintCnt)
        self.hintMAP[self.hintCnt] = hint

    def makeMove(self):
        if self.Px != -1 and self.Py != -1:
            for u in self.hintSIX:
                self.updateMask(u, True)
            self.hintSIX = list()
        
        for i in range(len(self.hintLst)):
            if self.hintLst[i] in self.hintVerified:
                self.hintLst[i] = -1
        self.hintLst.sort()
        while len(self.hintLst) > 0:
            if self.hintLst[0] == -1:
                self.hintLst.pop(0)
            else:
                break
        
        if len(self.hintLst) > 0:
            return [1, self.hintLst[0]]
        else:
            return [4]

    
    def updateMask(self, hint, isTrue):
        if hint[0] == 6:
            
            if not isTrue:
                if hint[1] == 'YOU':
                    hint[1] = 'PRISON'
                else:
                    hint[1] = 'YOU'
                isTrue = True

            if self.Px == -1 or self.Py == -1:
                self.hintSIX.append(hint)
                return

        tmpMask = self.createMask(hint, isTrue)
        
        for i in range(self.N):
            for j in range(self.M):
                if tmpMask[i][j]:
                    self.mask[i][j] = 1

    def getVerification(self, verify):
        self.hintVerified[verify[0]] = verify[1]
        self.updateMask(self.hintMAP[verify[0]], verify[1])

    def getMASK(self):
        return self.mask