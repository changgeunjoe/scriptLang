from cgitb import text
from tkinter import *
from tkinter import font
import tkinter.messagebox
from player import *
from dice import *
from configuration import *

def emailWindow():
    g_Tk  = Tk()
    toplevel=Toplevel(g_Tk)
    
    fontNormal = font.Font(toplevel, size=15, weight='bold')
    toplevel.geometry("600x200+820+100")
    SearchButton = Button(g_Tk, font = fontNormal, width= 8,\
    text="확인", command=g_Tk.destroy())
class YahtzeeBoard:
    upperTotal = 6
    upperBonus = 7  
    lowerTotal = 15 
    total = 16 
    dice = []  
    diceButtons = []  
    fields = []  
    players = [] 
    numPlayers = 0
    player = 0  
    round = 0  
    roll = 0 

    def __init__(self):
        self.InitPlayers()

    def InitPlayers(self):
        self.pwindow = Tk()

        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')
        self.label = []
        self.entry = []
        self.label.append(Label(self.pwindow, text="플레이어 수", font=self.TempFont))
        self.label[0].grid(row=0, column=0)
        for i in range(1, 11):
            self.label.append( Label(self.pwindow, text='플레이어 '+str(i), font=self.TempFont ) )            
            self.label[i].grid(row=i, column=0)
        for i in range(11):
            self.entry.append(Entry(self.pwindow, font=self.TempFont))
            self.entry[i].grid(row=i, column=1)
        Button(self.pwindow, text="Yahtzee 플레이어 설정 완료", font=self.TempFont, command=self.playerNames).grid(row=11, column=0)
        self.pwindow.mainloop()

    def playerNames(self):
        self.numPlayers = int(self.entry[0].get())

        for i in range(1, self.numPlayers + 1):
            self.players.append(Player(str(self.entry[i].get())))
        self.pwindow.destroy()
        self.initInterface()  

    def initInterface(self): 
        self.window = Tk("YahtzeeGame")
        self.window.geometry("1600x800")
        self.TempFont = font.Font(size=16, weight='bold', family ='Consolas')
        for i in range(5):
            self.dice.append(Dice())
        self.rollDice = Button(self.window, text='RollDice', font = self.TempFont,
                      command = self.rollDiceListener)
                      
        self.rollDice.grid(row=0, column=0)
        for i in range(5): 
            self.diceButtons.append(Button(self.window, text='?',font = self.TempFont, width=8, command = lambda row=i: self.diceListener(row)))
            self.diceButtons[i].grid(row=i + 1, column=0)



        for i in range(self.total + 2):
            Label(self.window, text=Configuration.configs[i], font=self.TempFont).grid(row=i, column=1)
            for j in range(self.numPlayers):  
                if (i == 0):  
                    Label(self.window, text=self.players[j].toString(), font=self.TempFont).grid(row=i, column=2 + j)
                else:
                    if (j == 0):  
                        self.fields.append(list())
                    self.fields[i - 1].append(Button(self.window, text="", font=self.TempFont, width=8, command=lambda row=i - 1: self.categoryListener(row)))
                    self.fields[i - 1][j].grid(row=i, column=2 + j)
                    if (j != self.player or (i - 1) == self.upperTotal or (i - 1) == self.upperBonus
                        or (i - 1) == self.lowerTotal or (i - 1) == self.total):
                        self.fields[i - 1][j]['state'] = 'disabled'
                        self.fields[i - 1][j]['bg'] = 'light gray'
        self.bottomLabel = Label(self.window, text=self.players[self.player].toString() +
                                               "차례: Roll Dice 버튼을 누르세요", width=35, font=self.TempFont)
        self.bottomLabel.grid(row=self.total + 2, column=0)
        self.window.mainloop()

    def rollDiceListener(self): 
        for i in range(5):
            self.winnertag=Label(self.window, text="                                   ", font=self.TempFont).grid(row=10,column=0)
            if (self.diceButtons[i]['state'] != 'disabled'):
                self.dice[i].rollDie()
                self.diceButtons[i].configure(text=str(self.dice[i].getRoll()))
            else:
                self.diceButtons[i]['state'] = 'normal'
                self.diceButtons[i]['bg'] = 'SystemButtonFace'
        if (self.roll == 0 or self.roll == 1):
            self.roll += 1
            self.rollDice.configure(text="Roll Again")
            self.bottomLabel.configure(text="보관할 주사위 선택 후 Roll Again")
        elif (self.roll == 2):
            self.bottomLabel.configure(text="카테고리를 선택하세요")
            self.rollDice['state'] = 'disabled'
            self.rollDice['bg'] = 'light gray'

    def diceListener(self, row):  
        if self.roll!=0 :
            if self.diceButtons[row]['state']!='disabled':
                self.diceButtons[row]['state'] = 'disabled'
                self.diceButtons[row]['bg'] = 'light gray'

    def categoryListener(self, row):  
        score = Configuration.score(row, self.dice)  


        index = row
        if (row > 7):
            index = row - 2
        self.players[self.player].setScore(score, index)
        self.players[self.player].setAtUsed(index)
        self.fields[row][self.player].configure(text=str(score))
        self.fields[row][self.player]['state'] = 'disabled'
        self.fields[row][self.player]['bg'] = 'light gray'
        if (self.players[self.player].allUpperUsed()):
            self.fields[self.upperTotal][self.player].configure(text=
                                                            str(self.players[self.player].getUpperScore()))
            if (self.players[self.player].getUpperScore() > 63):
                self.fields[self.upperBonus][self.player].configure(text="35")  
            else:
                self.fields[self.upperBonus][self.player].configure(text="0")  

        if (self.players[self.player].allLowerUsed()):
            self.fields[self.lowerTotal][self.player].configure(text=str(self.players[self.player].getLowerScore()))
        if (self.players[self.player].allUpperUsed() and self.players[self.player].allLowerUsed()):
            self.fields[self.total][self.player].configure(text=str(self.players[self.player].getTotalScore()))
        self.player = (self.player + 1) % self.numPlayers

        for i in range(self.total + 1):
            for j in range(self.numPlayers):
                self.fields[i][j]['state'] = 'disabled'
                self.fields[i][j]['bg'] = 'light gray'

                if (j != self.player or (i) == self.upperTotal or (i) == self.upperBonus
                        or (i) == self.lowerTotal or (i)  == self.total):
                        self.fields[i][j]['state'] = 'disabled'
                        self.fields[i][j]['bg'] = 'light gray'
                elif  self.fields[i][self.player]['text']:
                    self.fields[i][self.player]['state'] = 'disabled'
                    self.fields[i][self.player]['bg'] = 'light gray'
                else:
                    self.fields[i][self.player]['state'] = 'normal'
                    self.fields[i][self.player]['bg'] = 'SystemButtonFace'
        if(self.player==0):
            self.round+=1
        if(self.round==13):
            d={}
            for x in self.players:
                d[x.toString()]=x.getTotalScore()
            val=max(d.values())
            resurtList=list(key for key,value in d.items() if value ==val)
            if len(resurtList)==1:
               a="승자는: "+resurtList[0]+" 입니다."
               self.winnertag=Label(self.window, text=a, font=self.TempFont).grid(row=10,column=0)


             
            else:
                resultstr=""
                for x in resurtList:
                    resultstr+=resultstr+x+","
                resultstr+="가 비겼습니다."
                self.winnertag = Label(self.window, text=resultstr, font=self.TempFont).grid(row=10,column=0)
            self.round=0
            self.player=0


            for i in range(5):
                self.diceButtons[i].configure(text='?')
                self.diceButtons[i]['state']='normal'
                self.diceButtons[i]['bg']='SystemButtonFace'

            for i in range(self.total + 1):
                for j in range(self.numPlayers):
                    self.fields[i][j].configure(text='')
                    if j==self.player:
                        self.fields[i][j]['state']='normal'
                        self.fields[i][j]['bg']='SystemButtonFace'
                    if i==6 or i==7 or i==15 or i==16:
                        self.fields[i][j]['state']='disabled'
                        self.fields[i][j]['bg']='light gray'
            for player in self.players:
                player.scores=[0 for i in range(15)]
                player.used=[False for i in range(15)]
        
        self.rollDice.configure(text="Roll Dice")
        self.rollDice['state']='normal'
        self.rollDice['bg']='SystemButtonFace'

     

        # self.roll=0
        # self.dice=[]
        # for i in range(5):  
        #     self.dice.append(Dice())
        # self.rollDice .configure(text='RollDice')
        # self.rollDice['state'] = 'normal'
        # self.rollDice['bg'] = 'SystemButtonFace'
        # for i in range(5):  
        #     self.diceButtons[i].configure(text="?")
        #     self.diceButtons[i]['state'] = 'normal'
        #     self.diceButtons[i]['bg'] = 'SystemButtonFace'
        # self.bottomLabel.configure(text=self.players[self.player].toString() +
        #                            "차례: Roll Dice 버튼을 누르세요")

        self.roll=0
        for i in range(5):
            self.diceButtons[i].configure(text='?')
            self.diceButtons[i]['state']='normal'
            self.diceButtons[i]['bg']='SystemButtonFace'
        
        for dice in self.dice:
            dice.roll=0
        
        self.bottomLabel.configure(text=self.players[self.player].toString()+"차례: Roll Dice 버튼을 누르세요")
        print(self.round)
YahtzeeBoard()
