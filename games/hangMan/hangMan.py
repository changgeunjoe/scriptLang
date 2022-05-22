from random import randrange as randI
from tkinter import *
import random
from unittest import result
words = []
secretWord = '****'
answerWord = ''

def initWords():#단어 리스트 파일 읽어 오는 부분
    global words
    hangmanFile = open('txt\hangman.txt', 'r')    
    while(True):
        word = hangmanFile.read()
        if not word : break        
        wordlist = word.split() 
        for w in wordlist:
            words.append(w)
    hangmanFile.close()

def getRandWord():#answerWord = getRandWord()
    global words
    randWN = randI(0, len(words))
    answerWord = words[randWN]
    words.pop(randWN)
    global secretWord
    secretWord = ''
    for i in range(0, len(answerWord)):
        secretWord += '*'
    return answerWord


def isContainWord(inputWord):#현재 입력한 문자를 답인 문자에 포함 되어 있는지 판단 -> 존재 True /  False -> 행맨 부위 자르기// 반환은 bool, str(입력 문자)
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
class HANGMANGUI:
    def string(self,word):
        result =' '
        for ch in word:
            result +=ch
        return result
    def DrawHangman(self):
        self.canvas.delete('hangman')
        self.canvas.create_arc(20,200,20+80,200+40,start=0,extent=180)
        self.canvas.create_line(20+40,200,20+40,20)
        self.canvas.create_line(20+40,20,20+140,20)
        if self.doneWithWrong:
            self.canvas.create_text(200,250,text='정답'+self.hiddenword,tags='hangman')
            self.canvas.create_text(200,265,text='계속하면 Enter',tags='hangman')
        if self.doneWithCorrect:
            self.canvas.create_text(200,250,text='맞았습니다'+self.hiddenword,tags='hangman')
            self.canvas.create_text(200,265,text='계속하면 Enter',tags='hangman')
        else:
            self.canvas.create_text(200,250,text='단어 추측'+self.toString(self.guessWord),tags='hangman')
            if self.NofMiss>0:
                self.canvas.create_text(200,260,text='단어 추측'+self.toString(self.missChars),tags='hangman')
        if self.NofMiss<1:
            return
        x1=20+140
        y1=20
        x2=x1
        y2=y1+20
        self.canvas.create_line(x1,y1,x2,y2,tags='hangman')
        if self.NofMiss < 2:
            return
        x3=x2
        y3=y2+20
        self.canvas.create_oval(x3-20,y3-20,x3+20,y3+20,tags='hangman')
        if self.NofMiss < 3:
            return
        self.canvas.create_line(x3-15,y3+15,x3-50,y3+70,tags='hangman')
        if self.NofMiss < 4:
                return
        self.canvas.create_line(x3+15,y3+15,x3+50,y3+70,tags='hangman')
        if self.NofMiss < 5:
            return
        x4=x3
        y4=y3+100
        self.canvas.create_line(x3,y3+20,x4,y4,tags='hangman')
        if self.NofMiss < 6:
            return
        self.canvas.create_line(x4,y4,x4-50,y4+100,tags='hangman')
        if self.NofMiss < 7:
            return
        self.canvas.create_line(x4,y4,x4+50,y4+100,tags='hangman')
    def setWord(self):
        index=random.randint()

initWords()
answerWord = getRandWord()
while(True):
    if changeWord():
        answerWord = getRandWord()
    print(answerWord)
    print(secretWord)
    print(isContainWord(input()))


        