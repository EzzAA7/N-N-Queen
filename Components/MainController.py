from tkinter import Tk, Label, Grid, Button, Frame
from Model.Models import *
import copy
import random
import numpy as np
from itertools import cycle


def puzzle_window(Num, valueRB, thisBoard=None):
    global frame4, root2

    if thisBoard is None:
        root2 = Tk()
        frame4 = Frame(master=root2)
        root2.title("Custom N-Queen Puzzle by Ezz")
        root2.geometry("300x300")
        frame4.place(x=10, y=10)
        global frame5
        frame5 = Frame(master=root2)
        N = Num
        tiles = []
        numOfNodes = N * N
        initial = board(tiles, numOfNodes, N)
        initial.tiles.append(tile(0, -1, -1, "blue"))
        createBasicBoard(root2, initial, valueRB)  # A basic board is made

    else:
        initial = thisBoard
        changeButton(root2, initial, valueRB)
        isGoal(initial)
        if initial.goal is False:
            IDAstar(initial)
        resetQueen(initial)
        calQueenConflicts(initial)
        printConflicts(initial)


def createBasicBoard(root2, board, valueRB):
    r = 0
    col = 0

    if board.numOfNodes >= 64:
        board.tileSize = 1
        root2.geometry("500x550")
    elif board.numOfNodes == 16:
        board.tileSize = 2
        root2.geometry("200x400")
    elif 17 <= board.numOfNodes < 64:  # From N=4 to 7
        board.tileSize = 2
        root2.geometry("450x480")
    else:
        board.tileSize = 3

    for i in range(1,
                   board.numOfNodes + 1):  # Start coloring tiles and specify button atrributes if random/custom is chosen

        if board.N % 2 == 0:  # N is even number (even grid of buttons)

            if r == 0 or r % 2 == 0:  # current row is even number

                if i % 2 == 0:  # current index is even number
                    if valueRB == 1:  # if chosen method is custom

                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root2, board, valueRB, i))

                    else:  # if chosen method is random
                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}')

                    board.tiles.insert(i, tile(i, r, col,"black"))
                    # insert created button in list of tile objects at i index) (to start at 1 not 0)

                else:
                    if valueRB == 1:  # if it is random

                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20'),
                                         name=f'btn{i}', command=lambda i=i: tile_clicked(root2, board, valueRB, i))
                    else:
                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20'),
                                         name=f'btn{i}')

                    board.tiles.insert(i, tile(i, r, col, "gray"))

                btnName.grid(column=col, row=r)
                col = col + 1
            else:
                if i % 2 == 0:
                    if valueRB == 1:

                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root2, board, valueRB, i))
                    else:
                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}')
                    board.tiles.insert(i, tile(i, r, col, "gray"))

                else:
                    if valueRB == 1:

                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root2, board, valueRB, i))
                    else:
                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}')
                    board.tiles.insert(i, tile(i, r, col, "black"))

                btnName.grid(column=col, row=r)
                col = col + 1

            if i % board.N == 0:
                r = r + 1
                col = 0
        else:

            if r == 0 or r % 2 == 0:

                if i % 2 == 0:
                    if valueRB == 1:

                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root2, board, valueRB, i))
                    else:
                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}')
                    board.tiles.insert(i, tile(i, r, col, "black"))

                else:
                    if valueRB == 1:

                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root2, board, valueRB, i))
                    else:
                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}')
                    board.tiles.insert(i, tile(i, r, col, "gray"))

                btnName.grid(column=col, row=r)
                col = col + 1
            else:
                if i % 2 == 0:
                    if valueRB == 1:

                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root2, board, valueRB, i))
                    else:
                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}')
                    board.tiles.insert(i, tile(i, r, col, "black"))

                else:
                    if valueRB == 1:

                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root2, board, valueRB, i))
                    else:
                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}')
                    board.tiles.insert(i, tile(i, r, col, "gray"))

                btnName.grid(column=col, row=r)
                col = col + 1

            if i % board.N == 0:
                r = r + 1
                col = 0
    finalRow = r

    if valueRB == 2:
        createColumns(root2, board,valueRB)
        # if random is chosen then we need create list of columns to choose a random queen in each


