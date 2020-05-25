import requests
import base64

http_proxy  = "http://127.0.0.1:8080"
https_proxy = "http://127.0.0.1:8080"
ftp_proxy   = "http://127.0.0.1:8080"

proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy
            }
URL="http://192.168.2.6:8000/api/v1/exams/"
for i in range(50,100):
    b64=base64.b64encode(bytes(str(i).encode('utf-8')))
    #print(b64.decode('utf-8'))
    r=requests.get(str(URL).encode('utf-8')+str(b64.decode('utf-8')).encode('utf-8')+str('/').encode('utf-8'),headers={"Authorization":"Bearer PglvilwuWE3Yva4gTHddfrJtssJ4Wf"}, proxies=proxyDict)
    print(i," ",r.status_code)


