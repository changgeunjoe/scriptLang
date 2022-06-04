from threading import local
from tkinter import *
from tkinter import font
currentcolor = 'red'
window = Tk()
winner = 4
gameturn = 1

process_button = None


board = [[]]

myText = Label(window, text = "o의 차례", anchor = 'center', width=0, height= 2, fg = 'red', bg = 'blue')


class Playertext():
    UPPER=6
    LOWER=7
    name=' '
    scores=0
    used=True


class Playertext(Label):
    def __init__(self, row = 0, column = 0, Cellnums=0):
        global window
        super().__init__(window, width=13, height=1)   

        super().grid(row = row, column = column)
        if(Cellnums==0):
            super().configure(text=  "플레이어 수")
        else:
            Playtext="플레이어"+str(Cellnums)+" 이름"
            super().configure(text=Playtext)
        #super().bind("<Button-1>", lambda e: self.changePhoto(Playertextnum = Playertextnum, obj = self))
class PlayerInput(Entry):
    def __init__(self, row = 0, column = 0, Cellnums=0):
        global window
        super().__init__(window, width=13, height=1)   
        super().grid(row = row, column = column)
        
def StartInitScreen():
    global window

    window.title('Tic-Tac-Toe')
    window.geometry("400x400+450+100")
    global board
    board = [
    [Playertext(row = 0, column = 0, Cellnums=0)],
    [Playertext(row = 1, column = 0,Cellnums=1)],
    [Playertext(row = 2, column = 0,Cellnums=2)],
    [Playertext(row = 3, column = 0, Cellnums=3)],
    [Playertext(row = 4, column = 0,Cellnums=4)],
    [Playertext(row = 5, column = 0, Cellnums=5)],
    [Playertext(row = 6, column = 0,Cellnums=6)],
    [Playertext(row = 7, column = 0, Cellnums=7)],
    [Playertext(row = 8, column = 0,Cellnums=8)],
    [Playertext(row = 9, column = 0, Cellnums=9)],
    [Playertext(row = 10, column = 0, Cellnums=10)],
   # [PlayerInput(row = 11, column = 0, Cellnums=11)]
    ]
    window.mainloop()


def main():
    StartInitScreen()

def numScore(inputN, playerDice):#uppersection 1~6
    res = 0
    for i in range(6):
        if inputN == playerDice[i]:
            res += 1
    return (inputN, res)

def threeOfKind(playerDice):
    for i in range(6):
        equalCnt = 0    
        for j in range(i + 1, 6 - i):
            if playerDice[i] == playerDice[j]:
                equalCnt += 1
        if equalCnt >= 3:
            return True
    return False

def fourOfKind(playerDice):
    for i in range(6):
        equalCnt = 0    
        for j in range(i + 1, 6 - i):
            if playerDice[i] == playerDice[j]:
                equalCnt += 1
        if equalCnt >= 4:
            return True
    return False

def fullHouse(playerDice):
    localDice = playerDice
    list(localDice).sort()
    for i in range(0, 5):
        if i != i+1 and i == 2:
            if localDice[3] == localDice[4]:
                return True
        elif i != i+1 and i == 1:
            if localDice[2] == localDice[3] and localDice[3] == localDice[4]:
                return True
    return False

def smallStraight(playerDice):
    localList = []
    for x in playerDice:
        if x not in localList:
            localList.append(x)
    if len(localList) < 4:
        return False
    localList.sort()
    if localList[0] +3 == localList[1] + 2== localList [2] + 1 == localList[3]:
        return True
    return False
    

def largeStraight(playerDice):
    localList = []
    for x in playerDice:        
            localList.append(x)    
    localList.sort()
    if localList[0] +3 == localList[1] + 2== localList [2] + 1 == localList[3] == localList[4] - 1:
        return True
    return False


def yahtzee(playerDice):
    for i in range(1, 6):
        if playerDice[0] != playerDice[i]:
            return False
    return True

main()
