
from cgitb import reset
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
gameTurn = 0

myText = Label(window, text = "o의 차례", anchor = 'center', width=0, height= 2, fg = 'red', bg = 'blue')
        
def changeText():
    global gameTurn
    global myText
    
    if winner()==1:
        myText['text'] = checkox+"의 승리"
    elif winner()==0:
            myText['text']= "비겼습니다"
    elif gameTurn == 0 and  winner()==4:
        myText['text'] = "o의 차례"
    elif gameTurn == 1 and winner()==4:
        myText['text'] = "x의 차례"
 

class Cell(Label):
    cellStatus = 0
    def __init__(self, row = 0, column = 0,cellnums=0):
        global window
        global photo_Empty
        cellnum = cellnums
        cellStatus = 0
        super().__init__(window, width=37, height=34)
        super().grid(row = row, column = column)
        super().configure(image = photo_Empty)
        super().bind("<Button-1>", lambda e: self.changePhoto(cellnum = cellnum, obj = self))
        #self.winner(cells,checkoxox)
        
    def changePhoto(event, cellnum = -1, obj = NONE):
        global gameTurn
        if gameTurn == 0 and obj.cellStatus == 0:
            super().configure(image = photo_O)
            checkoxox='o'
            obj.cellStatus = 1
            cells[cellnum]='o'
            print(obj.cellStatus)
            winner()
            gameTurn = 1
        elif gameTurn == 1 and obj.cellStatus == 0:
            super().configure(image = photo_X)
            checkoxox='x'
            obj.cellStatus = 2
            cells[cellnum]='x'
            print(obj.cellStatus)
            winner()
            gameTurn = 0
        changeText()
    

def winner():
    for i in cells: 
            if  i ==' ':
                return 4 
    if  (cells[0] == checkox and cells[1] == checkox and cells[2] == checkox) or \
        (cells[3] == checkox and cells[4] == checkox and cells[5] == checkox) or \
        (cells[6] == checkox and cells[7] == checkox and cells[8] == checkox) or \
        (cells[0] == checkox and cells[3] == checkox and cells[6] == checkox) or \
        (cells[1] == checkox and cells[4] == checkox and cells[7] == checkox) or \
        (cells[2] == checkox and cells[5] == checkox and cells[8] == checkox) or \
        (cells[0] == checkox and cells[4] == checkox and cells[8] == checkox) or \
        (cells[2] == checkox and cells[4] == checkox and cells[6] == checkox):
        return 1
    else:
        return 0


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
    window.geometry("133x145+450+100")
    #window.resizable(False, False)

    board = [
    [Cell(row = 0, column = 0, cellnums=0), Cell(row = 0, column = 1,cellnums=1), Cell(row = 0, column = 2,cellnums=2)],
    [Cell(row = 1, column = 0,cellnums=3), Cell(row = 1, column = 1,cellnums=4), Cell(row = 1, column = 2,cellnums=5)],
    [Cell(row = 2, column = 0,cellnums=6), Cell(row = 2, column = 1,cellnums=7), Cell(row = 2, column = 2,cellnums=8)]]

    myText.grid(row=3, column = 1, padx = 0, sticky = 'n')
    
    


    window.mainloop()


main()
