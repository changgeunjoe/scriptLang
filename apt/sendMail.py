from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(fromAddr, toAddr, msg):
    import smtplib # 파이썬의 SMTP 모듈
# 메일 서버와 connect하고 통신 시작
    s = smtplib.SMTP("smtp.gmail.com", 587) # SMTP 서버와 연결
    s.starttls() # SMTP 연결을 TLS (Transport Layer Security) 모드로전환# 앱 password 이용
    s.login(fromAddr, 'wnqasjadunwjjuer')
    s.sendmail(fromAddr , [toAddr], msg.as_string())
    s.close()


def clickEmail(reciveLocal = '', aptName = None, region = None, startApply = None, EndApply = None, housePrizeDate = None, houseEngie = None,\
     contactStart = None, contactEnd = None):
    senderAddr = 'sh0win9907@gmail.com'
    recipientAddr = reciveLocal # HTML 전달을 위해 컨테이너 역할을 할 수 있는 "multipart/alternative" 타입사용
    main = '지역: ' + region + '\n아파트 이름: ' + aptName + '지원 시작일: ' + str(startApply) + ' ~ ' + str(EndApply) + '\n계약 시작일: ' \
        + str(contactStart) + ' ~ ' + str(contactEnd) + '\n건설회사: ' + str(houseEngie) + '\n당첨자 발표일: ' + str(housePrizeDate)
    msg = MIMEText(main)
    msg['From'] = senderAddr 
    msg['To'] = recipientAddr # 파일로부터 읽어서 MIME 문서를 생성.     
    msg['Subject'] = region + '에 있는 ' + aptName + '에 대한 청약 정보 입니다.'

#로고(사진) 첨부
    #htmlFD = open("logo.html", 'rb')
    #HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
    #htmlFD.close()
    #msg.attach(HtmlPart)

    # 메일 발송. 
    sendMail(senderAddr, recipientAddr, msg)