from dice import *

class Configuration:

    configs = [
        "Categoty", "Ones", "Twos", "threes", "Fours", "Fives", "Sixes",
        "Upper Scores", "Upper Bonus(35)",
        "3 of a kind", "4 of a kind", "Full House(25)",
        "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance",
        "Lower Scores", "Total"
    ]

    @staticmethod
    def getConfigs():       # 정적 메소드 (객체 없이 사용 가능)
        return Configuration.configs

    # row에 따라 주사위 점수를 계산하여 반환. 
    # 예를 들어, row가 0이면 "Ones"가, 2이면 "Threes"가 채점되어야 함을 의미. 
    # row가 득점위치가 아닌 곳(즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우 -1을 반환.
    @staticmethod
    def score(row, d): # 정적 메소드: 객체생성 없이 사용 가능
    #row에 따라 주사위 점수를 계산 반환. 예를 들어, row가 0이면 "Ones"가 채점되어야 함을
    # 의미합니다. row가 2이면, "Threes"가 득점되어야 함을 의미합니다. row가 득점 (scored)하지
    # 않아야 하는 버튼 (즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우
    # -1을 반환합니다.
        if (row>=0 and row<=6):
            return Configuration.numScore(row+1, d)
        elif row==8:
            return Configuration.scoreThreeOfAKind(d)
        elif row==9:
            return Configuration.scoreFourOfAKind(d)
        elif row==10:
            return Configuration.scoreFullHouse(d)
        elif row==11:
            return Configuration.scoreSmallStraight(d)
        elif row==12:
            return Configuration.scoreLargeStraight(d)
        elif row==13:
            return Configuration.scoreYahtzee(d)
        elif row==14:
            return Configuration.sumDice(d)
        else:
            return -1

    def scoreYahtzee(d):
        lst = []
        for i in range(5):
            lst.append(d[i].getRoll())
        if len(set(lst))==1:
            return 50
        else:
            return 0

    def sumDice(d):
        s=0
        for i in range(5):
           s+=d[i].getRoll()
        return s

    def numScore(inputN, playerDice):#uppersection 1~6
        res = 0
        for i in range(5):
            if inputN == playerDice[i]:
                res += inputN
        return res

    def scoreThreeOfAKind(d):
        s=0
        val1=0
        val2=0
        val3=0
        val4=0
        val5=0
        val6=0
        for i in range(5):
            if d[i].getRoll()==1:
                val1+=1
            elif d[i].getRoll()==2:
                val2+=1
            elif d[i].getRoll()==3:
                val3+=1
            elif d[i].getRoll()==4:
                val4+=1
            elif d[i].getRoll()==5:
                val5+=1
            elif d[i].getRoll()==6:
                val6+=1
        if val1>2 or val2>2 or val3>2 or val4>2 or val5>2 or val6>2:
            for i in range(5):
                s+=d[i].getRoll()

        return s


    def scoreFourOfAKind(d):
        s = 0
        val1 = 0
        val2 = 0
        val3 = 0
        val4 = 0
        val5 = 0
        val6 = 0
        for i in range(5):
            if d[i].getRoll() == 1:
                val1 += 1
            elif d[i].getRoll() == 2:
                val2 += 1
            elif d[i].getRoll() == 3:
                val3 += 1
            elif d[i].getRoll() == 4:
                val4 += 1
            elif d[i].getRoll() == 5:
                val5 += 1
            elif d[i].getRoll() == 6:
                val6 += 1
        if val1 > 3 or val2 > 3 or val3 > 3 or val4 > 3 or val5 > 3 or val6 > 3:
            for i in range(5):
                s += d[i].getRoll()

        return s


    def scoreFullHouse(d):
        lst = []
        for i in range(5):
            lst.append(d[i].getRoll())
        if len(set(lst))==2:
            return 25
        else:
            return 0

    def scoreSmallStraight(d):
        lst = []
        for i in range(5):
            lst.append(d[i].getRoll())
        if len(set(lst))>3:
            lst.sort()
            s=0
            count=0
            for i in range(3):
                if abs(lst[i]-lst[i+1])>1:
                    count+=1
            for i in range(1,4):
                if abs(lst[i] - lst[i + 1]) >1:
                    count += 1

            if count>=2:
                return 0
            else:
                return 30
        else:
            return 0
    # 1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
    # 1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5

    def scoreLargeStraight(d):
        lst=[]
        for i in range(5):
            lst.append(d[i].getRoll())
        lst.sort()
        count1=0
        count2=0
        for i in range(5):
            if lst[i]==i+1:
                count1+=1
        for i in range(5):
            if lst[i]==i+2:
                count2+=1
        if count1==5 or count2 == 5:
            return 40
        else:
            return 0
    # 1 2 3 4 5 혹은 2 3 4 5 6 검사
