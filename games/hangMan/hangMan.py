words = []


def initWords():
    global words
    hangmanFile = open('txt\hangman.txt', 'r')    
    while(True):
        word = hangmanFile.read()
        if not word : break        
        wordlist = word.split()
        for w in wordlist:
            words.append(w)
    hangmanFile.close()


initWords()
for i in words:
    print(i)

