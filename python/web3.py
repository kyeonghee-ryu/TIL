#
# import re
# print(re.match('\d{4}','1234'))
# print(re.match('\d{4}','12345')) #매치됨 -> 비정상적인 번호로 분류하려면?
#
# if re.match('\d{4}$','12345'):  #반드시 숫자 4자리로 끝나야함
#     print('정상 전화번호')
# else:
#     print('비정상 전화번호')
#
#
# #sub함수
#
# # 대한민국,한국,코리아...-> 대한민국
#
#
# # re.sub('패턴','바꿀문자열','문자열',바꿀횟수)
# print(re.sub('apple|orange','fruit','apple tree banana orange'))
#
#
# '1 2 apple 3 banana 4 7 9 20 tree'
# # 수치데이터 -> 'num'으로 변경
# print(re.sub('\d+','num', '1 2 apple 3 banana 4 7 9 20 tree'))
#
# #바꿀 횟수 지정 / 생략하면 모두 다 바꿈
# print(re.sub('\d+','num', '1 2 apple 3 banana 4 7 9 20 tree',1))
#
#
# # compile사용
# print(re.sub('apple|orange','fruit','apple tree banana orange'))
#
# pat = re.compile('apple|orange')
# res = pat.sub('fruit','apple tree banana orange')
# print(res)
#
#
#
# import urllib.request
# url='https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png'
# # urllib.request.urlretrieve(url, 'test.png')
# # print('저장되었습니다')
# mem = urllib.request.urlopen(url).read()
# with open('test2.png','wb') as f:
#     f.write(mem)
#     print('저장되었습니다.')



#xml 문서 읽어서 원하는 자료 가져오기

# 웹에서 사용하는 언어 중 하나
# -웹에서 사용하는 언어: 서버와 클라이언트간에 데이터를 주고받을때 사용하는 언어
# 클라이언트(페이지 요청, 웹브라우저에 www.naver.com입력 )-> 웹서버-> 메인 페이지 제공(보통 index.html)

#  예시: HTML(Hyper Text Markup Language/비구조적문서/정적페이지
#       XML : extensible markup language (확장 가능한 마크업 언어)/구조화된문서/정적페이지

#       구조화된문서: 의미를 이해할 수 있는 식으로 작성됨
#       비구조화된 문서: 문서에 대한 구조를 컴퓨터가 이해하기 어려움

# 클라이언트(날씨 클릭) -> 웹서버(날씨페이지 (동적 페이지)생성)->생성되 페이지 html문서로 만들어서 제공
# -> 웹브라우저 해석 -> 결과를 화면에 출력
# 오늘의 날씨는 맑습니다. 기온은 섭씨 영하 2도 입니다.

# 정적 vs동적 페이지
# 정적 페이지: 변하지 않는 내용(html, xml)/ 동적페이지: 클릭할때마다 내용 바뀜(jsp,asp,php)

# 검색어 :BTS
# 노래제목, 멤버들, ... 검색-> BTS
# 비구조화된 문서: 웹페이지 내용에 대해 기계가 해석하지 못하는 문서
#   BTS가 서울 강남구에서 공연을 했습니다. 의 내용 -> 해석못함
# -> 검색어 기반 검색
# 구조화된 문서:웹페이지 내용에 대해 기계가 해석 가능한 문서
#  <가수>
#   <그룹명>BTS</그룹명>
#   <도시이름>서울</도시이름>
#   <구이름>강남구</구이름>
#   <멤버이름>...</멤버이름>
#  </가수>
#  검색어들의 의미를 기반으로 검색, 검색폭넓음, 검색 결과에 대한 정확도 높음

# http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp



import urllib.parse as parse
import urllib.request as request
# addr = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
#
# values={'stdId':'109'}
# params = parse.urlencode(values)
# url=addr+'?'+params
# print(url)
#
# # data = request.urlopen(url).read()
# # print(data) # 16진수로 나온다
#
# data = request.urlopen(url).read()
# data = data.decode('utf-8')
# print(data)


#제주시의 1월 16일 자정 온도
# -> beautifulsoup패키지

from bs4 import BeautifulSoup
html="""
<html>
<body>
<h1>스크래핑</h1>
<p>웹페이지 분석</p>
<p>원하는 부분 추출</p>
</body>
</html>
"""
# soup =BeautifulSoup(html, 'html.parser')
# #붕어빵봉투=붕어빵기계(크림,10cm)
# # BeautifulSoup은 클래스
# print(soup.html.body.h1)
# print(soup.html.body.p)
# print(soup.html.body.p.string) # 태그 안에 있는 문자열만 추출
#
# p1=soup.html.body.p
# print(p1.next_sibling) # </p>뒤에 줄바꿈 문자 가져온것
# p2=p1.next_sibling
# print(p2.next_sibling)
#
# #  위에 코드 한줄로 표현
# p2=p1.next_sibling.next_sibling.string
# print(p2)

html2="""
<html>
<body>
<h1 id='title'>스크래핑</h1>
<p id='body'>웹페이지 분석</p>
<p>원하는 부분 추출</p>
</body>
</html>
"""

soup=BeautifulSoup(html2,'html.parser')
# print(soup.html.body.h1.string)
# print(soup)
# print(soup.html.body)
print(soup.find(id='title'))
print(soup.find(id='title').string)
print(soup.find(id='body').string)


