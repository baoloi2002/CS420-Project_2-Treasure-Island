class Agent:
    def __init__(self, N, M, regionMap, specialMap, Ax, Ay) -> None:
        self.N = N
        self.M = M
        self.regionMap = regionMap
        self.specialMap = specialMap
        self.Ax = Ax
        self.Ay = Ay

        self.isFree = False
        self.mask = [[0 for j in range(M)] for i in range(N)]
        self.hintNotVerify = []
        self.hintNear = []
        self.hintCnt = 0

    def find(self, tmpMask):
        cnt = 0
        for i in range(self.N):
            for j in range(self.M):
                if self.mask[i][j] == 0 and tmpMask[i][j] == 1:
                    cnt += 1
        return cnt


    def reverseMask(self, tmpMask):
        res = [[0 for j in range(M)] for i in range(N)]
        for i in range(self.N):
            for j in range(self.M):
                if tmpMask[i][j] == 0:
                    res[i][j] = 1
        return res

    def createMask(self, hint):
        pass

    def isNeedToVerify(self, hint):
        if hint[0] == 0:
            return False
        tmpMask = self.createMask(hint)
        revMask = self.reverseMask(tmpMask)
        if self.find(tmpMask) + self.find(revMask) > 0:
            return True
        return False

    def getInformation(self, hint):# [hint number, details] or [0, prison location] pirate Reveal
        self.hintCnt += 1
        if hint[0] == 0:
            pass
        if self.isNeedToVerify(hint):
            pass

    def makeMove(selft):
        return [4]
    
    def getVerification(selft, verify):
        pass