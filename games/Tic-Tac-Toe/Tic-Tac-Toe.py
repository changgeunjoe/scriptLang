from tkinter import *

image_o_path = "o.gif"
image_x_path = "x.gif"
image_empty_path = "empty.gif"


window = Tk()
photo_Empty = PhotoImage(file = image_empty_path)
photo_O = PhotoImage(file = image_o_path)
photo_X = PhotoImage(file = image_x_path)

gameTurn = 0

class Cell(Label):
    cellStatus = 0
    def __init__(self, row = 0, column = 0):
        global window

        global photo_Empty

        super().__init__(window, width=34, height=34)
        super().grid(row = row, column = column)
        super().configure(image = photo_Empty)
        super().bind("<Button-1>", lambda e: self.changePhoto())
        
    
    def changePhoto(event):
        global gameTurn
        if gameTurn == 0:
            super().configure(image = photo_O)
            gameTurn = 1
        else:
            super().configure(image = photo_X)
            gameTurn = 0
    
    def setCellStatus(s):
        cellStatus = s

    


def main():
    global window
   
    window.title('Tic-Tac-Toe')
    window.geometry("115x125+450+100")
    window.resizable(False, False)

    board = [
        [Cell(row = 0, column = 0), Cell(row = 0, column = 1), Cell(row = 0, column = 2)],
     [Cell(row = 1, column = 0), Cell(row = 1, column = 1), Cell(row = 1, column = 2)],
     [Cell(row = 2, column = 0), Cell(row = 2, column = 1), Cell(row = 2, column = 2)]]


    window.mainloop()


main()