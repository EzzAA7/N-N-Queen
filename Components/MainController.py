from tkinter import Tk, Label, Grid, Button, Frame
from Model.Models import *
import copy
import random
import numpy as np


def puzzle_window(root, Num, valueRB, thisBoard=None):
    global frame4

    if thisBoard is None:

        frame4 = Frame()
        root.title("Custom N-Queen Puzzle by Ezz")
        root.geometry("300x300")
        frame4.place(x=10, y=10)
        global frame5
        frame5 = Frame()
        N = Num
        tiles = []
        numOfNodes = N * N
        initial = board(tiles, numOfNodes, N)

        initial.tiles.append(tile(0, -1, -1, "blue"))

        createBasicBoard(root, initial, valueRB)  # A basic board is made

    else:
        initial = thisBoard
        changeButton(root,initial, valueRB)
        IDAstar(initial)
        initial.roundNum +=1
        calQueenConflicts(initial)
        printConflicts(initial)


def createBasicBoard(root, board, valueRB):
    r = 0
    col = 0

    if (board.numOfNodes >= 64):
        board.tileSize = 1
        root.geometry("500x550")
    elif (board.numOfNodes == 16):
        board.tileSize = 2
        root.geometry("200x400")
    elif (board.numOfNodes >= 17 and board.numOfNodes < 64):  # From N=4 to 7
        board.tileSize = 2
        root.geometry("450x480")
    else:
        board.tileSize = 3

    for i in range(1,
                   board.numOfNodes + 1):  # Start coloring tiles and specify button atrributes if random/custom is chosen

        if (board.N % 2 == 0):  # N is even number (even grid of buttons)

            if (r == 0 or r % 2 == 0):  # current row is even number

                if (i % 2 == 0):  # current index is even number
                    if valueRB == 1:  # if chosen method is custom

                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root, board, valueRB, i))

                    else:  # if chosen method is random
                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}')

                    board.tiles.insert(i, tile(i, r, col,
                                               "black"))  # insert created button in list of tile objects at i index) (to start at 1 not 0)

                else:
                    if valueRB == 1:  # if it is random

                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20'),
                                         name=f'btn{i}', command=lambda i=i: tile_clicked(root, board, valueRB, i))
                    else:
                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20'),
                                         name=f'btn{i}')

                    board.tiles.insert(i, tile(i, r, col, "gray"))

                btnName.grid(column=col, row=r)
                col = col + 1
            else:
                if (i % 2 == 0):
                    if valueRB == 1:

                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root, board, valueRB, i))
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
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root, board, valueRB, i))
                    else:
                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}')
                    board.tiles.insert(i, tile(i, r, col, "black"))

                btnName.grid(column=col, row=r)
                col = col + 1

            if (i % board.N == 0):
                r = r + 1
                col = 0
        else:

            if (r == 0 or r % 2 == 0):

                if (i % 2 == 0):
                    if valueRB == 1:

                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root, board, valueRB, i))
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
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root, board, valueRB, i))
                    else:
                        btnName = Button(master=frame4, text=" ", bg="gray", fg="White", width=board.tileSize, height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}')
                    board.tiles.insert(i, tile(i, r, col, "gray"))

                btnName.grid(column=col, row=r)
                col = col + 1
            else:
                if (i % 2 == 0):
                    if valueRB == 1:

                        btnName = Button(master=frame4, text=" ", bg="black", fg="White", width=board.tileSize,
                                         height=1,
                                         font=('Helvetica', '20')
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root, board, valueRB, i))
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
                                         , name=f'btn{i}', command=lambda i=i: tile_clicked(root, board, valueRB, i))
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

    # if valueRB == 1:
    #
    #     startBoard = board(tiles, numOfNodes, board.N)
    if valueRB == 2:
        createColumns(root, board, valueRB)  # if random is chosen then we need create list of columns to choose a random queen in each
        # startBoard = board(tiles, numOfNodes, board.N)    # create object of board using tiles just created