def tile_clicked(root2, board, valueRB, btn):  # func to handle clicking a button in custom mode

    board.tiles[btn].isQueen = True  # Clicked tiles is now a count, num of queens is increased and tile is updates
    tile_clicked.counter += 1
    Button(master=frame4, text="Q", bg=board.tiles[btn].colour, fg="White", width=board.tileSize, height=1,
           font=('Helvetica', '20')
           , state="normal").grid(column=board.tiles[btn].column, row=board.tiles[btn].row)

    if tile_clicked.counter == board.N:  # if we have have board.N number of queens

        for j in range(1, len(board.tiles)):  # then all other board.tiles are unpressable and cant become queens now
            if board.tiles[j].isQueen is False:
                Button(master=frame4, text=" ", bg=board.tiles[j].colour, fg="White", width=board.tileSize, height=1,
                       font=('Helvetica', '20')
                       , state="disabled").grid(column=board.tiles[j].column, row=board.tiles[j].row)

        calQueenConflicts(board)  # check conflicts for each queen
        printConflicts(board)  # print if theres conflicts for each column queen

        if board.tileSize == 1:
            frame5.place(x=board.N * 40, y=10)
            Button(master=frame5, text="Next", font=('Roboto', '20'), width=4 * board.tileSize, height=1,
                   command=lambda: btnNext(root2, board, valueRB)).grid(column=1, row=0)

        else:
            frame5.place(x=10, y=board.N * 80)
            Button(master=frame5, text="Next", font=('Roboto', '20'), width=2 * board.tileSize, height=1,
                   command=lambda: btnNext(root2, board, valueRB)).grid(column=1, row=0)


tile_clicked.counter = 0


def createColumns(root2, board, valueRB):
    cols = {}
    colTempList = []
    end = int(board.numOfNodes / board.N)

    for i in range(1, end + 1):
        for j in range(1, len(board.tiles)):
            if board.tiles[i].column == board.tiles[j].column:
                colTempList.append(board.tiles[j])
        cols[f'column{i - 1}'] = copy.deepcopy(colTempList)
        colTempList.clear()

    randomColumnTiles(root2, board, valueRB, cols)


def randomColumnTiles(root2, board, valueRB, columns):
    randomTiles = []

    for x in columns:
        tempList = columns[x]
        randomVal = random.choice(tempList)
        randomTiles.append(randomVal)

    createRandomBoard(root2, board, valueRB, randomTiles)


def createRandomBoard(root2, board, valueRB, random):
    for i in range(0, len(random)):
        board.tiles[random[i].num].isQueen = True  # random tiles is now a count and tile is updates
        Button(master=frame4, text="Q", bg=random[i].colour, fg="White", width=board.tileSize, height=1,
               font=('Helvetica', '20')
               , state="normal").grid(column=random[i].column, row=random[i].row)

    calQueenConflicts(board)  # check conflicts for each queen
    printConflicts(board)

    if board.tileSize == 1:
        frame5.place(x=board.N * 40, y=10)
        Button(master=frame5, text="Next", font=('Roboto', '20'), width=4 * board.tileSize, height=1,
               command=lambda: btnNext(root2, board, valueRB)).grid(column=1, row=0)
    else:
        frame5.place(x=10, y=board.N * 80)
        Button(master=frame5, text="Next", font=('Roboto', '20'), width=2 * board.tileSize, height=1,
               command=lambda: btnNext(root2, board, valueRB)).grid(column=1, row=0)



def calQueenConflicts(board):
    for i in range(1, len(board.tiles)):

        if board.tiles[i].isQueen is True:
            for j in range(1, len(board.tiles)):

                if i == j:
                    continue
                if board.tiles[j].isQueen is True:
                    if board.tiles[i].row == board.tiles[j].row or board.tiles[i].num in indexDiagonal(board,
                                                                                                       board.tiles[j]):
                        board.tiles[i].hasConflicts = True
                        board.tiles[i].h += 1
                        board.tiles[i].updateF()
                    elif board.tiles[i].num in indexDiagonalRev(board, board.tiles[j]):
                        board.tiles[i].hasConflicts = True
                        board.tiles[i].h += 1
                        board.tiles[i].updateF()


