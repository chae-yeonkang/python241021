# chatGPT로크롤링하는코드.py

import requests
from bs4 import BeautifulSoup

# 뉴스 페이지 URL
url = 'https://example.com/news'  # 실제 크롤링할 웹사이트 URL로 변경

# 페이지 가져오기
response = requests.get(url)
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 기사 제목 크롤링 (예시: <h2> 태그 안에 제목이 있는 경우)
titles = soup.find_all('h2')

# 제목 출력
for i, title in enumerate(titles, 1):
    print(f'{i}. {title.get_text()}')
