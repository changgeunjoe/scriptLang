from random import randrange as randI
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

initWords()
answerWord = getRandWord()
while(True):
    if changeWord():
        answerWord = getRandWord()
    print(answerWord)
    print(secretWord)
    print(isContainWord(input()))