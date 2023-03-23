# 웹크롤링

# 터미널 안에서 입력
# pip install bs4 : bs4를 설치한다.
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 메모장 초기화
folderName = 'output.txt'
f = open(folderName, 'w', encoding='utf-8')
data = ''
f.write(data)
f.close()

# 사용자에게 입력값 받기
address = input('크롤링할 웹 주소를 입력해주세요.: ')
first7CharsAddress = address[0:7]
if (first7CharsAddress != 'http://' and first7CharsAddress != 'https:/'):
    address = 'http://'+address
    
response = urlopen(address)
soup = BeautifulSoup(response, 'html.parser')

for anchor in soup.select('a'):
    link = anchor.get('href', '/')
    first7Chars = link[0:7]

    if (link == '#'):
        continue

    if (first7Chars != 'http://' and first7Chars != 'https:/'):
        continue

    # 로그에 출력
    print(link)

    # 메모장에 저장
    folderName = 'output.txt'
    f = open(folderName, 'a', encoding='utf-8')
    data = link + '\n'
    f.write(data)
    f.close()
