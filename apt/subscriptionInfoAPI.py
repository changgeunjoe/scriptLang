from codecs import utf_16_be_encode
from encodings import utf_8
from http.client import HTTPSConnection
import regionCode
import json
import urllib
import requests


competitionApiAddress = 'https://infuser.odcloud.kr/api/stages/36148/api-docs?1644395106638'
competitionConnect = None
sellAptInfoApiAddress = 'http://api.odcloud.kr/api'
sellAptInfoConnect = None
priceAptApiAddress = 'https://infuser.odcloud.kr/api/stages/27803/api-docs?1646718284600'
priceAptConnect = None


def connectOpenAPIServer(server):   
    conn = HTTPSConnection(server) 
    conn.set_debuglevel(1)
    return conn


def userURIBuilder(uri, **user): 
    str = uri + "?"
    for key in user.keys(): 
        str += key + "=" + user[key] + "&"
    return str

def getsellAptInfo(search):
    serviceKey = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="
    Autho = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D" 
    uri = userURIBuilder("/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail", serviceKey = Autho, page= '1', perPage= '100')    
    #얘는 지역이 서울, 부산... 으로 입력 가능
    req =  requests.get(sellAptInfoApiAddress + uri)
    print (req)
    print(req.status_code)
    if req.status_code == 200:
        print("response complete!")
        jsonData = json.loads(req.text)
        return jsonData
    else:
        print("error - response!")
        return None


# def getcompetitionRatio():
#     client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D"
#     client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="
#     global competitionConnect
#     if competitionConnect == None :
#         global competitionApiAddress
#         connectOpenAPIServer(competitionConnect, competitionApiAddress)
#     uri = userURIBuilder(sellAptInfoApiAddress + "/ApplyhomeInfoCmpetRtSvc/v1/getCancResplLttotPblancCmpet", page= 1, perPage= 1, returnType = "JSON")
#     competitionConnect.request("GET", uri, None, #GET 요청
#     {"ApiKeyAuth": client_id, "ApiKeyAuth2": client_secret})
#     req = competitionConnect.getresponse()
#     print (req.status)
#     if int(req.status) == 200 :
#         print("response complete!")
#     else:
#         print("error - response!")





# def getpriceApt():
#     client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D" 
#     client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="
#     global priceAptConnect
#     if priceAptConnect == None :
#         global priceAptApiAddress
#         connectOpenAPIServer(priceAptConnect, priceAptApiAddress)
#     uri = userURIBuilder("/HousePriceTrendSvc/v1/getHouseSaleDepositRate", page= 1, perPage= 1, returnType = "JSON" )
#     #사용자가 지역 검색시 인자로 받아온 거 사용해야할듯 -> 인자는 서울 => regionCode[서울] 해서 넣어줘야됨
#     priceAptConnect.request("GET", uri, None, #GET 요청
#     {"ApiKeyAuth": client_id, "ApiKeyAuth2": client_secret})
#     req = priceAptConnect.getresponse()
#     print (req.status)
#     if int(req.status) == 200 : 
#         print("response complete!")
#     else:
#         print("error - response!")