# web2.py
# 웹크롤링에 관련된 선언
from bs4 import BeautifulSoup

# 웹서버에 요청
import requests

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)
# 검색에 용이한 객체 생성
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# 파일에 저장: 기존 파일에 첨부 가능
f = open("daangn.txt", "a+", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    regionElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.replace("\n", "").strip()
    price = priceElem.text.replace("\n", "").strip()
    region = regionElem.text.replace("\n", "").strip()
    # 내부에 문자열만 출력: f-string
    print(f"{title}, {price}, {region}")
    f.write(f"{title}, {price}, {region}\n")

f.close()

