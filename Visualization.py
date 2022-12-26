from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, RGBColor
from docx.shared import Inches
import MapPaint
import random

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
                if tmp[j][-1] not in "0123456789":
                    specialMap[i][j] = tmp[j][-1]
                    regionMap[i][j] = int(tmp[j][:len(tmp[j])-1])
                else:
                    regionMap[i][j] = int(tmp[j])


    

def main(LOG):
    global document
    input()

    colorMap = [(255, 204, 204), (153, 255, 51), (0, 255, 0), (255, 204, 153), (255, 255, 102),
                (0, 204, 102), (0, 153, 153), (255, 51, 51), (192, 192, 192), (96, 96, 96),
                (255, 0, 127), (255, 204, 255), (102, 102, 255), (51, 255, 153), (51, 51, 0),
                (255, 230, 102), (12, 26, 22), (7, 57, 20), (64, 83, 13), (44, 43, 76)]
    random.shuffle(colorMap)
    colorMap = [(0, 0, 102)] + colorMap
    
    document = Document()
    
    for u in LOG:
        document.add_paragraph(u)


        MapPaint.main(1600, 1600, N, M, regionMap, specialMap, boundaryMap, Tx, Ty, colorMap)
        document.add_picture("test.png", width=Inches(7))

        document.add_page_break()




    document.save("Visualization.docx")
