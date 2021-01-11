#1 정규표현식:복잡한 문자열 처리 (시간 단축)

jumin="""
park 850101-1234567
kim 950202-2345678
"""
print(jumin)

#jumin데이터의 뒷부분을 모두 *로 변환하여 출력
print(jumin.split('\n'))  #['', 'park 850101-1234567', 'kim 950202-2345678', '']

#  주의!
# pithon ->python 할때
s='pithon'
# s[1]='y'
# print(s)  에러!
print(s[0]+'y',s[2:])  #이렇게 해야함


for line in jumin.split('\n'):
    for word in line.split(" "):
        if len(word)==14:
            word=word[:6]+'-'+'*******'
            print(word)
#-> 번거로움
# -> 주민번호 앞자리 7자리이거나, 뒷자리에 알파벳등 잘못입력하면? 분류하면 안된다

#제대로 입력했는지도 체크하고자 한다! -> 코드 엄청 복잡해짐

# 정규표현식 필요!


#순수 파이썬 함수 사용
d='1234'
print(d.isdigit())
d='12s34'
print(d.isdigit())



for line in jumin.split('\n'):
    for word in line.split(" "):
        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
            word=word[:6]+'-'+'*******'
            print(word)


#정규표현식으로

jumin="""
park 850101-12a4567
kim 950202-2345678
"""

import re #regular expression(정규 표현식 모듈)
p=re.compile("(\d{6})[-]\d{7}")  #정규식 작성
print(p.sub('\g<1>-*******',jumin))

#정상적인 주민번호에 대한 일반적인 규칙을 정의 (숫자6자리-숫자7자리)

# re.match('패턴','문자열') #문자열이 패턴에 부합되나요?
#문자열은 주어짐, 패턴 잘 정의하자

# 'hello world' 문자열에 hello문자열이 있는지 판단
#매치가 됨(매치객체 return)
print(re.match('hello','hello world')) #<re.Match object; span=(0, 5), match='hello'>
##span-> 위치 0번부터 5번전까지

#매치가 안됨
print(re.match('hi','hello, world')) #None

if re.match('hello','hello, world'):
    print('주어진 hello, world문자열은 hello 문자열 패턴에 매치됐습니다')

else: print('매치되지 않았습니다.')

#find쓰는것과같음
#문자열 복잡해지면 정규표현식 쓰는것 권장
print('hello, world'.find('hello'))

#특정 문자열이 맨앞/뒤에 오는지 판단?
# 문자열 맨 앞에 ^를 붙이면 맨 앞에 오는지 판단
#         끝에 $를 붙이면 맨 끝에오는지 판단

#hello로 시작하는지 확인
print((re.search('^hello','hello,world')))
#<re.Match object; span=(0, 5), match='hello'>

#world로 끝나는지 확인
print(re.search('world$','hello,world'))
#<re.Match object; span=(6, 11), match='world'>


#hello또는 world문자열이 포함되어있는지 확인
print(re.match('hello|world','hello'))
#<re.Match object; span=(0, 5), match='hello'>
print(re.match('hi|world','hello'))
#none


#정규표현식 메다문자
# (메타: 정보의 정보, 데이터(전화번호부)의 데이터(색인=인덱스, ),
#   고유의 의미가 아닌 특정 의미로 사용됨
# ex: () {} [],|,\,?,*,+
#의미 하나하나 알아야함

"""
[] 메타문자 (대괄호 메타문자): 대괄호 안에 어떤 문자도 올 수 있음
ex) [abcdef] 의미? a,b,,,f 중에서 어떤 한개의 문자와 매치
'a'문자는 정규표현식에 매치됨

"""
print(re.match('[abcdef]','a')) # 매치됨
#<re.Match object; span=(0, 1), match='a'>

print(re.match('[abcdef]','g')) # 매치 안됨
#none

print(re.match('[abcdef]','abc')) #매치됨
#<re.Match object; span=(0, 1), match='a'>

print(re.match('[abcdef]','c')) # 매치됨
#<re.Match object; span=(0, 1), match='c'>

#re.match, re.search 다름
#match는 처음에 안나오면 안됨

# [from-to]
# [a-d] 정규식의미: [abcd],[a-f]==[abcdef]
# [0-5]==[012345]

print(re.match('[0-9]','1234')) #1234는 0-9에 해당 -> 매치됨
# [0-9]는 하나의 문자

print(re.match('[0-9]*','1234')) #1234는 0~9까지 문자[숫자]가 0개 이상 있는지 확인
#1,2,3,4모두 해당됨

