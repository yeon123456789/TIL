# https://finance.naver.com/sise/에 요청을 보내서, 응답을 받아온다.
# 스크래핑:한 번 긁어오는 것 , 크롤링:크롤러를 둔 곳에서 계속해서 정보를 가져오는 것

import requests
import bs4 #beautiful soup

url = "https://finance.naver.com/sise/"
response = requests.get(url)
#print(response.text) #response만 입력하면 200만 뜸, html코드(페이지소스) 보려면 .text

html = bs4.BeautifulSoup(response.text, "html.parser") #사람 눈에는 똑같지만 python이 읽기 좋게 정제된 것
# print(html)

kospi = html.select_one('#KOSPI_now') #마우스 오른쪽 -> 검사 -> copy selector
print(kospi.text)
