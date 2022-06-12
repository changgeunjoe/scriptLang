import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime
import noty


def replyAptData(user, houseNum = None, notificationNum = None,region = None,recruitStart = None,recruitEnd = None): 
    print(user, houseNum, region) 
    res_list = noty.getData( houseNum = houseNum, notificationNum = notificationNum,region = region,recruitStart = recruitStart,recruitEnd = recruitEnd ). 
    msg = '' 
    for r in res_list: 
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noty.MAX_MSG_LENGTH: 
            noty.sendMessage( user, msg ) 
            msg = r+'\n' 
        else: msg += r+'\n'
    if msg: 
        noty.sendMessage( user, msg ) 
    else: 
        noty.sendMessage( user, '%s 기간에 해당하는 데이터가 없습니다.'%recruitStart)


def save( user, loc_param ): 
    conn = sqlite3.connect('users.db') 
    cursor = conn.cursor() 
    cursor.execute('CREATE TABLE IF NOT EXISTS \ users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try: 
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param)) 
    except sqlite3.IntegrityError: 
        noty.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' ) 
        return
    else: 
        noty.sendMessage( user, '저장되었습니다.' )
        conn.commit()


def check( user ): 
    conn = sqlite3.connect('users.db') 
    cursor = conn.cursor() 
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, locationTEXT, PRIMARY KEY(user, location) )') 
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall(): 
        row = 'id:' + str(data[0]) + ', location:' + data[1] 
        noty.sendMessage( user, row )


def handle(msg): 
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text': 
        noty.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.') 
        return
    text = msg['text']
    splitText = text.split(' ')
    houseNum = None
    region = None
    notiNum = None
    applyS= None 
    applyE = None
    if '주택관리번호' not in splitText and '지역' not in splitText and '공고번호' not in splitText\
        and '모집공고시작일' not in splitText and '모집공고종료일' not in splitText and '확인' not in splitText\
            and '저장'not in splitText:
        noty.sendMessage(chat_id, '''도움말\n 예시\n주택관리번호 111, 지역 서울, 공고번호 1231, 모집공고시작일 yyyymmdd, 모집공고종료일 yyyymmdd"]''')
        return
    if '주택관리번호' in splitText:
        houseNum = splitText[splitText.index('주택관리번호') + 1]
    if '지역' in splitText:
        region = splitText[splitText.index('지역') + 1]
    if '공고번호' in splitText:
        notiNum = splitText[splitText.index('공고번호') + 1]
    if '모집공고시작일' in splitText:
        applyS = splitText[splitText.index('모집공고시작일') + 1]
    if '모집공고종료일' in splitText:
        applyE = splitText[splitText.index('모집공고종료일') + 1]
    if '확인' in splitText:
        check( chat_id )
    if '저장' in splitText:
        save( chat_id, splitText[splitText.index('저장') + 1] )
    replyAptData(chat_id, houseNum=houseNum, notificationNum=notiNum, region=region, recruitStart=applyS, recruitEnd=applyE)

    
    if houseNum == None and region == None and notiNum == None and applyS == None and applyE == None: 
        noty.sendMessage(chat_id, '''모르는 명령어입니다.\n 예시\n주택관리번호 nnnn, 지역 서울, 공고번호 nnnn, 모집공고시작일 yyyymmdd, 모집공고종료일 yyyymmdd"]''')
    

today = date.today() 
current_month = today.strftime('%Y%m')
print( '[',today,']received token :', noty.TOKEN )
from noty import bot
pprint( bot.getMe() )
bot.message_loop(handle)
print('Listening...') 
while 1: 
    time.sleep(10)