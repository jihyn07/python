# 미완성 : 하지현씨 스스로의 프로젝트

# pip install selenium
from bs4 import BeautifulSoup
from selenium import webdriver
path = 'C:/Chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://isin.krx.co.kr/srch/srch.do?method=srchList")

element = driver.find_element_by_id("isur_nm1")
# input = ('ISIN을 입력해주세요')
element.send_keys("KR574401BAA2")

driver.find_element_by_link_text("조회").click()
driver.find_elements_by_class_name("strong calss").click()

