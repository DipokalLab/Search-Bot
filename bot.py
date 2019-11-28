# Search Bot made by DeVent
# Developer: Dipokal HHJ
# 이 검색 봇은 추후 서비스 될 DeVent Ser 에 적용될 예정입니다
# 2019-11-28 최초 개발

import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def header(ur):
    res = requests.get(ur, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.find('title')
    print(cleanhtml(str(title)))


def serc(ur):
    res = requests.get(ur, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    for link in soup.findAll("a"):
        if 'href' in link.attrs:
            if 'http://' in link.attrs['href']:
                print (link.attrs['href'])
                header(link.attrs['href'])
            elif 'https://' in link.attrs['href']:
                print (link.attrs['href'])
                header(link.attrs['href'])
            else:
                print (ur+link.attrs['href'])
                header(ur+link.attrs['href'])



serc('https://getbootstrap.com/')