def tile_clicked(root, board, valueRB, btn):  # func to handle clicking a button in custom mode

    board.tiles[btn].isQueen = True  # Clicked tiles is now a count, num of queens is increased and tile is updates
    tile_clicked.counter += 1
    Button(master=frame4, text="Q", bg=board.tiles[btn].colour, fg="White", width=board.tileSize, height=1,
           font=('Helvetica', '20')
           , state="normal").grid(column=board.tiles[btn].column, row=board.tiles[btn].row)

    if (tile_clicked.counter == board.N):  # if we have have board.N number of queens

        for j in range(1, len(board.tiles)):  # then all other board.tiles are unpressable and cant become queens now
            if board.tiles[j].isQueen == False:
                Button(master=frame4, text=" ", bg=board.tiles[j].colour, fg="White", width=board.tileSize, height=1,
                       font=('Helvetica', '20')
                       , state="disabled").grid(column=board.tiles[j].column, row=board.tiles[j].row)

        calQueenConflicts(board)  # check conflicts for each queen
        printConflicts(board)  # print if theres conflicts for each column queen

        if (board.tileSize == 1):
            frame5.place(x=board.N * 40, y=10)
            Button(master=frame5, text="Next", font=('Roboto', '20'), width=4 * board.tileSize, height=1,
                       command=lambda: btnNext(root, board, valueRB)).grid(column=1, row=0)
            Button(master=frame5, text="New", font=('Roboto', '20'), width=4 * board.tileSize, height=1, ).grid(
                column=1, row=1)
        else:
            frame5.place(x=10, y=board.N * 80)
            Button(master=frame5, text="Next", font=('Roboto', '20'), width=2 * board.tileSize, height=1,
                   command=lambda: btnNext(root, board, valueRB)).grid(column=1, row=0)
            Button(master=frame5, text="New", font=('Roboto', '20'), width=2 * board.tileSize, height=1).grid(column=5,
                                                                                                              row=0)

tile_clicked.counter = 0


def createColumns(root, board, valueRB):
    cols = {}
    colTempList = []
    end = int(board.numOfNodes / board.N)

    for i in range(1, end + 1):
        for j in range(1, len(board.tiles)):
            # if i==j:
            #     break
            if board.tiles[i].column == board.tiles[j].column:
                colTempList.append(board.tiles[j])
        cols[f'column{i - 1}'] = copy.deepcopy(colTempList)
        colTempList.clear()

    randomColumnTiles(root, board,valueRB, cols)


def randomColumnTiles(root, board, valueRB, columns):
    randomTiles = []

    for x in columns:
        tempList = columns[x]
        randomVal = random.choice(tempList)
        randomTiles.append(randomVal)

    createRandomBoard(root, board, valueRB, randomTiles)


def createRandomBoard(root, board, valueRB,random):
    for i in range(0, len(random)):
        board.tiles[random[i].num].isQueen = True  # random tiles is now a count and tile is updates
        Button(master=frame4, text="Q", bg=random[i].colour, fg="White", width=board.tileSize, height=1,
               font=('Helvetica', '20')
               , state="normal").grid(column=random[i].column, row=random[i].row)

    calQueenConflicts(board)  # check conflicts for each queen
    printConflicts(board)

    if (board.tileSize == 1):
        frame5.place(x=board.N * 40, y=10)
        Button(master=frame5, text="Next", font=('Roboto', '20'), width=4 * board.tileSize, height=1,
               command=lambda: btnNext(root, board, valueRB)).grid(column=1, row=0)
        Button(master=frame5, text="New", font=('Roboto', '20'), width=4 * board.tileSize, height=1).grid(column=1, row=1)
    else:
        frame5.place(x=10, y=board.N * 80)
        Button(master=frame5, text="Next", font=('Roboto', '20'), width=2 * board.tileSize, height=1,
               command=lambda: btnNext(root, board, valueRB)).grid(column=1, row=0)
        Button(master=frame5, text="New", font=('Roboto', '20'), width=2 * board.tileSize, height=1,
               command=lambda: btnNext(root, board, valueRB)).grid(column=5, row=0)


def calQueenConflicts(board):

    for i in range(1, len(board.tiles)):

        if board.tiles[i].isQueen == True:
            for j in range(1, len(board.tiles)):

                if i == j:
                    continue
                if board.tiles[j].isQueen == True:
                    if board.tiles[i].row == board.tiles[j].row or board.tiles[i].num in indexDiagonal(board, board.tiles[j]):
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

                if board.tiles[i].isQueen == True and board.tiles[i].hasConflicts:
                    Label(master=frame4, text="Y", font=('Roboto', '20')).grid(column=col, row=board.N + 1)
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


def btnNext(root, myboard, valueRB):

    if myboard.roundNum == 0:
        newState = copy.deepcopy(myboard)
        puzzle_window(root, newState.N, valueRB, newState)
    else:
        puzzle_window(root, currentBoard.N, valueRB, currentBoard)

def changeButton(root, newBoard, valueRB):

    Button(master=frame5, text="Next", font=('Roboto', '20'), width=4 * newBoard.tileSize, height=1,
           command=lambda: btnNextAfter(root, newBoard, valueRB)).grid(column=1, row=0)

def btnNextAfter(root, myboard, valueRB):

        newState = copy.deepcopy(myboard)
        puzzle_window(root, currentBoard.N, valueRB, currentBoard)

