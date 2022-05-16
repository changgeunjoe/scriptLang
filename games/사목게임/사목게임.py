from tkinter import *

currentcolor = 'red'
window = Tk()
winner = 4
gameturn = 1

_MAXROW = 6
_MAXCOL = 7
process_button = None  # 하단의 버튼
myText = Button(window, text="red의 차례", anchor='center',
                width=7, height=1, fg='red', bg='blue')

board = [[]]

def continueColStone():
    global board
    rowC=0
    while(rowC < 6):        
        myContinueStone = ''
        contCnt = 0
        col=0
        while(col < 7):
            if contCnt == 0 and board[rowC][col].cellStatus != '':
                if board[rowC][col].cellStatus == 'yellow':
                    myContinueStone = 'yellow'
                    contCnt = contCnt + 1
                elif board[rowC][col].cellStatus == 'red':
                    myContinueStone = 'red'
                    contCnt = contCnt + 1
            elif board[rowC][col].cellStatus == myContinueStone and myContinueStone != '':
                contCnt = contCnt + 1
            elif board[rowC][col].cellStatus != myContinueStone:
                contCnt = 0
                myContinueStone = ''
            if contCnt == 4:
                return (rowC, col, myContinueStone)
            col = col + 1    
        if contCnt == 4:
                return (rowC, col, myContinueStone)
        rowC = rowC + 1
    return (-1, -1, '')


def continueRowStone():
    global board
    colC = 0
    while(colC < 7):
        myContinueStone = ''
        contCnt = 0
        row = 0
        while(row < 6):
            if contCnt == 0 and board[row][colC].cellStatus != '':
                if board[row][colC].cellStatus == 'yellow':
                    myContinueStone = 'yellow'
                    contCnt = contCnt + 1
                elif board[row][colC].cellStatus == 'red':
                    myContinueStone = 'red'
                    contCnt = contCnt + 1
            elif board[row][colC].cellStatus == myContinueStone and myContinueStone != '':
                contCnt = contCnt + 1
            elif board[row][colC].cellStatus != myContinueStone:
                contCnt = 0
                myContinueStone = ''
            if contCnt == 4:
                return (row, colC, myContinueStone)
            row = row + 1
        if contCnt == 4:
            return (row, colC, myContinueStone)
        colC = colC + 1
    return (-1,-1, '')


def continuedialogRDStone():
    global board
    for rowW in range(6):        
        contiStone = ''
        countCnt = 0
        col = 0
        row = rowW
        while(row < 6 and col < 7):
            if countCnt != 0:
                if board[row][col].cellStatus == contiStone:
                    countCnt += 1
                elif board[row][col].cellStatus != contiStone:
                    contiStone = ''
                    countCnt = 0
            elif board[row][col].cellStatus != '':
                contiStone = board[row][col].cellStatus
                countCnt += 1
            if countCnt == 4:
                return (row, col, contiStone)
            row += 1
            col += 1

    for colW in range(1, 6):
        contiStone = ''
        countCnt = 0
        col = colW
        row = 0
        while(row < 6 and col < 7):
            if countCnt != 0:
                if board[row][col].cellStatus == contiStone:
                    countCnt += 1
                elif board[row][col].cellStatus != contiStone:
                    contiStone = ''
                    countCnt = 0
            elif board[row][col].cellStatus != '':
                contiStone = board[row][col].cellStatus
                countCnt += 1
            if countCnt == 4:
                return (row, col, contiStone)
            row += 1
            col += 1
    return (-1, -1, '')


