from msilib.schema import ListBox
from tkinter import *
from turtle import width

window = Tk()

class regionButton(Button):
    def __init__(self):
        super().__init(text = "지역 선택", anchor = 'center', width = 40, height = 20)
        
        


class aptApp(Canvas):
    logo = Label()
    selectRegion = regionButton()
    searchButton = Entry()
    myList = Listbox()
    atpInformation = Button()
    aptPhoto = Canvas()
    #email
    #graph =  #수업시간에 할거
    #aptMap = 

    def __init__(self):
        self.color = "white"                
        global window
        super().__init__(window, width=400, height=300, bg="white")
        super().grid(row=0, column=0)
        self.draw()
        

