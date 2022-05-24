from http.client import HTTPSConnection
conn = None
server = "openapi.naver.com“ # 네이버 OpenAPI 서버"

def connectOpenAPIServer(): global conn, server conn = HTTPSConnection(server) conn.set_debuglevel(1)
