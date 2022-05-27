from http.client import HTTPSConnection

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


def getBookDataFromISBN(isbn): 
    global server, conn
    client_id = "XXXXXXXXXXXXX" 
    client_secret = "YYYYYYYY"
    if conn == None : 
        connectOpenAPIServer() # OpenAPI 접속
#네어버에서 ISBN에 의한 도서정보 가져올 URL 생성


    uri = userURIBuilder("/v1/search/book_adv.xml", display="1", start="1", d_isbn=isbn)
    conn.request("GET", uri, None, #GET 요청
    {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    req = conn.getresponse()
    print (req.status)
    if int(req.status) == 200 : 
        print("Book data downloading complete!")
        return extractBookData(req.read()) #요청이 성공이면 book 정보추출
    else: 
        print ("OpenAPI request has been failed!! please retry")
        return None


#competitionRatio #경쟁률
#sellAptInfo # 분양 정보
#priceApt #아파트 가격 동향

def getcompetitionRatio():
    client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D"
    client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="
    global competitionConnect
    if competitionConnect == None :
        global competitionApiAddress
        connectOpenAPIServer(competitionConnect, competitionApiAddress)
    uri = userURIBuilder("/ApplyhomeInfoCmpetRtSvc/v1/getCancResplLttotPblancCmpet", page= 1, perPage= 1, returnType = "JSON")
    conn.request("GET", uri, None, #GET 요청
    {"ApiKeyAuth": client_id, "ApiKeyAuth2": client_secret})
    req = conn.getresponse()
    print (req.status)
    if int(req.status) == 200 : 
        print("response complete!")
    else:
        print("error - response!")



def getsellAptInfo():
    client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D" 
    client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="
    global sellAptInfoConnect
    if conn == None :
        global sellAptInfoApiAddress
        connectOpenAPIServer(sellAptInfoConnect, sellAptInfoApiAddress)

def getpriceApt():
    client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D" 
    client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="
    global priceAptConnect
    if conn == None :
        global priceAptApiAddress
        connectOpenAPIServer(priceAptConnect, priceAptApiAddress)