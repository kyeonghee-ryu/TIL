#1. html 데이터 참조

from bs4 import BeautifulSoup
fp = open('html1.html',mode='r', encoding='utf-8')
soup = BeautifulSoup(fp,'html.parser')

#python을 다양한 방법으로 참조해보자
print(soup.select_one('li#py'))
print(soup.select('li')[2])
print(soup.select('ul > li')[2])
print(soup.select('li')[2])
print(soup.select_one('li[id=py]'))
print(soup.select_one('li:nth-of-type(3)'))
print(soup.find(id='language').find(id='py'))
print(soup.find(id='py'))
print(soup.find_all('li')[2])


#2. 웹크롤링


#2-1 네이버 환율 정보 크롤링
import urllib.request as req
url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
res = req.urlopen(url).read().decode('euc-kr')
soup=BeautifulSoup(res,'html.parser')

d = soup.select_one('a.head.usd div > span.value') #달러당 환율
print('달러당 환율:',d.string)

news = soup.select('div.section_news > div > ul > li')
for i,j in enumerate(news):
    print('{}번째 뉴스 : {}'.format(i+1,j.text.strip()))


#2-2 위키피디아 윤동주시인 검색
import urllib.request as req
from bs4 import BeautifulSoup
url = 'https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC'
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

poem_list=soup.select('ul:nth-child(6) > li > ul > li')
for i in poem_list:
    print(i.text.strip())


#2-3 find함수로 선택자 불러오기

#select = findALL, select_one = find

fp =open('fruits-vegetables.html',mode='r', encoding='utf-8')
soup = BeautifulSoup(fp,'html.parser')
print(soup)
# <html>
# <body>
# <div id="main-goods" role="page">
# <h1>과일과 야채</h1>
# <ul id="fr-list">
# <li class="red green" data-lo="ko">사과</li>
# <li class="purple" data-lo="us">포도</li>
# <li class="yellow" data-lo="us">레몬</li>
# <li class="yellow" data-lo="ko">오렌지</li>
# </ul>
# <ul id="ve-list">
# <li class="white green" data-lo="ko">무</li>
# <li class="red green" data-lo="us">파프리카</li>
# <li class="black" data-lo="ko">가지</li>
# <li class="black" data-lo="us">아보카도</li>
# <li class="white" data-lo="cn">연근</li>
# </ul>
# </div>
# </body>
# </html>


#아보카도를 찾아보자
print(soup.select('ul#ve-list > li')[3].string)
print(soup.select('li.black')[1].string)
print(soup.select('#ve-list > li:nth-of-type(4)')[0].string)
print(soup.select_one('#ve-list > li:nth-of-type(4)').string)

#find 함수 이용

dic ={'data-lo':'us'}
print(soup.findAll('li',dic)) #해당하는것 모두 리스트로 출력
print(soup.find('li',dic)) # 제일 처음것 출력(포도)

print(soup.findAll('li',dic)[3])  #아보카도

dic = {'data-lo':'us','class':'black'}
print(soup.find('li',dic))
print(soup.find(id='ve-list').find('li',dic))


#3) selenium: 웹브라우저 제어하는 프로그램
# chromedriver : 크롬 웹브라우제 제어하는 프로그램

from selenium import webdriver
driver = webdriver.Chrome('c:/scrap/chromedriver.exe')
url='https://www.melon.com/chart/index.htm'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
print(soup)

#멜론 인기차트 출력
song = soup.select('tr > td:nth-child(4) > div > div > div.ellipsis.rank01')
singer = soup.select('tr > td:nth-child(4) > div > div > div.ellipsis.rank02')
for (i,j) in zip(singer,song):
    print('가수:{} 제목:{}'.format(i.text.strip(),j.text.strip()))
    print('-'*50)