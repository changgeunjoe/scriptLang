from tkinter import *


MaxRow = 6
MaxCol = 7

class Cell(Canvas):
    pass


def continueColStone(cells):
    for row in cells:
        myContinueStone = 0
        contCnt = 0
        for col in row:
            if myContinueStone ==0 and col.cellStatus !='':
                if col.cellStatus == 'yellow':
                    myContinueStone = 'yellow'
                    contCnt = contCnt + 1
                elif col.cellStatus == 'red':
                    myContinueStone = 'red'
                    contCnt = contCnt + 1
            elif col.cellStatus == myContinueStone:
                contCnt = contCnt + 1
            elif col.cellStatus != myContinueStone:
                contCnt = 0
                myContinueStone = 0
        if contCnt == 4:
            return (4, myContinueStone)
    return (0, 0)


def continueRowStone(cells):
    for col in range(7):
        myContinueStone = 0
        contCnt = 0
        for row in range(6):
            if myContinueStone ==0 and cells[row][col].cellStatus !='':
                if cells[row][col].cellStatus == 'yellow':
                    myContinueStone = 'yellow'
                    contCnt = contCnt + 1
                elif cells[row][col].cellStatus == 'red':
                    myContinueStone = 'red'
                    contCnt = contCnt + 1
            elif cells[row][col].cellStatus == myContinueStone:
                contCnt = contCnt + 1
            elif cells[row][col].cellStatus != myContinueStone:
                contCnt = 0
                myContinueStone = 0
        if contCnt == 4:
            return (4, myContinueStone)
    return (0, 0)


def continuedialogRDStone(cells):
    while(True):
        pass