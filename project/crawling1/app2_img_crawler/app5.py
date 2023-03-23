# [다수 검색어 이미지 크롤링]
    # 소스코드 : app4에서 복사해 옴
    # 숙제 : 폴더명 검색어명으로 해서 여러개의 폴더 생성, 검색어 갯수 정하고 그만큼 검색어 칠 수 있도록 생성

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
from pathlib import Path

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어 입력: ') 
crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))

url = baseUrl + quote_plus(plusUrl) 
html = urlopen(url)
soup = bs(html, "html.parser") 
img = soup.find_all(class_='_img') 

Path("./img").mkdir(parents=True, exist_ok=True)
n = 1
for i in img:
    print(n)
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./img/img' + str(n)+'.jpg','wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    if n > crawl_num:
        break
    
print('Image Crawling is done.')