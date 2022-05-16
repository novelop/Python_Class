# from urllib.request import urlopen
# html = urlopen("http://127.0.0.1:5000/list")  
# bsObject = BeautifulSoup(html, "html.parser") 
# print(bsObject) # 웹 문서 전체가 출력

import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5000/list"

html = requests.get(url)


soup = BeautifulSoup(html.text, "html.parser")

print(soup)