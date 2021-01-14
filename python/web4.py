#ID를 이용한 다양한 데이터 참조 방법
from bs4 import BeautifulSoup
# fp = open('lang.html',mode = 'r',encoding='utf-8') #한글 포함일때 인코딩 설정
# soup = BeautifulSoup(fp,'html.parser')
# print(soup)
#
# # print(soup.select_one('ul > li')) #출력하면 첫번째 li
# # print(soup.select('ul > li'))  #리스트안에 모든 li
#
# #python 참조해보자
# print(soup.select_one('ul > li#py')) #id가 py인 데이터 추출
# # li#py 선택자 유일! -> ul 필요없음
# print(soup.select_one('li#py'))
# #id도 유일 -> li빼도됨
# print(soup.select_one('#py'))
#
#
# #좀더 복잡한 방법으로 찾아보기
# print(soup.select_one('ul#language > li#py'))
#
# #또 다른 방법
# print(soup.select_one('#language > #py'))
# print(soup.select_one('#language #py'))
# print(soup.select_one("li[id='py']"))
# print(soup.select_one('li:nth-of-type(3)'))
# print(soup.select('li')[2])
# print(soup.find_all('li')[2])



#네이버 달러 환율 정보 가져오기
import urllib.request as req

# url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
# res = req.urlopen(url).read().decode('euc-kr')  #한글안깨짐
# print(res)
# soup = BeautifulSoup(res,'html.parser')
# print(soup)

# print('달러당',soup.select('a.head.usd div > span.value')[0].string+'원')
#
#
# print('달러당',soup.select('#exchangeList > li.on > a.head.usd > div > span.value')[0].string, '원')
#
# print('금값',soup.select_one('#oilGoldList > li.on > a.head.wti > div > span.value').string)
#
# print('기사',soup.select_one('#content > div.section_news > div > ul > li:nth-child(1) > p > a').string)


#위키피디아 윤동주 검색
#
# url = 'https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC'
# res = req.urlopen(url)
# soup = BeautifulSoup(res,'html.parser')
#
# #시집 1번제목
# # print(soup.select_one('#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a').string)
#
# #시집에 수록된 모든 목록 가져오기
# mylist = soup.select('#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li')
# print(len(mylist))
#
# for li in mylist:
#     print(li.string)

#fruits-vegetables.html
#
# fp = open('fruits-vegetables.html',encoding='utf-8')
# soup = BeautifulSoup(fp,'html.parser')
# print(soup)
#
# #아보카도 찾기
#
# print(soup.select('div'))
# print(soup.select('div > ul#ve-list > li')[3].string)
#
# #class블랙인것 추출
# print(soup.select('li.black'))
# #아보카도
# print(soup.select('li.black')[1].string)
#
# # print(soup.select('#ve-list > li'))
# # print(soup.select('#ve-list > li:nth-of-type(4)')[0].string)
# # print(soup.select('#ve-list > li.black')[1].string)
# print(soup.select("#ve-list > li[data-lo='us']")[1])
#
# #find함수로 찾기
# dic = {'data-lo':'us'} #{속성명:속성값}
# #  # select=findALL, select_one = find함수
# print(soup.findAll('li',dic)) #us인것 리스트로 다 나옴
# print(soup.find('li', dic)) #포도
# #
# dic={'data-lo':'us','class':'black'}
# print(soup.find('li',dic)) #포도
#
# print(soup.find(id='ve-list').find('li')) #무
# print(soup.find(id='ve-list').find('li',dic)) #id ve-list > li>dic



#
#selenium 웹브라우저 제어하는 프로그램
from selenium import webdriver
#크롬드라이버를 다운받아 설치 c:\scrap\파일복사

#chromedriver는 크롬 웹부라우저를 제어하는 프로그램
# driver=webdriver.Chrome('c:/scrap/chromedriver.exe')
# url="https://www.naver.com"
# driver.get(url)
# html = driver.page_source
# print(html)



#멜론 실시간 인기 차트곡 수집
# url='https://www.melon.com/chart/index.htm'
# driver.get(url)
# html = driver.page_source
# # print(html)
#
# soup = BeautifulSoup(html,'html.parser')
# print(soup)
# #
# # songs=soup.select('tr')
# # print(len(songs))
# # print((songs[0])) # 노래가 아님.
# # print(songs[1]) # 위노래
# songs = soup.select('tr')[1:]
# # print(songs[0])
# song=songs[0]
#
# print(song)
#
# title=song.select('a')
# print('title')
#
# print('='*50)
# # print(song.select('div.ellipsis.rank01 > span > a')[0].string)
# # print(song.select('div.ellipsis.rank02 > span > a')[0].string)
#
#
# for song in songs:
#     print ('곡명:', song.select ( 'div.ellipsis.rank01 > span > a' )[0].string )
#     print ( song.select ( 'div.ellipsis.rank02 > span > a' )[0].string )
#     print('='*50)



#인스타그램 크롤링(제주도 맛집)



#f리뉴얼되어서 보류

# 네이버 -> 강아지 -> 이미지 탭 주소
# https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B0%95%EC%95%84%EC%A7%80
# 네이버 -> 고양이 -> 이미지 탭 주소
#https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4

#
# baseUrl='https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# word=input('검색어를 입력하세요:')
# from urllib.request import urlopen
# from urllib.parse import quote_plus
# num= int(input('개수 입력: '))
# url = baseUrl+quote_plus((word))
# print(url)
# html = urlopen(url)
# # print(html)
# soup = BeautifulSoup(html,'html.parser')
# # print(soup)
# img=soup.find_all('._img')
# print(len(img))