def printConflicts(board):
    flagList = []
    for k in range(0, board.N):
        flagList.insert(k, False)

    for col in range(0, board.N):

        for i in range(1, len(board.tiles)):

            if board.tiles[i].column == col:  # find board.tiles in this column (col)

                if board.tiles[i].isQueen is True and board.tiles[i].hasConflicts is True:
                    Label(master=frame4, text="Y", font=('Roboto', '20')).grid(column=col, row=board.N + 1)
                    Label(master=frame4, text=board.tiles[i].f, font=('Roboto', '20')).grid(column=col, row=board.N + 2)
                    flagList[col] = True
                elif board.tiles[i].isQueen is True and board.tiles[i].hasConflicts is False:
                    Label(master=frame4, text="N", font=('Roboto', '20')).grid(column=col, row=board.N + 1)
                    Label(master=frame4, text=board.tiles[i].f, font=('Roboto', '20')).grid(column=col, row=board.N + 2)
                    flagList[col] = True

    for col in range(0, board.N):
        if flagList[col] is False:
            Label(master=frame4, text="N", font=('Roboto', '20')).grid(column=col, row=board.N + 1)


def indexDiagonal(board, tile):
    giveDiagonalVal(board)
    curIndex = tile.num

    for i in range(len(diaList)):
        if curIndex in diaList[i]:
            return diaList[i]


def indexDiagonalRev(board, tile):
    giveDiagonalVal(board)
    curIndex = tile.num

    for i in range(len(diaListRev)):
        if curIndex in diaListRev[i]:
            return diaListRev[i]


def giveDiagonalVal(board):
    global diaList, diaListRev
    diaList = []
    diaListRev = []

    for i in range(1, board.N + 1):  # Return diagonals of upper matrix
        z = np.arange(i, (board.numOfNodes - board.N * (i - 1)) + 1,
                      board.N + 1).tolist()  # each element is seperated by N+1 and it goes till total nodes - N* i-1
        if z: diaList.append(z)

    j = 1  # Return diagonals of lower matrix
    for k in range(board.N + 1, board.numOfNodes + 1, board.N):
        z = np.arange(k, (board.numOfNodes - j) + 1, board.N + 1).tolist()
        if z: diaList.append(z)  # append diagonals of lower matrix diagonals of upper matrix
        j += 1

    m = board.N
    for i in range(board.N - (board.N - 1), board.N + 1):  # Return diagonals of reverse upper matrix
        z = np.arange(i, (board.numOfNodes - (board.N * m - 1)) + 1, board.N - 1).tolist()
        if z: diaListRev.append(z)  # each element is seperated by N+1 and it goes till total nodes - N* i-1
        m -= 1

    k = 2
    d = board.N  # Return diagonals of reverse lower matrix
    for k in range(k * board.N, board.numOfNodes + 1, board.N):
        z = np.arange(k, (board.numOfNodes - d) + 3, board.N - 1).tolist()
        if z: diaListRev.append(z)  # append diagonals of reverse lower matrix to diagonals of reverse upper matrix
        d -= 1


def btnNext(root2, myboard, valueRB):
    if myboard.roundNum == 0:
        newState = copy.deepcopy(myboard)
        puzzle_window(newState.N, valueRB, newState)
    else:
        puzzle_window(currentBoard.N, valueRB, currentBoard)


def changeButton(root2, newBoard, valueRB):
    Button(master=frame5, text="Next", font=('Roboto', '20'), width=4 * newBoard.tileSize, height=1,
           command=lambda: btnNextAfter(root2, newBoard, valueRB)).grid(column=1, row=0)


def btnNextAfter(root2, myboard, valueRB):
    newState = copy.deepcopy(myboard)
    puzzle_window(currentBoard.N, valueRB, currentBoard)


