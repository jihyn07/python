# [클릭 등의 조작 후에 정보를 가져옴]

# pip install selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen

# 크롤링대상 찾기
path = 'C:/Chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("http://azumaj.jbhomelove.com/")
# element = driver.find_element_by_id("isur_nm1")
# #input = ('ISIN을 입력해주세요')
# element.send_keys("KR574401BAA2")
driver.find_element_by_link_text("Home in New Tab").click()
# driver.find_elements_by_class_name("strong class").click() # 클래스명으로 가져옴

# 첫번째 탭에 있는 정보를 가져옴
address = driver.current_url

# 두번째 탭에 있는 정보를 가져옴
# ?

# 메모장 초기화
folderName = 'output3.txt'
f = open(folderName, 'w', encoding='utf-8')
data = ''
f.write(data)
f.close()



# ★여기를 수정하고 싶으면 먼저 html, css 정도에 대한 이해를 해야합니다.
# 사용자에게 입력값 받기 
# address = input('크롤링할 웹 주소를 입력해주세요.: ')
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
    folderName = 'output3.txt'
    f = open(folderName, 'a', encoding='utf-8')
    data = link + '\n'
    f.write(data)
    f.close()


print(address)