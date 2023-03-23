#JPX발행가능주식수 검색

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from urllib.request import urlopen
from urllib.parse import quote_plus
from pathlib import Path

jCode = input('Pleae enter J Code: ')

# list = []
# n = 1

# for i in range(isinNumber):
#     i = input('ISIN을 입력해주세요: ')  
# #        break

# baseUrl = 'https://www2.tse.or.jp/tseHpFront/StockSearch.do?method=&topSearchStr='
# url = baseUrl + quote_plus(jCode)
# html = urlopen(url)
# soup = bs(html, "html.parser")

path = 'C:/Chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www2.tse.or.jp/tseHpFront/StockSearch.do?method=&topSearchStr='+quote_plus(jCode))
    # element = driver.find_element_by_id("isur_nm1")
# element.send_keys(isin)

driver.find_element_by_class_name("activeButton").click()

#xpath 위치의 정보를 받아오기 (xpath 사이에"있으면 """로커버 )
table = driver.find_element_by_xpath("""//*[@id="body_basicInformation"]/div/table[3]/tbody/tr[2]/td[2]""")

print(table.text)

#  tr td 나눠주는 코드  from https://m.blog.naver.com/hjinha2/221830387511
#  for tr in table.find_elements_by_tag_name("tr"):
#     td = tr.find_elements_by_tag_name("td")
#     s = "{} , {}\n".format(td[1].text , td[2].text)
#     print (s)
#         # fp.write(s)

driver.quit()








# driver.find_element_by_link_text("조회").click()
# driver.find_element_by_link_text(isin).click()