def continuedialogLDStone():
    global board
    for rowW in range(6):
        contiStone = ''
        countCnt = 0
        col = 6
        row = rowW
        while(row < 6 and col < 7):
            if countCnt != 0:
                if board[row][col].cellStatus == contiStone:
                    countCnt += 1
                elif board[row][col].cellStatus != contiStone:
                    contiStone = ''
                    countCnt = 0
            elif board[row][col].cellStatus != '':
                contiStone = board[row][col].cellStatus
                countCnt += 1
            if countCnt == 4:
                return (row, col, contiStone)
            row += 1
            col -= 1
    for colW in range(1, 7):
        contiStone = ''
        countCnt = 0
        col = colW
        row = 0
        while(row < 6 and col < 7):
            if countCnt != 0:
                if board[row][col].cellStatus == contiStone:
                    countCnt += 1
                elif board[row][col].cellStatus != contiStone:
                    contiStone = ''
                    countCnt = 0
            elif board[row][col].cellStatus != '':
                contiStone = board[row][col].cellStatus
                countCnt += 1
            if countCnt == 4:
                return (row, col, contiStone)
            row += 1
            col -= 1
    return (-1, -1, '')

def changeText():
    global gameturn
    global myText
    global winner
    if winner == 1:
        myText['text'] = "red의 승리"
    elif winner == 2:
        myText['text'] = "yellow 승리"
    elif winner == 0:
        myText['text'] = "비겼습니다"
    elif gameturn == 0 and winner == 4:
        myText['text'] = "yellow의 차례"
    elif gameturn == 1 and winner == 4:
        myText['text'] = "red의 차례"





def checkFloorPosition(myRow=-1, myCol=-1):
    if myRow == -1 or myCol == -1:
        return False
    elif board[myRow][myCol].cellStatus != '':
        return False
    elif myRow == 5:
        return True
    elif board[myRow + 1][myCol].cellStatus != '':
        return True

class Cell(Canvas):
    cellStatus = ""

    def __init__(self, row=0, column=0, cellnums=0):
        self.color = "white"
        self.row = row
        self.col = column
        cellnum = cellnums
        cellStatus = ""
        global window
        super().__init__(window, width=20, height=20, bg="blue")
        super().grid(row=row, column=column)
        #global photo_Empty
        #super().configure(image = photo_Empty)
        super().create_oval(4, 4, 20, 20, fill="white", tags="oval")
        super().bind("<Button-1>", lambda e: self.clicked(obj=self))
       # super().bind("<Button-1>", lambda e: self.changePhoto(cellnum = cellnum, obj = self))

    def clicked(event, obj):  # red 또는 yellow 돌 놓기.
        global currentcolor
        global winner
        global gameturn
        if str(continueRowStone()) == 'red' or str(continueColStone()) == 'red' or str(continuedialogRDStone()) == 'red' or str(continuedialogLDStone()) == 'red':
            pass
        elif str(continueRowStone()) == 'red' or str(continueColStone()) == 'yellow' or str(continuedialogRDStone()) == 'yellow' or str(continuedialogLDStone()) == 'yellow':
            pass

        elif checkFloorPosition(obj.row, obj.col):
            if currentcolor == "red":
                obj.cellStatus = currentcolor
                currentcolor = "yellow"
            elif currentcolor == "yellow":
                obj.cellStatus = currentcolor
                currentcolor = "red"
            obj.setColor(color=obj.cellStatus)
        if gameturn == 0:
            gameturn = 1
        elif gameturn == 1:
            gameturn = 0
        if continueRowStone()[2] == 'red':
            winner = 1
            setLineUp(continueRowStone()[0], continueRowStone()[1], continueRowStone()[2])
            obj.create_oval(4, 4, 20, 20, tags="oval")
        elif continueColStone()[2] == 'red':
            winner = 1
            setLineLeft(continueRowStone()[0], continueRowStone()[1], continueRowStone()[2])
            #obj.create_oval(4, 4, 20, 20, fill="blue", tags="oval")
        elif continuedialogRDStone()[2] == 'red':
            winner = 1
            obj.create_oval(4, 4, 20, 20, fill="blue", tags="oval")
        elif continuedialogLDStone()[2] == 'red':
            winner = 1
            obj.create_oval(4, 4, 20, 20, fill="blue", tags="oval")

        elif continueRowStone()[2] == 'yellow':
            winner = 2
            obj.create_oval(4, 4, 20, 20, fill="blue", tags="oval")
        elif continueColStone()[2] == 'yellow':
            winner = 2
            obj.create_oval(4, 4, 20, 20, fill="blue", tags="oval")
        elif continuedialogRDStone()[2] == 'yellow':
            winner = 2
            obj.create_oval(4, 4, 20, 20, fill="blue", tags="oval")
        elif continuedialogLDStone()[2] == 'yellow':
            winner = 2
            obj.create_oval(4, 4, 20, 20, fill="blue", tags="oval")
        changeText()

    def setColor(self, color):
        self.delete("oval")  # https://pythonguides.com/python-tkinter-canvas/
        self.color = color
        self.create_oval(4, 4, 20, 20, fill=self.color, tags="oval")