def IDAstar(board):
    global currentBoard
    board.roundNum += 1
    currentBoard = board

    if board.roundNum == 1 or board.flagChange == 1:    # Create cycle list of queens at start and at restart (flag=1)
        listQueen = []
        # for i in range(1, len(board.tiles)):  # for loop create a list of queens in the board
        #     if board.tiles[i].isQueen is True:
        #         listQueen.append(copy.deepcopy(board.tiles[i]))

        for col in range(0, board.N):
            for i in range(1, len(board.tiles)):
                if board.tiles[i].column == col:  # find board.tiles in this column (col)
                    if board.tiles[i].isQueen is True :
                        listQueen.append(copy.deepcopy(board.tiles[i]))
        uncycle=listQueen
        board.listQueens=cycle(listQueen)
        listQueens = board.listQueens

    else:                                               # not first round nor is there a restart
        listQueens=board.listQueens

    minF = board.minF  # for loop to find min F (F=g+h) in list of queens

    if board.flagChange == -1:                  # first iteration
        leastQueen = next(listQueens)
        leastColTile = searchIterativeCol(board, leastQueen, minF)  # get tile with least F value from same column

    if board.roundNum > 1:
        ogFlag=copy.deepcopy(board.flagChange)
        if ogFlag == 1:
            leastQueen = next(listQueens)                               # get first queen
            leastColTile = searchIterativeCol(board, leastQueen, minF)  # get tile with least F value from same column
            if board.flagChange == 0:
                listQueens = updateQueens(board, listQueens, leastQueen, leastColTile, 1)
                board.listQueens = cycle(listQueens)
                listQueens = board.listQueens
                replaceQueen(board, leastColTile, leastQueen)               # replace queen with tile with new threshold
                leastQueen=next(listQueens)

        elif ogFlag== 0:                   # we found fmin within we need to change to col of next
            leastQueen = next(listQueens)
            leastColTile = searchIterativeCol(board, leastQueen, minF)  # now get tile with least F value from next column
            if board.flagChange == 0:
                listQueens = updateQueens(board, listQueens, leastQueen, leastColTile, 0)
                board.listQueens = cycle(listQueens)
                listQueens = board.listQueens
                replaceQueen(board, leastColTile, leastQueen)
                leastQueen = next(listQueens)

def searchIterativeCol(idaState, leastQ, minF):
    listF = []

    for i in range(1, len(idaState.tiles)):                     # find board.tiles in this column (col)
        if idaState.tiles[i].column == leastQ.column and idaState.tiles[i].isQueen is False:
            listF.append(copy.deepcopy(idaState.tiles[i]))  # containing every non queen tiles in column

    least = calNodeConflicts(idaState, listF, leastQ, minF)
    return least


def calNodeConflicts(brd, listNonQueen, leastQ, minF):
    tmpBoard = copy.deepcopy(brd)
    leastQ.isQueen = False
    # Find F value for each one in column of leasQ
    for i in range(len(listNonQueen)):
        tmpBoard.tiles[listNonQueen[i].num].isQueen = True

        for j in range(1, len(tmpBoard.tiles)):

            if listNonQueen[i].num == j:
                continue
            if tmpBoard.tiles[j].isQueen is True:  # find a queen
                # if same row or diagonal with index in list of no non-queens
                if tmpBoard.tiles[listNonQueen[i].num].row == tmpBoard.tiles[j].row or tmpBoard.tiles[listNonQueen[i].num].num in indexDiagonal(tmpBoard, tmpBoard.tiles[j]):
                    listNonQueen[i].hasConflicts = True
                    listNonQueen[i].h += 1
                    listNonQueen[i].updateF()
                elif tmpBoard.tiles[listNonQueen[i].num].num in indexDiagonalRev(tmpBoard, tmpBoard.tiles[j]):
                    listNonQueen[i].hasConflicts = True
                    listNonQueen[i].h += 1
                    listNonQueen[i].updateF()
        tmpBoard.tiles[listNonQueen[i].num].isQueen = False

    minColF = listNonQueen[0].f         # only at the start
    leastNonQueen = None     # for loop to find min F (F=g+h) in list of non-queen in column of leasQ queen
    for i in range(0, len(listNonQueen)):
        Label(master=frame4, text=listNonQueen[i].f, font=('Roboto', '20')).grid(column=tmpBoard.N + 1,
                                                                                 row=listNonQueen[i].row)
        if listNonQueen[i].f <= minF and listNonQueen[i].h != 0 and listNonQueen[i].hasBeenVisited is False:
            # if less the current then make it least F non-queen
            leastNonQueen = listNonQueen[i]                         # non queen with F less than threshold
            brd.flagChange = 0                                      # no change in threshold, change column
            break

    if leastNonQueen is None:       # if none less than threshold
        leastNonQueen = leastNotVisitedChild(tmpBoard,listNonQueen)
        brd.minF = leastNonQueen.f                                  # fmin is now value of least non visited in col
        brd.flagChange = 1                                          # change in threshold, restart with new threshold

    return leastNonQueen


