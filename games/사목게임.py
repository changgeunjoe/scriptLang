from tkinter import *


MaxRow = 6
MaxCol = 7

from tkinter import *
window = Tk()
_MAXROW = 6
_MAXCOL = 7
process_button = None#하단의 버튼
myText = Label(window, text = "새로 시작", anchor = 'center', width=0, height= 1, fg = 'red', bg = 'blue')
class Cell(Canvas):
    cellStatus = 0
    def __init__(self, row = 0, column = 0,cellnums=0):
        self.color = "white"
        cellnum = cellnums
        cellStatus = 0
        global window
        super().__init__(window, width=20, height=20,bg="blue")
        super().grid(row = row, column = column)
        #global photo_Empty
        #super().configure(image = photo_Empty)
        super().create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        super().bind("<Button-1>", self.clicked)
       # super().bind("<Button-1>", lambda e: self.changePhoto(cellnum = cellnum, obj = self))
    def clicked(self, event): # red 또는 yellow 돌 놓기.
        nextcolor = "red" 
        if self.color != "yellow":
            nextcolor="red" 
        else: 
            nextcolor="red"
        self.setColor(nextcolor)
    def setColor(self, color):
        self.delete("oval") # https://pythonguides.com/python-tkinter-canvas/
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")



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
    myText.grid(row=6, column = 1, padx = 0, sticky = 'n')
    
    window.mainloop()

main()