def IDAstar(board):
    listQueens = []
    board.roundNum += 1
    global currentBoard
    currentBoard=board

    for i in range(1, len(currentBoard.tiles)):  # for loop create a list of queens in the board

        if currentBoard.tiles[i].isQueen is True and currentBoard.tiles[i].hasBeenVisited is False:
            listQueens.append(copy.deepcopy(currentBoard.tiles[i]))

    minF = listQueens[0].f  # for loop to find min F (F=g+h) in list of queens
    leastQueen=copy.deepcopy(listQueens[0])
    for i in range(0, len(listQueens)):
        if listQueens[i].f < minF and listQueens[i].h != 0:  # if less the current then make it least F queen
            minF = listQueens[i].f  # queen with minimum F
            leastQueen = listQueens[i]

    leastColTile = searchIterativeCol(currentBoard, leastQueen, minF)      # get tile with least F value from same column

    for i in range(1,len(currentBoard.tiles)):                             # update h and f values for queens
        if currentBoard.tiles[i].isQueen is True :
            currentBoard.tiles[i].h = 0
            currentBoard.tiles[i].updateF()

    for i in range(1,len(currentBoard.tiles)):                             # exchange the old queen with the new one
        if currentBoard.tiles[i].num == leastColTile.num:
            currentBoard.tiles[i].isQueen = True
            Button(master=frame4, text="Q", bg=currentBoard.tiles[i].colour, fg="White", width=currentBoard.tileSize, height=1,
                   font=('Helvetica', '20')
                   , state="normal").grid(column=currentBoard.tiles[i].column, row=currentBoard.tiles[i].row)
            currentBoard.tiles[i].hasBeenVisited = True

        if currentBoard.tiles[i].num == leastQueen.num:
            currentBoard.tiles[i].isQueen = False
            Button(master=frame4, text=" ", bg=currentBoard.tiles[i].colour, fg="White", width=currentBoard.tileSize, height=1,
                   font=('Helvetica', '20')
                   , state="normal").grid(column=currentBoard.tiles[i].column, row=currentBoard.tiles[i].row)


    print('dddd')
    print("fff")



def searchIterativeCol(idaState, leastQ, minF):
    listF = []

    for i in range(1, len(idaState.tiles)):
        if idaState.tiles[i].column == leastQ.column and idaState.tiles[i].isQueen is False:    # find board.tiles in this column (col)
            listF.append(copy.deepcopy(idaState.tiles[i]))                                               #containing every non queen tiles in column

    print("ddd")

    least = calNodeConflicts(idaState, listF, leastQ)
    return least


def calNodeConflicts(brd, listNonQueen, leastQ):
    tmpBoard=copy.deepcopy(brd)
    leastQ.isQueen = False
                                            #Find F value for each one in column of leasQ
    for i in range(len(listNonQueen)):
        tmpBoard.tiles[listNonQueen[i].num].isQueen = True

        for j in range(1, len(tmpBoard.tiles)):

            if listNonQueen[i].num == j:
                continue
            if tmpBoard.tiles[j].isQueen is True:               # find a queen
                                                            # if same row or digonal with index in list of no non-queens
                if tmpBoard.tiles[listNonQueen[i].num].row == tmpBoard.tiles[j].row or tmpBoard.tiles[listNonQueen[i].num].num in indexDiagonal(tmpBoard, tmpBoard.tiles[j]):
                    # if tmpBoard.tiles[i].row == tmpBoard.tiles[j].row or tmpBoard.tiles[i].num in indexDiagonal(tmpBoard, tmpBoard.tiles[j]):
                    # else:
                    listNonQueen[i].hasConflicts = True
                    listNonQueen[i].h += 1
                    listNonQueen[i].updateF()
                elif tmpBoard.tiles[listNonQueen[i].num].num in indexDiagonalRev(tmpBoard, tmpBoard.tiles[j]):

                    listNonQueen[i].hasConflicts = True
                    listNonQueen[i].h += 1
                    listNonQueen[i].updateF()
        tmpBoard.tiles[listNonQueen[i].num].isQueen = False

    minColF = listNonQueen[0].f
    leastNonQueen = listNonQueen[0]                                          # for loop to find min F (F=g+h) in list of non-queen in column of leasQ queen
    for i in range(0, len(listNonQueen)):
        if listNonQueen[i].f < minColF and listNonQueen[i].h != 0:  # if less the current then make it least F non-queen
            minColF = listNonQueen[i].f                             # non queen with minimum F
            leastNonQueen = listNonQueen[i]

    return leastNonQueen
