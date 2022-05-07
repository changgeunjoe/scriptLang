from tkinter import *

image_o_path = "o.gif"
image_x_path = "x.gif"
image_empty_path = "empty.gif"


class Cell(Label): # 하나의 그림 1 부분
    cellStatus = 0
    def __init__(self, window):
        photoInit = PhotoImage(file = "empty.gif")
        
        #PhotoImage(file = image_o_path)
        super().__init__(window, image = photoInit, width=23, height=13)
        super().pack()
  


def main():
    window = Tk()
    window.title('Tic-Tac-Toe')
    window.geometry("600x600+450+100")
    window.resizable(False, False)

    c1 = Cell(window)
    c1.configure(image = image_o_path) 
    c1.pack(side = 'top', anchor= 'w')


    window.mainloop()


main()