# *: 0개 이상 있는지 확인
print(re.match('[0-9]*','a1234')) #a1234는 a부터 매치가 안됨 (a는 0-9사이 아님)
#<re.Match object; span=(0, 0), match=''>    0개 존재, 객체나옴

print(re.match('[0-9]','a1234'))
#none


# + : 1개 이상 나오면 매치됨
print(re.match('[0-9]+','1234'))
# <re.Match object; span=(0, 4), match='1234'>

print(re.match('[0-9]+','12a34'))
# <re.Match object; span=(0, 2), match='12'>
#문자 a부터 매치안돼서 끝남

print(re.match('[0-9]+','a12a34'))
# None
print(re.match('[0-9]*','a12a34'))
# <re.Match object; span=(0, 0), match=''>
#a까지 매치된걸로봄 a->0개 / match='' 매치된 것은 없고 객체만나온것



# [a-z],[A-Z],[a-zA-z],
# ^ 가 대괄호 안에있을때 :not/ 대괄호 밖일때 -로 시작
# [^0-9]:0-9(숫자)를 제외한 문자
# ^hello :hello로 시작하는문자


print(re.search('^hi','hello, hi')) # 문자열이 hi로 시작해야함
#none
print(re.search('hi', 'hello,hi')) # span=(6, 8), match='hi'
#<re.Match object; span=(6, 8), match='hi'>
print(re.match('hi','hello,hi')) # none

print(re.match('hello|hi|good','hi')) #매치됨 셋중하나만 되면!
# <re.Match object; span=(0, 2), match='hi'>

print(re.match('[0-9]','12a3bcd')) # 매치됨
# <re.Match object; span=(0, 1), match='1'>

print(re.match('[0-9]*','12a3bcd')) # 숫자가 0개이상있는지 판단 -> 매치됨

print(re.match('[0-9]+','12a3bcd')) # 숫자가 1개이상있는지 판단
# <re.Match object; span=(0, 2), match='12'>





# 위에 두개 차이점? a먼저 오면 달라짐
print(re.match('[0-9]*','a12a3bcd')) # 숫자가 0개이상있는지 판단 -> 매치됨
#<re.Match object; span=(0, 0), match=''>
print(re.match('[0-9]+','a12a3bcd'))
#none


print(re.match('[a-z]*','12a3bcd'))
#<re.Match object; span=(0, 0), match=''> 0개매치
print(re.match('[a-z]+','12a3bcd'))
# none


print(re.match('[a-z]*','aabb12a3bcd'))
# <re.Match object; span=(0, 4), match='aabb'>
print(re.match('[a-z]+','aabb12a3bcd'))
# <re.Match object; span=(0, 4), match='aabb'>


print(re.match('ab','abc'))
# <re.Match object; span=(0, 2), match='ab'> ab까지 매치됨
print(re.match('ba','abcba'))
#none

#위에 두개를 search로 구현하면
print(re.search('ab','abc'))
# <re.Match object; span=(0, 2), match='ab'>
print(re.search('ba','abcba'))
# <re.Match object; span=(3, 5), match='ba'>


print(re.match("a*",'b')) # *앞에있는 문자 0개이상매치되면 매치
#<re.Match object; span=(0, 0), match=''>

print(re.match("b*",'b'))
# <re.Match object; span=(0, 1), match='b'>

print(re.match("a*b",'b')) #a문자가 0개이상 있고, b가 나오면 매치
# <re.Match object; span=(0, 1), match='b'>

print(re.match("a*b",'bb'))
# <re.Match object; span=(0, 1), match='b'>

print(re.match("a+b",'bb')) #a문자가 1개이상 나와야하고, 반드시 그뒤에 b가 나와야함
#none

print(re.match("a+b",'ab'))
# <re.Match object; span=(0, 2), match='ab'>

print(re.match("a+b",'aaab'))
# <re.Match object; span=(0, 4), match='aaab'>

print(re.match("a+b+",'aaab'))  # a,b 1개이상

print(re.match("a+b*",'aaaaaaabb'))

print(re.match("a+cb+",'aaaaaacb'))

print(re.match('a+b*','aaaaabbbcc'))
# <re.Match object; span=(0, 8), match='aaaaabbb'>

#패턴이 문자열에 있는지만 보면 됨( 문자열이 패턴을 반드시 가지고있어야함)

print(re.match('a+b*k','aaaaabbbcck'))
# none

# 사용예시
# 대한한한한한민국= 대한민국으로 만들고싶을때
print(re.match('대한+민국','대한민국'))
print(re.match('대한+민국','대한한한한한민국'))


#대괄호쓰면 한문자
# [a-z]+ :알파벳 한 문자 이상
