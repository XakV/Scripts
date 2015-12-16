#!/usr/bin/python3


import requests, json, time
from bs4 import BeautifulSoup as bs

rwurl = 'https://oak-oh.client.renweb.com/pw/index.cfm'

def genhwurl():
    """

    :rtype: str
    """
    hwdate = str(time.strftime("%m/%d/%Y"))
    dathwurl = 'https://oak-oh.client.renweb.com/pw/student/homework-print.cfm?studentid=all&day=' + hwdate
    return dathwurl

hwurl = genhwurl()

district = 'OAK-OH'
data = {'username': '##editthis##', 'password': '##editthis##'}

rwsesh = requests.session()
rwlogin = rwsesh.get('https://oak-oh.client.renweb.com/pw/index.cfm')
rwauth = rwsesh.post(rwurl, data=data)
rwhw = rwsesh.get(hwurl)
print(rwhw.text)