def setLineLeft(row = 0, col = 0, color = 'blue'):
    for x in range(col - 4 , col):
        board[row][x].configure = color


def setLineUp(row = 0, col = 0, color = 'blue'):
    for x in range(row - 4 , row):
        board[x][col].configure = color


def setDialogLU(row = 0, col = 0, color = 'blue'):
    for x in range(row - 4 , row):
        for y in range(col - 4, col):
            board[x][y].configure = color

def setDialogRU(row = 0, col = 0, color = 'blue'):
    for x in range(row - 4 , row):
        for y in range(col, col + 4):
            board[x][y].configure = color

def main():
    global window

    window.title('Tic-Tac-Toe')
    window.geometry("270x145+450+100")
    
    global board
    board = [
    [Cell(row=0, column=0, cellnums=0), Cell(row=0, column=1, cellnums=1), Cell(row=0, column=2, cellnums=2), Cell(
        row=0, column=3, cellnums=3), Cell(row=0, column=4, cellnums=4), Cell(row=0, column=5, cellnums=5), Cell(row=0, column=6, cellnums=6)],
    [Cell(row=1, column=0, cellnums=0), Cell(row=1, column=1, cellnums=1), Cell(row=1, column=2, cellnums=2), Cell(
        row=1, column=3, cellnums=3), Cell(row=1, column=4, cellnums=4), Cell(row=1, column=5, cellnums=5), Cell(row=1, column=6, cellnums=6)],
    [Cell(row=2, column=0, cellnums=0), Cell(row=2, column=1, cellnums=1), Cell(row=2, column=2, cellnums=2), Cell(
        row=2, column=3, cellnums=3), Cell(row=2, column=4, cellnums=4), Cell(row=2, column=5, cellnums=5), Cell(row=2, column=6, cellnums=6)],
    [Cell(row=3, column=0, cellnums=0), Cell(row=3, column=1, cellnums=1), Cell(row=3, column=2, cellnums=2), Cell(
        row=3, column=3, cellnums=3), Cell(row=3, column=4, cellnums=4), Cell(row=3, column=5, cellnums=5), Cell(row=3, column=6, cellnums=6)],
    [Cell(row=4, column=0, cellnums=0), Cell(row=4, column=1, cellnums=1), Cell(row=4, column=2, cellnums=2), Cell(
        row=4, column=3, cellnums=3), Cell(row=4, column=4, cellnums=4), Cell(row=4, column=5, cellnums=5), Cell(row=4, column=6, cellnums=6)],
    [Cell(row=5, column=0, cellnums=0), Cell(row=5, column=1, cellnums=1), Cell(row=5, column=2, cellnums=2), Cell(
        row=5, column=3, cellnums=3), Cell(row=5, column=4, cellnums=4), Cell(row=5, column=5, cellnums=5), Cell(row=5, column=6, cellnums=6)]
    ]
    #myText.grid(row=6, column = 1, padx = 0, sticky = 'n')
    # myText.pack()
    # myText.grid(6,1)
    # myText.create_text(150,100,text="dddddd",font=(20),fill="blue")
    myText.grid(row=1, column=9, padx=0, sticky='n')
    window.mainloop()


main()
