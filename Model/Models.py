class board():
    def __init__(self, tiles=[], numOfNodes=int, N=int):
        self.roundNum = 0
        self.tiles = tiles
        self.numOfNodes = numOfNodes
        self.N = N
        self.tileSize = 0
        self.goal = False
        self.minF = 1
        self.curLeastQueen = 0
        self.flagChange = -1
        self.listQueens = []

class tile():
    def __init__(self, num, row, column, colour):
        self.isQueen = False
        self.num = num
        self.row = row
        self.column = column
        self.colour = colour
        self.hasConflicts = False
        self.hasBeenVisited = False
        self.h = 0
        self.g = 1
        self.f = 0
        self.updateF()

    def updateF(self):
        self.f = self.g + self.h

    def resetF(self):
        self.h = 0
        self.f = 0
