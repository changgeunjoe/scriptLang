from http.client import HTTPSConnection
conn = None
server = "openapi.naver.com“ # 네이버 OpenAPI 서버"

def connectOpenAPIServer(): 
    global conn, server
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
    global server, conn
    client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D" 
    client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="

def getsellAptInfo():
    global server, conn
    client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D" 
    client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="

def getpriceApt():
    global server, conn
    client_id = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D" 
    client_secret = "WTdhSu8Xoa2qFTe9YL4yicpM+fSZpEp9NFAWZJDT9Uv+FTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g=="