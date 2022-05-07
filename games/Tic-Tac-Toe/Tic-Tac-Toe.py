from tkinter import *

image_o_path = "o.gif"
image_x_path = "x.gif"
image_empty_path = "empty.gif"


class Cell(Label): # 하나의 그림 1 부분
    cellStatus = 0
    def __init__(self):
        global window
        super().__init__(window, width=200, height=100)
        global photo_Empty        
        self.configure(image = photo_Empty)
       

window = Tk()
photo_Empty = PhotoImage(file = image_empty_path)
photo_O = PhotoImage(file = image_o_path)
photo_X = PhotoImage(file = image_x_path)

def main():
    global window
    
    window.title('Tic-Tac-Toe')
    window.geometry("600x600+450+100")
    window.resizable(False, False)

    c1 = Cell()
    c1.pack(side = 'top', anchor= 'w')


    window.mainloop()


main()