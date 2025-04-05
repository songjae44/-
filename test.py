import requests
from bs4 import BeautifulSoup

# 웹 페이지 요청
url = "https://www.dailysecu.com/news/articleList.html?sc_section_code=S1N6&view_type=sm"  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 뉴스 제목 가져오기
news_titles = soup.select("#user-container > div.float-center.max-width-1080 > div.user-content > section > article > div.article-list > section > div > div.list-titles > a > strong")

# 출력
for title in news_titles:
    print(title.text)
