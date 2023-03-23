#https://hyesunzzang.tistory.com/153

from bs4 import BeautifulSoup
from selenium import webdriver

path = 'c:/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://isin.krx.co.kr/srch/srch.do?method=srchList')

element = driver.find_element_by_id("isur_nm1")
element.send_keys("KR574401BAA2")
driver.find_element_by_link_text("조회").click()
