from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, RGBColor
from docx.shared import Inches
import MapPaint

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
                regionMap[i][j] = int(tmp[j][0])


    

def main(LOG):
    global document
    input()
    
    document = Document()

    for u in LOG:
        document.add_paragraph(u)

        MapPaint.main(1000, 1000, N, M, regionMap, specialMap, boundaryMap)
        document.add_picture("test.png", width=Inches(7))

        document.add_page_break()




    document.save("Visualization.docx")
