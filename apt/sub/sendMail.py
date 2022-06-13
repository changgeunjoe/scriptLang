from email.mime.text import MIMEText

def sendMail(fromAddr, toAddr, msg):
    import smtplib
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(fromAddr, 'wnqasjadunwjjuer')
    s.sendmail(fromAddr , [toAddr], msg.as_string())
    s.close()


def clickEmail(reciveLocal = '', aptName = None, region = None, startApply = None, EndApply = None, housePrizeDate = None, houseEngie = None,\
     contactStart = None, contactEnd = None):
    senderAddr = 'sh0win9907@gmail.com'
    recipientAddr = reciveLocal
    main = '지역: ' + region + '\n아파트 이름: ' + aptName + '지원 시작일: ' + str(startApply) + ' ~ ' + str(EndApply) + '\n계약 시작일: ' \
        + str(contactStart) + ' ~ ' + str(contactEnd) + '\n건설회사: ' + str(houseEngie) + '\n당첨자 발표일: ' + str(housePrizeDate)
    msg = MIMEText(main)
    msg['From'] = senderAddr 
    msg['To'] = recipientAddr
    msg['Subject'] = region + '에 있는 ' + aptName + '에 대한 청약 정보 입니다.'
 
    sendMail(senderAddr, recipientAddr, msg)
    