from random import randrange as randI
from tkinter import *

words = []
secretWord = '****'
answerWord = ''
wrongWords = []
wrongCount=6
window = Tk()


def initWords():
    hangmanFile = open('txt\hangman.txt', 'r')    
    while(True):
        word = hangmanFile.read()
        if not word : break        
        wordlist = word.split() 
        for w in wordlist:
            words.append(w)
    hangmanFile.close()

def getRandWord():
    global words
    global answerWord
    randWN = randI(0, len(words))
    answerWord = words[randWN]
    words.pop(randWN)
    global secretWord
    secretWord = ''
    for i in range(0, len(answerWord)):
        secretWord += '*'
    return answerWord


def isContainWord(inputWord):
    isFind = False
    global answerWord
    global secretWord
    for i in range(0, len(answerWord)):
        if answerWord[i] == inputWord:
            secretWord = secretWord[:i] + answerWord[i] + secretWord[i + 1:]
            isFind = True
    return (isFind, inputWord)

def changeWord():
    global secretWord    
    for x in secretWord:
        if x == '*':
            return False
    return True

def keyEvent(event):
    hang.delete('keyevent')
    hang.delete('secretword')
    hang.delete('hangman')
    global wrongCount
    if wrongCount != -1:
        hang.create_text(280,210,text = (repr(event.char))[1], tags='keyevent')
        global wrongWords
        res = isContainWord(repr(event.char)[1])
        if not res[0]:
            if wrongWords.count(res[1]) != 1:
                wrongCount-=1
                wrongWords.append(res[1])
                hang.delete('wrongevent')
                hang.create_text(280,240,text = wrongWords, tags='wrongevent')
        hang.draw()

def inputReturn(event):     
    global wrongCount
    global wrongWords
    global hang
    if (not changeWord() and wrongCount == -1) or changeWord():
        wrongCount = 6
        getRandWord()
        wrongWords.clear()
        hang.draw()
        hang.delete('keyevent')
        hang.delete('secretword')
        hang.delete('hangman')
        hang.delete('wrongevent')
        hang.delete('regame')
        hang.create_text(280,190,text=secretWord,tags='secretword')
        

def inputBackSpace(event, obj):
    print('backSpace')


class Hangman(Canvas):    

    def __init__(self):
        self.color = "white"        
        initWords()
        getRandWord()
        global window
        super().__init__(window, width=400, height=300, bg="white")
        super().grid(row=0, column=0)
        self.draw()
        window.bind("<Key>", keyEvent)
        window.bind("<Return>", inputReturn)

   
    def guess(self,letter):
        pass
    def draw(self):
        global secretWord
        global wrongWords
        self.delete('hangman')
        self.create_text(200,190,text='단어 추측:')
        self.create_text(200,210,text='추측 단어 입력:')
        self.create_text(280,190,text=secretWord,tags='secretword')
        self.create_arc(20,200,20+80,200+40,start=0,extent=180)
        self.create_line(20+40,200,20+40,20)
        self.create_line(20+40,20,20+140,20)
        x1=20+140
        y1=20
        x2=x1
        y2=y1+20
        self.create_line(x1,y1,x2,y2,tags='hangman')
        x3=x2
        y3=y2+20
        if wrongCount < 6:
            self.create_oval(x3-20,y3-20,x3+20,y3+20,tags='hangman')
        if wrongCount < 5:    
            self.create_line(x3-15,y3+15,x3-50,y3+70,tags='hangman')
        if wrongCount < 4:    
            self.create_line(x3+15,y3+15,x3+50,y3+70,tags='hangman')
        x4=x3
        y4=y3+100
        if wrongCount < 3:
            self.create_line(x3,y3+20,x4,y4,tags='hangman')
        if wrongCount < 2:
            self.create_line(x4,y4,x4-50,y4+100,tags='hangman')
        if wrongCount < 1:    
            self.create_line(x4,y4,x4+50,y4+100,tags='hangman')

        if changeWord():
            global answerWord
            self.create_text(200,260,text='정답입니다. 다시 시작하려면 enter를 입력하세요', tags = 'regame')


        if not changeWord() and wrongCount == -1:
            global answerWord
            self.create_text(200,260,text='정답은' + answerWord + '다시 시작하려면 enter를 입력하세요', tags = 'regame')

    
hang = 0

def main():
    global window

    window.title('Hang-man')
    window.geometry("400x400+450+100")
    global hang
    hang = Hangman()    
    window.mainloop()


main()
