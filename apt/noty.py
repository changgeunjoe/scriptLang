import imp
import sys
import telepot
from pprint import pprint # 데이터를 읽기 쉽게 출력
from urllib.request import urlopen
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString
from subscriptionInfoAPI import *
key = 'WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D'
TOKEN = '5500444950:AAE7R8eqIK1OO1KvUw7VkG9XuqUzq8eupxQ'
MAX_MSG_LENGTH = 300
baseurl = '/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail'
bot = telepot.Bot(TOKEN)


def getData(houseNum = None, notificationNum = None,region = None,recruitStart = None,recruitEnd = None): 
    serviceKey = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="    
    uri = userURIBuilder(baseurl, serviceKey = key, page= '1', perPage= '100')    
    if region != None:
        uri += urllib.parse.quote('cond[SUBSCRPT_AREA_CODE_NM::EQ]')
        uri += '='
        uri += urllib.parse.quote(region)
    if notificationNum != None:
        uri += urllib.parse.quote('cond[HOUSE_MANAGE_NO::EQ]')
        uri += '='
        uri += urllib.parse.quote(notificationNum)
    if houseNum != None:
        uri += urllib.parse.quote('cond[PBLANC_NO::EQ]')#공고
        uri += '='
        uri += urllib.parse.quote(houseNum)
    if recruitStart != None:
        uri += urllib.parse.quote('cond[RCRIT_PBLANC_DE::GTE]')
        uri += '='
        uri += urllib.parse.quote(recruitStart)
    if recruitEnd != None:
        uri += urllib.parse.quote('cond[RCRIT_PBLANC_DE::LTE]')
        uri += '='
        uri += urllib.parse.quote(recruitEnd)
        
    req =  requests.get("http://api.odcloud.kr/api" + uri)
    print (req)
    print(req.status_code)
    if req.status_code == 200:
        print("response complete!")
        jsonData = json.loads(req.text)
    
    res_list = []

    if jsonData['data'] != None:
        for item in jsonData['data']:
            houseName = item["HOUSE_NM"]
            notificationNum = item["HOUSE_MANAGE_NO"]#주택관리번호
            region = item["HSSPLY_ADRES"]
            applyStart = item["RCEPT_BGNDE"]#지원 시작일
            applyEnd = item["RCEPT_ENDDE"]
            housePrizeDate= item["PRZWNER_PRESNATN_DE"]#당첨자
            houseEngineerCompany = item["CNSTRCT_ENTRPS_NM"]#건설 회사
            contactStartDate = item["CNTRCT_CNCLS_BGNDE"]#계약 시작일
            contactEndDate = item["CNTRCT_CNCLS_ENDDE"]
            row = '청약 접수 기간: ' + str(applyStart) + ' ~ ' + str(applyEnd) + '\n계약 기간: ' + str(contactStartDate) + ' ~ ' + str(contactEndDate) + '\n공급지역: ' + \
                str(region) + '\n집 이름: ' + str(houseName) + '\n주택관리번호: ' + str(notificationNum) + '\n건설회사: ' + str(houseEngineerCompany) + \
                    '\n당첨자 발표일: ' + str(housePrizeDate)
            res_list.append(row)
    return res_list

    #sendMessage('5123909010', 'aaa')

def sendMessage(user, msg): 
    try:
        bot.sendMessage(user, msg) 
    except:
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)


#getData('11545', '202101')