def leastNotVisitedChild(tmpBoard, listNonQueen, ):

    minColF = listNonQueen[0].f
    leastNonQueen = listNonQueen[0]  # for loop to find min F (F=g+h) in list of non-queen in column of leasQ queen
    for i in range(0, len(listNonQueen)):
        Label(master=frame4, text=listNonQueen[i].f, font=('Roboto', '20')).grid(column=tmpBoard.N + 1,
                                                                                 row=listNonQueen[i].row)
        if listNonQueen[i].f < minColF and listNonQueen[i].h != 0 and listNonQueen[i].hasBeenVisited is False:
            # if less the current then make it least F non-queen
            minF = listNonQueen[i].f  # non queen with minimum F
            leastNonQueen = listNonQueen[i]

    return leastNonQueen


def replaceQueen(brd, leastColTile, leastQueen):

    resetQueen(brd)

    for i in range(1, len(brd.tiles)):  # exchange the old queen with the new one
        if brd.tiles[i].num == leastColTile.num:
            brd.tiles[i].isQueen = True
            brd.tiles[i].hasConflicts = False             # since they will be re calculated
            brd.tiles[i].hasBeenVisited = True
            Button(master=frame4, text="Q", bg=brd.tiles[i].colour, fg="Red", width=brd.tileSize, height=1,
                   font=('Helvetica', '20')
                   , state="normal").grid(column=brd.tiles[i].column, row=brd.tiles[i].row)

        if brd.tiles[i].num == leastQueen.num:            # original column queen
            brd.tiles[i].isQueen = False
            brd.tiles[i].hasConflicts = False
            # brd.tiles[i].hasBeenVisited = True
            Button(master=frame4, text=" ", bg=brd.tiles[i].colour, fg="White", width=brd.tileSize, height=1,
                   font=('Helvetica', '20')
                   , state="normal").grid(column=brd.tiles[i].column, row=brd.tiles[i].row)


def resetQueen(brd):

    for i in range(1, len(brd.tiles)):  # reset h and f values for queens
        if brd.tiles[i].isQueen is True:
            brd.tiles[i].hasConflicts = False
            brd.tiles[i].h = 0
            brd.tiles[i].updateF()


def updateQueens(brd, listOfQueens, leastQ, leastTile, flg):

    tmpList = [leastQ]
    for i in range(0, brd.N):
        tmpList.append(next(listOfQueens))
    uniqueList = []
    for item in tmpList:
        if item not in uniqueList:
            uniqueList.append(item)
    ls = [leastTile if (x.num == leastQ.num) else x for x in uniqueList]

    return ls


def isGoal(brd):
    counter = 0
    for i in range(1, len(brd.tiles)):  # loop to check is goal is reached
        if brd.tiles[i].isQueen is True:
            if brd.tiles[i].f == 1:  # all have f=1 means all queens have no conflicts
                counter += 1
    if counter == brd.N:
        brd.goal = True