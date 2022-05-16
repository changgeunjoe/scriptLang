from tkinter import *

image_o_path = "o.gif"
image_x_path = "x.gif"
image_empty_path = "empty.gif"

window = Tk()
photo_Empty = PhotoImage(file = image_empty_path)
photo_O = PhotoImage(file = image_o_path)
photo_X = PhotoImage(file = image_x_path)
gameTurn = 0

myText = Label(window, text = "o의 차례", anchor = 'center', width=0, height= 2, fg = 'red', bg = 'blue')
        
def changeText():
    global gameTurn
    global myText
    
    if winner() == 1:
        myText['text'] = "o의 승리"
    elif winner() == 2:
        myText['text'] = "x의 승리"
    elif winner() == 0:
            myText['text']= "비겼습니다"
    elif gameTurn == 0 and  winner() == 4:
        myText['text'] = "o의 차례"
    elif gameTurn == 1 and winner() == 4:
        myText['text'] = "x의 차례"
 

class Cell(Label):
    cellStatus = 0
    def __init__(self, row = 0, column = 0,cellnums=0):
        cellnum = cellnums
        cellStatus = 0
        global window
        super().__init__(window, width=37, height=34)
        super().grid(row = row, column = column)
        global photo_Empty
        super().configure(image = photo_Empty)
        super().bind("<Button-1>", lambda e: self.changePhoto(cellnum = cellnum, obj = self))
        
    def changePhoto(event, cellnum = -1, obj = NONE):
        if winner()==1:
            return
        global gameTurn
        if gameTurn == 0 and obj.cellStatus == 0:
            super().configure(image = photo_O)
            obj.cellStatus = 1            
            gameTurn = 1
        elif gameTurn == 1 and obj.cellStatus == 0:
            super().configure(image = photo_X)
            obj.cellStatus = 2
            gameTurn = 0
        changeText()

    def getCellStatus(self):
        return int(self.cellStatus)
    

def winner():
    global board
    if  (board[0][0].getCellStatus() == board[0][1].getCellStatus() == board[0][2].getCellStatus() == 1) or \
        (board[1][0].getCellStatus() == board[1][1].getCellStatus() == board[1][2].getCellStatus() == 1) or \
        (board[2][0].getCellStatus() == board[2][1].getCellStatus() == board[2][2].getCellStatus() == 1) or \
        (board[0][0].getCellStatus() == board[1][0].getCellStatus() == board[2][0].getCellStatus() == 1) or \
        (board[0][1].getCellStatus() == board[1][1].getCellStatus() == board[2][1].getCellStatus() == 1) or \
        (board[0][2].getCellStatus() == board[1][2].getCellStatus() == board[2][2].getCellStatus() == 1) or \
        (board[0][0].getCellStatus() == board[1][1].getCellStatus() == board[2][2].getCellStatus() == 1) or \
        (board[0][2].getCellStatus() == board[1][1].getCellStatus() == board[2][0].getCellStatus() == 1):
        return 1
    elif  (board[0][0].getCellStatus() == board[0][1].getCellStatus() == board[0][2].getCellStatus() == 2) or \
        (board[1][0].getCellStatus() == board[1][1].getCellStatus() == board[1][2].getCellStatus() == 2) or \
        (board[2][0].getCellStatus() == board[2][1].getCellStatus() == board[2][2].getCellStatus() == 2) or \
        (board[0][0].getCellStatus() == board[1][0].getCellStatus() == board[2][0].getCellStatus() == 2) or \
        (board[0][1].getCellStatus() == board[1][1].getCellStatus() == board[2][1].getCellStatus() == 2) or \
        (board[0][2].getCellStatus() == board[1][2].getCellStatus() == board[2][2].getCellStatus() == 2) or \
        (board[0][0].getCellStatus() == board[1][1].getCellStatus() == board[2][2].getCellStatus() == 2) or \
        (board[0][2].getCellStatus() == board[1][1].getCellStatus() == board[2][0].getCellStatus() == 2):
        return 2
   
    for i in board:
        for j in i:
            if  j.getCellStatus() == 0:
                return 4
    return 0

board = list   

def main():
    global window
   
    window.title('Tic-Tac-Toe')
    window.geometry("133x145+450+100")

    global board
    board = [
    [Cell(row = 0, column = 0, cellnums=0), Cell(row = 0, column = 1,cellnums=1), Cell(row = 0, column = 2,cellnums=2)],
    [Cell(row = 1, column = 0,cellnums=3), Cell(row = 1, column = 1,cellnums=4), Cell(row = 1, column = 2,cellnums=5)],
    [Cell(row = 2, column = 0,cellnums=6), Cell(row = 2, column = 1,cellnums=7), Cell(row = 2, column = 2,cellnums=8)]]

    myText.grid(row=3, column = 1, padx = 0, sticky = 'n')  myText.grid(row=3, column = 1, padx = 0, sticky = 'n')
    
    window.mainloop()


main()
