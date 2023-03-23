# [이미지 크롤링]
    # 구글 검색 : 파이썬 이미지 크롤링
    # 참조한 사이트 : https://bskyvision.com/721

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
from pathlib import Path

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어 입력: ') 
crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))

# 한글 검색 자동 변환 (파싱: 웹이 이해할 수 있는 언어로 변환)
url = baseUrl + quote_plus(plusUrl) 
# 웹이 이해할 수 있는 언어로 url을 파싱해서 웹에 전달
html = urlopen(url)
# soup 변수에 해당 url의 모든 소스코드가 들어감
soup = bs(html, "html.parser") 
# img 변수에 soup 변수 안에 있는 것들 중 class가 _img 인 것들만 찾아서 담음 
img = soup.find_all(class_='_img') 

# 폴더 만들기
Path("./img").mkdir(parents=True, exist_ok=True)

# n(돌릴 횟수) 초기값 지정
n = 1

# n의 갯수만큼 이미지 추출 반복
for i in img:
    print(n)
    # 이미지의 실제 장소는 <img src="" ... data-source="이 부분">에 있는데, 그것을 추출해내서, imgUrl 변수에 담는다.
    imgUrl = i['data-source']
    # urlopen(imgUrl)을 f로 치환
    with urlopen(imgUrl) as f:
        with open('./img/img' + str(n)+'.jpg','wb') as h: # w - write b - binary
            # f = 이미지의 주소를 가져온다. 
            # .read = 그것을 이미지 파일로 변환한다. 
            # 그 이미지 파일을 img 변수에 담는다.
            img = f.read()
            # 정해진 폴더에 .jpg 확장자를 "덮어씌우기, 이진법"의 형태로 담는다.
            h.write(img)
    # 실행한 횟수를 1 추가한다.           
    n += 1
    # 지정 횟수를 초과하지 않으면 뒤로 돌아가고, 초과하면 반복문을 나간다.
    if n > crawl_num:
        break
    
# 반복문이 나가지면(작업이 끝나면) 실행된다.    
print('Image Crawling is done.')