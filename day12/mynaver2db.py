# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
from day12.dao_blog import Daoblog

blog = Daoblog()

client_id = "NoYgp1QJTsn1Eb8M9Zok"
client_secret = "P1xLyOgBlE"
encText = urllib.parse.quote("대전 오류동 맛집")
#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
response_body = response.read()
text = response_body.decode('utf-8')

    
soup = BeautifulSoup(text, "html.parser")

items = soup.select("item")
for i in items:
    title = i.select_one("title").text
    link = i.select_one("link").text
    description = i.select_one("description").text
    bloggername = i.select_one("bloggername").text
    bloggerlink = i.select_one("bloggerlink").text
    postdate = i.select_one("postdate").text
    
    print(title,link,description,bloggername,bloggerlink,postdate)
    cnt = blog.myinsert(title,link,description,bloggername,bloggerlink,postdate)
    
    print("cnt",cnt)
    
    
    
    