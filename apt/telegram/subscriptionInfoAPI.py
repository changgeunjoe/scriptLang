from codecs import utf_16_be_encode
from encodings import utf_8
from http.client import HTTPSConnection
import json
import requests
import urllib

sellAptInfoApiAddress = 'http://api.odcloud.kr/api'
sellAptInfoConnect = None

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
    Autho = "WTdhSu8Xoa2qFTe9YL4yicpM%2BfSZpEp9NFAWZJDT9Uv%2BFTLLJ1CkIjIl3Kmbk7jUxg2Y8fep6Tz08BdBHpXw4g%3D%3D" 
    uri = userURIBuilder("/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail", serviceKey = Autho, page= '1', perPage= '100')    
    uri += urllib.parse.quote('cond[SUBSCRPT_AREA_CODE_NM::EQ]')
    uri += '='
    uri += urllib.parse.quote(search)
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
