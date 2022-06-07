import sys
import telepot
from pprint import pprint # 데이터를 읽기 쉽게 출력
from urllib.request import urlopen
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString
key = 'WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D'
TOKEN = '5500444950:AAE7R8eqIK1OO1KvUw7VkG9XuqUzq8eupxQ'
MAX_MSG_LENGTH = 300
baseurl = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?type=xml&serviceKey='+key
bot = telepot.Bot(TOKEN)


def getData(loc_param, date_param): 
    res_list = [] 
    url = baseurl+'&LAWD_CD='+loc_param+'&DEAL_YMD='+date_param
    res_body = urlopen(url).read() 
    strXml = res_body.decode('utf-8')
    tree = ElementTree.fromstring(strXml)

    items = tree.iter("item") # return list type
    for item in items: 
        amount = item.find("거래금액").text.strip()
        build = item.find("건축년도").text
        y = item.find("년").text
        dong = item.find("법정동").text 
        apt = item.find("아파트").text 
        m = item.find("월").text
        d = item.find("일").text 
        n = item.find("전용면적").text 
        row = y + '/' + m + '/' + d + ', ' + dong + ' ' + apt + '(' \
            + build+') ' + n + 'm², ' + amount + '만원'
        res_list.append(row)
    return res_list

    #sendMessage('5123909010', 'aaa')

def sendMessage(user, msg): 
    try:
        bot.sendMessage(user, msg) 
    except:
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)


#getData('11545', '202101')