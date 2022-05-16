from tkinter import *
MaxRow = 6
MaxCol = 7
currentcolor = 'red'
from tkinter import *
window = Tk()
winner=4
gameturn=0
_MAXROW = 6
_MAXCOL = 7
process_button = None#하단의 버튼
myText = Button(window, text = "red의 차례", anchor = 'center', width=7, height= 1, fg = 'red', bg = 'blue')
class Cell(Canvas):
    cellStatus = ""
    def __init__(self, row = 0, column = 0,cellnums=0):
        self.color = "white"
        self.row = row
        self.col = column
        cellnum = cellnums
        cellStatus = ""
        global window
        super().__init__(window, width=20, height=20,bg="blue")
        super().grid(row = row, column = column)
        #global photo_Empty
        #super().configure(image = photo_Empty)
        super().create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        super().bind("<Button-1>", self.clicked)
       # super().bind("<Button-1>", lambda e: self.changePhoto(cellnum = cellnum, obj = self))
    def clicked(self, event): # red 또는 yellow 돌 놓기.
        global currentcolor
        global winner
        global gameturn
        if str(continueRowStone()) == 'red' or str(continueColStone())=='red' or str(continuedialogRDStone())=='red' or str(continuedialogLDStone())=='red':
            winner = 1
            print("red")
        elif str(continueRowStone()) == 'red' or str(continueColStone())=='yellow' or str(continuedialogRDStone())=='yellow' or str(continuedialogLDStone())=='yellow':
            winner =2
            print("yellow")

        elif checkFloorPosition(self.row, self.col):
            if currentcolor == "red":
                self.cellStatus = currentcolor
                currentcolor="yellow"
            elif currentcolor == "yellow":
                self.cellStatus= currentcolor
                currentcolor="red"
            self.setColor(color = self.cellStatus)
        if gameturn == 0:
            gameturn=1
        else:
            gameturn =0
        changeText()

    def setColor(self, color):
        self.delete("oval") # https://pythonguides.com/python-tkinter-canvas/
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")
def changeText():
    global gameturn
    global myText
    global winner
    if winner == 1:
        myText['text'] = "red의 승리"
    elif winner == 2:
        myText['text'] = "yellow 승리"
    elif winner == 0:
            myText['text']= "비겼습니다"
    elif gameturn == 0 and  winner == 4:
        myText['text'] = "yellow의 차례"
    elif gameturn == 1 and winner == 4:
        myText['text'] = "red의 차례"

def continueColStone():
    global board
    for row in board:
        myContinueStone = ''
        contCnt = 0
        for col in row:
            if myContinueStone == '' and col.cellStatus !='':
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
            return myContinueStone
    return ''    




def continueRowStone():
    global board
    for col in range(7):
        myContinueStone = ''
        contCnt = 0
        for row in range(6):
            if myContinueStone == '' and board[row][col].cellStatus != '':
                if board[row][col].cellStatus == 'yellow':
                    myContinueStone = 'yellow'
                    contCnt = contCnt + 1
                elif board[row][col].cellStatus == 'red':
                    myContinueStone = 'red'
                    contCnt = contCnt + 1
            elif board[row][col].cellStatus == myContinueStone:
                contCnt = contCnt + 1
            elif board[row][col].cellStatus != myContinueStone:
                contCnt = 0
                myContinueStone = 0
        if contCnt == 4:
            return myContinueStone
    return ''


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
                contiStone  = board[row][col].cellStatus
                countCnt += 1
            if countCnt == 4:
                return contiStone
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
                contiStone  = board[row][col].cellStatus
                countCnt += 1
            if countCnt == 4:
                return contiStone
            row += 1
            col += 1        
    return ''

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
                contiStone  = board[row][col].cellStatus
                countCnt += 1
            if countCnt == 4:
                return contiStone
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
                contiStone  = board[row][col].cellStatus
                countCnt += 1
            if countCnt == 4:
                return contiStone
            row += 1
            col -= 1
    return ''


def checkFloorPosition(myRow = -1, myCol = -1):
    if myRow == -1 or myCol == -1:
        return False
    elif board[myRow][myCol].cellStatus != '':
        return False
    elif myRow == 5:
        return True
    elif board[myRow + 1][myCol].cellStatus != '':
        return True
    

def main():
    global window
   
    window.title('Tic-Tac-Toe')
    window.geometry("133x145+450+100")

    global board
    board = [
    [Cell(row = 0, column = 0, cellnums=0), Cell(row = 0, column = 1,cellnums=1), Cell(row = 0, column = 2,cellnums=2),Cell(row = 0, column = 3,cellnums=3),Cell(row = 0, column = 4,cellnums=4),Cell(row = 0, column = 5,cellnums=5),Cell(row = 0, column = 6,cellnums=6)],
    [Cell(row = 1, column = 0, cellnums=0), Cell(row = 1, column = 1,cellnums=1), Cell(row = 1, column = 2,cellnums=2),Cell(row = 1, column = 3,cellnums=3),Cell(row = 1, column = 4,cellnums=4),Cell(row = 1, column = 5,cellnums=5),Cell(row = 1, column = 6,cellnums=6)],
    [Cell(row = 2, column = 0, cellnums=0), Cell(row = 2, column = 1,cellnums=1), Cell(row = 2, column = 2,cellnums=2),Cell(row = 2, column = 3,cellnums=3),Cell(row = 2, column = 4,cellnums=4),Cell(row = 2, column = 5,cellnums=5),Cell(row = 2, column = 6,cellnums=6)],
    [Cell(row = 3, column = 0, cellnums=0), Cell(row = 3, column = 1,cellnums=1), Cell(row = 3, column = 2,cellnums=2),Cell(row = 3, column = 3,cellnums=3),Cell(row = 3, column = 4,cellnums=4),Cell(row = 3, column = 5,cellnums=5),Cell(row = 3, column = 6,cellnums=6)],
    [Cell(row = 4, column = 0, cellnums=0), Cell(row = 4, column = 1,cellnums=1), Cell(row = 4, column = 2,cellnums=2),Cell(row = 4, column = 3,cellnums=3),Cell(row = 4, column = 4,cellnums=4),Cell(row = 4, column = 5,cellnums=5),Cell(row = 4, column = 6,cellnums=6)],
    [Cell(row = 5, column = 0, cellnums=0), Cell(row = 5, column = 1,cellnums=1), Cell(row = 5, column = 2,cellnums=2),Cell(row = 5, column = 3,cellnums=3),Cell(row = 5, column = 4,cellnums=4),Cell(row = 5, column = 5,cellnums=5),Cell(row = 5, column = 6,cellnums=6)]]
    #myText.grid(row=6, column = 1, padx = 0, sticky = 'n')
    #myText.pack()
    #myText.grid(6,1)
    #myText.create_text(150,100,text="dddddd",font=(20),fill="blue")
    myText.grid(row=1, column = 9, padx = 0, sticky = 'n')
    window.mainloop()
    

main()