html3="""
<html><body>
<url>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
</url>
</body></html>
"""


# <태그명 속성명=속성값 속성명-속성값 ...>
soup = BeautifulSoup(html3, "html.parser")
print(html3) #문자열을 저장하고있는 변수
print(soup) #문자열->html파서로 분석할 수 있는 객체로 변환


# 보기에는 차이없어보이지만 html3은 변수에 불과함
#
# print(soup.find_all('a'))
# # print(html3.find_all('a')) # 에러 !=soup
#
# links = soup.find_all('a') # 리스트로 저장
#
# print(links[0]) # 네이버
# print(links[1])  #다음
#
# for i in links:
#     print(i.attrs['href'])  #href 속성만 출력
#
# for i in links:
#     href= i.attrs['href']
#     na = i.string
#     print(na,'-->',href)
#
#
# html4 ="""
# <p><a href='aaa.html'>aaa page</a></p>
# """
#
# soup =BeautifulSoup(html4,'html.parser')
# print(soup)
# print(soup.p) #p태그로 이동
# print(soup.p.a) # p->a태그로 이동
# print(soup.p.a.string)
# print(soup.a) #p태그부터 접근할필요없다
# print(soup.a.string)
#
# #a태그 여러개있을때 p.a 로 접근하면 됨
#
#
# print(soup.a.attrs) #{'href': 'aaa.html'} #attribute:값으로 나열



html4="""
<p><a href="aaa.html" name="kkk">aaa page</a></p>
"""
soup=BeautifulSoup(html4,"html.parser")
print(soup)
print(soup.p)

print(soup.p.a)  #a태그가 다양한 태그 속에 들어가 있을 때는 반드시
print(soup.p.a.string)#상위 태그인 p.a로 작성해야함
print(soup.a)
print(soup.a.string)
print(soup.a.attrs)  # 딕셔너리 구조:{'href': 'aaa.html', 'name': 'kkk'}

mydict=soup.a.attrs
print(mydict.keys())
print(mydict.values())
print(mydict.items())
print('href' in mydict)
print('hreff' in mydict)

print(mydict)
# 값만 출력
dic=soup.a.attrs
print(dic)
print(dic.values)

#다른 방법
print(list(dic.values())[1])

#다른 방법
soup.a.attrs.get('name')



import urllib.request as req


url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url)
print(res)  #<http.client.HTTPResponse object at 0x000001ABBFA27488>
#내용물이 바로 보이는 것이 아님
#HTTPResponse :(객체형태)
# res: 페이지 내용이 담겨있는 포장지(봉투) ->가져오고싶어서 beautifulsoup사용

# 클라이언트-> 서버한테요청했을때
# 정상응답 =>200:ok
# 문서를 찾지 못한경우 => 40x
# 서버 자체 오류 (전원중단으로 인한 오류)=>

soup = BeautifulSoup(res,'html.parser')
print(type(soup)) #<class 'bs4.BeautifulSoup'>

# print(soup) # 웹스크래핑
# print("문서제목:",soup.title.string)  #처음 나오는title
#
# #다른 방법으로 제목 가져오기
# print(soup.find('title')) #<title>기상청 육상 중기예보</title>
# print(soup.find('title').string) #기상청 육상 중기예보
#
#
# print(soup.find_all('title')) # 모든 title태그 가져옴
# print(soup.find_all('title')[0].string)

#모든 wf 태그의 내용을 출력
# print(soup.find('wf').string)
print(len(soup.find_all('wf')))  #534개






from bs4 import BeautifulSoup

html4 = """
<html><body>
<div id="lang">
    <h1>programming</h1>
    <ul class="items">
        <li>python</li>
        <li>java</li>
        <li>cpp</li>
    </ul>
</div>
</body></html>
"""

# ul:unorderd list:순서가 없는 목록 리스트
# ol:orderd list:순서가 있는 목록 리스트

soup = BeautifulSoup(html4, 'html.parser')
# print(soup.select('div'))
#자료구조 리스트 형태로 통으로 들어감
#[<div id="lang">
# <h1>프로그래밍언어</h1>
# <ul class="items">
# <li>python</li>
# <li>java</li>
# <li>cpp</li>
# </ul>
# </div>]

# print(soup.select('div#lang'))  #div태그 하나라서 위와 동일한 결과
# print(soup.select('div#lang > h1')[0].string)

# print(soup.select_one('div#lang > h1'))  #<h1>programming</h1>

#select,select_one차이점 : select는 리스트로 출력, one은 문자열로 나옴
#select 용도 -> 태그 여러개 모두 추출할때 사용
#select_one-> 한 개를 추출할 때


# li태그 가져올때
# print(soup.select('div#lang > ul'))
#위에랑 대괄호 유무 차이
# print(soup.select_one('div#lang > ul'))

# print(soup.select('div#lang > ul.items'))

# print(soup.select('div#lang > ul.items > li'))
#[<li>python</li>, <li>java</li>, <li>cpp</li>]

# print(soup.select_one('div#lang > ul.items > li'))
#<li>python</li>

mylist = soup.select('div#lang > ul.items > li')
for i in mylist:
    print(i.string)