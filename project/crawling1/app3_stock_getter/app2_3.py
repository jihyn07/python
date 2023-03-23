#KRX 접속해서 상장주식수 검색하기

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from urllib.request import urlopen
from urllib.parse import quote_plus
from pathlib import Path

krCode = input('Pleae enter KR Code(6digit): ')

path = 'C:/Chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('http://marketdata.krx.co.kr/mdi#document=040601')

searchBox = driver.find_element_by_class_name("func-finder-input ")
searchBox.clear()
searchBox.click()
searchBox.send_keys(krCode)
driver.find_element_by_xpath("""//*[@id="finderbtn33e75ff09dd601bbe69f351039152189"]""").click()
