from http.client import HTTPSConnection
import regionCode
import json
competitionApiAddress = 'https://infuser.odcloud.kr/api/stages/36148/api-docs?1644395106638'
competitionConnect = ''
sellAptInfoApiAddress = 'https://infuser.odcloud.kr/api/stages/37000/api-docs?1643022751478'
sellAptInfoConnect = ''
priceAptApiAddress = 'https://infuser.odcloud.kr/api/stages/27803/api-docs?1646718284600'
priceAptConnect = ''


def connectOpenAPIServer(conn, server):   
    conn = HTTPSConnection(server) 
    conn.set_debuglevel(1)


def userURIBuilder(uri, **user): 
    str = uri + "?"
    for key in user.keys(): 
        str += key + "=" + user[key] + "&"
    return str


def getcompetitionRatio():
    client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D"
    client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="
    global competitionConnect
    if competitionConnect == None :
        global competitionApiAddress
        connectOpenAPIServer(competitionConnect, competitionApiAddress)
    uri = userURIBuilder("/ApplyhomeInfoCmpetRtSvc/v1/getCancResplLttotPblancCmpet", page= 1, perPage= 1, returnType = "JSON")
    competitionConnect.request("GET", uri, None, #GET 요청
    {"ApiKeyAuth": client_id, "ApiKeyAuth2": client_secret})
    req = competitionConnect.getresponse()
    print (req.status)
    if int(req.status) == 200 : 
        print("response complete!")
    else:
        print("error - response!")



def getsellAptInfo(search):
    client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D" 
    client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="
    global sellAptInfoConnect
    if sellAptInfoConnect == None :
        global sellAptInfoApiAddress
        connectOpenAPIServer(sellAptInfoConnect, sellAptInfoApiAddress)
    uri = userURIBuilder("/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail", page= 1, perPage= 1, returnType = "JSON", HOUSE_MANAGE_NO = search)
    #얘는 지역이 서울, 부산... 으로 입력 가능
    sellAptInfoConnect.request("GET", uri, None, #GET 요청
    {"ApiKeyAuth": client_id, "ApiKeyAuth2": client_secret})
    req = sellAptInfoConnect.getresponse()
    print (req.status)
    if int(req.status) == 200 : 
        print("response complete!")
        jsonData = json.load(req)
        return jsonData
    else:
        print("error - response!")
        return None


def getpriceApt():
    client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D" 
    client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="
    global priceAptConnect
    if priceAptConnect == None :
        global priceAptApiAddress
        connectOpenAPIServer(priceAptConnect, priceAptApiAddress)
    uri = userURIBuilder("/HousePriceTrendSvc/v1/getHouseSaleDepositRate", page= 1, perPage= 1, returnType = "JSON" )
    #사용자가 지역 검색시 인자로 받아온 거 사용해야할듯 -> 인자는 서울 => regionCode[서울] 해서 넣어줘야됨
    priceAptConnect.request("GET", uri, None, #GET 요청
    {"ApiKeyAuth": client_id, "ApiKeyAuth2": client_secret})
    req = priceAptConnect.getresponse()
    print (req.status)
    if int(req.status) == 200 : 
        print("response complete!")
    else:
        print("error - response!")