
from glob import glob
from tkinter import *

image_o_path = "o.gif"
image_x_path = "x.gif"
image_empty_path = "empty.gif"

statusLabel=['X 차례','O 차례','비겼습니다','x승리입니다','o승리입니다']
cells = [' ', ' ', ' ', 
        ' ', ' ', ' ', 
        ' ', ' ', ' ']

checkox='o'
window = Tk()
photo_Empty = PhotoImage(file = image_empty_path)
photo_O = PhotoImage(file = image_o_path)
photo_X = PhotoImage(file = image_x_path)
cellnum=0
gameTurn = 0

class Cell(Label):
    cellStatus = 0
    def __init__(self, row = 0, column = 0,cellnums=0):
        global window
        global photo_Empty
        global cellnum
        cellnum=cellnums
     
        super().__init__(window, width=34, height=34)
        super().grid(row = row, column = column)
        super().configure(image = photo_Empty)
        super().bind("<Button-1>", lambda e: self.changePhoto())
        #self.winner(cells,checkoxox)
        
    def changePhoto(event):
        global gameTurn
        global cellnum
        if gameTurn == 0:
            super().configure(image = photo_O)
            checkoxox='o'
            #cells[cellnum]='o'
            print(cellnum)
            gameTurn = 1
        else:
            super().configure(image = photo_X)
            checkoxox='x'
            cells[cellnum]='x'
            print(cellnum)
            gameTurn = 0
    
    def setCellStatus(s):
        cellStatus = s

def winner():
    if  (cells[0] == checkox and cells[1] == checkox and cells[2] == checkox) or \
        (cells[3] == checkox and cells[4] == checkox and cells[5] == checkox) or \
        (cells[6] == checkox and cells[7] == checkox and cells[8] == checkox) or \
        (cells[0] == checkox and cells[3] == checkox and cells[6] == checkox) or \
        (cells[1] == checkox and cells[4] == checkox and cells[7] == checkox) or \
        (cells[2] == checkox and cells[5] == checkox and cells[8] == checkox) or \
        (cells[0] == checkox and cells[4] == checkox and cells[8] == checkox) or \
        (cells[2] == checkox and cells[4] == checkox and cells[6] == checkox):
        print(checkox+"비겼습니다.")
        return True
    else:
        return False
def full(cells):
    full = True
    for mark in cells:
        if mark == ' ':
            full = False 
        break
    print("비겼습니다!")
    return full    
def main():
    global window
   
    window.title('Tic-Tac-Toe')
    window.geometry("115x125+450+100")
    window.resizable(False, False)

    board = [
    [Cell(row = 0, column = 0, cellnums=0), Cell(row = 0, column = 1,cellnums=1), Cell(row = 0, column = 2,cellnums=2)],
    [Cell(row = 1, column = 0,cellnums=3), Cell(row = 1, column = 1,cellnums=4), Cell(row = 1, column = 2,cellnums=5)],
    [Cell(row = 2, column = 0,cellnums=6), Cell(row = 2, column = 1,cellnums=7), Cell(row = 2, column = 2,cellnums=8)]]


    window.mainloop()


main()