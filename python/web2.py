#과제리뷰
#모스부호 for문으로
#공백하나->글자구분 공백두개-> 단어구분

dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}
print(dic)
def morse(src):
    res=[]
    for word in src.split('  '):
        #print(word) #입력된 문장의 단어가 3개임
        for c in word.split(' '):
            #print(c) #c에는 문자 저장
            res.append(dic[c]) #단어 저장됨
        res.append(' ') #단어와 단어가 공백문자로 구분
    return ''.join(res)


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))




#day8 과제 5번 ngram

#함수 여러개로 해보자
# def 입력()
#     return 저장변수
# def 처리()
#     return 결과
# def 출력()
#     화면출력
# 입렉데이터변수=입력(데이터1,데이터2,,)
# 결과=처리(입력데이터변수)
# 출력(결과)

def ngram(s, num):
    res=[]
    slen=len(s)-num+1
    for i in range(slen):
        ss=s[i:i+num]
        print(ss)
        res.append(ss)
    return res  # res지역변수지만 res가지고 아래 함수로 ㄷ로아감


def diff_ngram(sa,sb,num):
    a=ngram(sa,num)
    b=ngram(sb,num)
    #print(a)
    #print(b)
    cnt=0 #일치한 단어의 개수를 저장하기 위한 변수
    r=[] # 일치한 단어를 저장하기 위한 변수
    for i in a:
        for j in b:
            if i==j:#두 단어(i,j)가 일치한다면
                cnt+=1
                r.append(i)
    return cnt/len(a), r




a="오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다."
b="멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다."

r2,word2=diff_ngram(a,b,2)
print('2-gram',r2,word2)  #유사도, bigram으로 묶인 단어셋
r3,word3=diff_ngram(a,b,3)
print('3-gram',r3,word3)


#수정사항
# 1)중복 허용 안되도록!
# 2)두 문장에서 길이가 긴 문장의 단어 개수를 분모


#수업시작

# [a-zA-Z]
# [0-9]
# [^0-9]: NOT 0-9/ 대괄호 밖에있으면 시작하는


# \d: 숫자([0-9]) 와 같음
# \D : not \d의 의미 ,[^0-9]랑 같음

# \s: 공백문자, 탭문자, 엔터문자 등
# \S: not 공백문자, 탭문자, 엔터문자 의미

# \w: 문자+숫자(문자숫자 모두 포함된다는 의미), [a-zA-Z0-9_]과 같음
# \W: not 문자+숫자를 의미 [^a-zA-Z0-9_]과 같음

# ? 또는 . : 문자가 1개만 있는지 판단
# ?는 문자가 0개 또는 1개가 있으면 매치 ={0,1}=최소 0개이상 최대 1개.있어도 되고 없어도 된다
# .은 문자가 1개인지 판단

# ab?c = a뒤에 b가 있어도 없어도 됨 +c
import re
print(re.match('h?','h'))
print(re.match('h?','he'))
print(re.match('h?','his'))
print(re.match('h.','hello')) #h+문자한개 -> 매치(he)

print(re.match('ab?c','abc')) # a+ b가 있어도 없어도 됨+c
print(re.match('ab?c','ac'))
print(re.match('ab?c','abbc')) #none b가 0개또는 1개 나와야함
print(re.match('abbc','abbc'))


print(re.match('h.','hello'))

print(re.match('a.b','aab')) # ab사이에 모든문자 하나라도 있어야함
print(re.match('a.b','a0b'))
print(re.match('a.b','ab'))
print(re.match('a.b','abb'))


print(re.match('a.b','abb'))
print(re.match('a[.]b','abb')) # none
#[123]의미?
print(re.match('[123]','3')) #매치딤
print(re.match('[123]','32')) #3만 매치됨
print(re.match('[123]+','32321'))
print(re.match('[123]+','323521')) #323까지매치
print(re.match('[1-7]+','3235217')) # 다 매치됨
print(re.match('\d+','3235217'))
print(re.match('[123]+','93235217')) #none
print(re.match('[1]','1112223'))

print(re.match('a.b','abbbbb'))  #.은 문자1개
print(re.match('a[.]b','abb'))  #[.]은 특수문자(마침표)
print(re.match('a[.]b','a.b'))
print(re.match('a[.^#$]b','a#b'))
print(re.match('a[.^#$]b','a%b'))


# 빅데이터(파일)
# abc.txt  [a-zA-Z0-9]+[.]+[a-zA-Z]+
# abc.exe
# abc.cfg
# 파일명.확장자
# ...
# sadklfi 잘못된 파일명
# skdf.sdg.fdf 잘못된 파일명

# fn='abc.txt'
# res = re.match('[a-zA-Z0-9]+[.]+[a-zA-Z]+',fn)
# if res:
#     print('정상적인 파일명')
# else:
#     print('잘못된 파일명')

print(re.match('do*g','dg')) #매치됨 o가 번이상 반복
print(re.match('do*g','dog'))
print(re.match('do*g','doooog'))
print(re.match('do*g','dooookg'))

print(re.match('do+g','dg')) #none
print(re.match('do+g','dog'))
print(re.match('do+g','doooog'))
print(re.match('do+g','dooookg')) # none



# 반복 :
# {최소, 최대}
# {최소,}: 최소 횟수 이상 반복
# {,최대}: 최대 횟수 이하 반복
# {숫자}: 숫자만큼 반드시 반복

print(re.match('do{2}g','dog')) #o문자가 반드시 2번 반복
print(re.match('do{2}g','doog'))
print(re.match('do{2}g','doooog'))

print(re.match('do{2,5}g','dog')) #o문자가 2번이상 5번이하 반복
print(re.match('do{2,5}g','doog')) # o문자가 반드시 2번 반복
print(re.match('do{2,5}g','doooooooog')) #o문자가 5번초과
print(re.match('do{2,5}g','dooooog')) #o문자가 5번

print(re.match('do{2,}g','dog')) #o문자가 2번이상
print(re.match('do{,2}g','doooog')) #o문자가 2번까지만 허용
print(re.match('do{,2}g','dog'))


# 휴대폰 전화번호(3자리-4자리-4자리)/모두숫자
# 010-1234-5678  정상
# 010-1234-567 비정상
# abc-1234-567 비정상
# 01c-1234-567 비정상
# 010-12345-4566 비정상
# 01012345678 비정상
# 010-2345&9877 비정상
# ...
print(re.match('\d{3}[-]\d{4}[-]\d{4}','010-2345-6789'))


# match,search,\
# findall: 정규식과 매치되는 모든 문자열을 리스트로 리턴
# finditer: 정규식과 매치되는 모든 문자열을 반복 가능한 객체 형태로 리턴

print(re.match('[a-z]+','python'))

# <위에 코드랑 같은의미>
pat = re.compile('[a-z]+') # 정의한 패턴을 pat에 저장
res = pat.match('python') #패턴객체(pat)가 가지고 있는 match함수를 이용하여 주어잊 ㄴ문자열이 패턴에 매치되는지 확인
print(res)


print('-'*50)
print(re.match('[a-z]+','python'))
print(re.search('[a-z]+','python'))
#결과같음 , 차이점은?

print(re.match('[a-z]+','7python'))
print(re.search('[a-z]+','7python'))


print(re.match('[a-z]+','7python'))
print(re.search('[a-z]+','7python8java')) # 첫번째 만나는 문자 매치됨
#search결과는 1개의 매치 객체가 리턴

print(re.findall('[a-z]+','7python8java'))

# 위와 같은 결과
pat=re.compile('[a-z]+')
res=pat.findall('7python8java')
print(res)


res = re.finditer('[a-z]+','7python8java9cpp') #반복가능한 객체로 리ㅓㄴ
for i in res:
    print(i)
    print(i.start()) #매치된위치의 시작점
    print(i.end()) # 매치 끝 위치
    print(i.group()) # 매치된 문자열
    print(i.span()) #시작 끝위치 모두 출력/끝위치는 포함 안함

# .: 점(.) 메타문자는 모든 문자 1개와 매치됨
#예외) 매치가 안되는 문자 1개 :\n (줄바꿈문자)

print(re.match('a.b','a0b'))
print(re.match('a.b','ab'))
print(re.match('a.b','a\nb'))

pat = re.compile('a.b',re.DOTALL) #\n도 포함
print(pat.match('a\nb'))

pat=re.compile('[a-z]')
print(pat.match('python')) #p하나만 매치됨
print(pat.match('Python')) #none

pat=re.compile('[a-z]',re.I) #Ignorecase와 같음 / 대문자소문자 무시하겠다는뜻
print(pat.match('Python'))



print(re.search('\section','sdf gssgwgws \section'))
# 패턴: \s 는 엔터, 공백, 탭 등 문자

# \s를 문자열로 찾고싶을때?

print(re.search('\\\\section','sdf gssgwgws \section'))
print(re.search('\\\section','sdf gssgwgws \section'))
#\문자가 문자열 자체임을 나타내기 위해서 역슬래쉬 3개 입력

# 출력결과에 나오는 \\는 하나로 봐야함


print(re.search(r"\\section", 'sdf gssgwgws \section'))
#앞에 r붙이고 ""-> 역슬래쉬 2개가 1개로
# r"\\section -> \section


#그룹
print(re.match('ab[0-9]?c','abc')) #ab뒤에 숫자 한개가 있을수도 없을수도있음
print(re.match('ab[0-9]?c','ab9c')) #매치됨
print(re.match('ab[0-9].c','ab9c')) #매치됨


print(re.match('h{3}','hhhiii')) # h 3개 -> 매치
print(re.match('h{3}','hihihihelloworld')) #h가 먼저나오고 i가 3번 -> 매치안됨
#hi가 세번 반복되려면
print(re.match('(hi){3}','hihihihelloworld'))
print(re.match('(hi){3,5}','hihihihelloworld'))

print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}','02-1234-5678'))

print(re.match("[ㄱ-ㅎ]+",'ㅋㅋㅋㅋㅋ'))
print(re.match("[ㄱ-ㅎ]+",'ㅋㅋㅋㅋㅋ캬캬캬캬'))
print(re.match("[ㄱ-ㅎ가-힣]+",'ㅋㅋㅋㅋㅋ캬캬캬캬ㅎㅎ'))
print(re.match("[ㄱ-ㅎ가-힣]+",'ㅋㅋㅋㅋsdㅋ캬캬캬캬ㅎㅎ'))
print(re.search("[^ㄱ-ㅎ가-힣]+",'ㅋㅋㅋㅋsdㅋ캬캬캬캬ㅎㅎ'))

print(re.findall("[^ㄱ-ㅎ가-힣]+",'ㅋㅋㅋㅋsdㅋ캬234캬캬캬ㅎㅎ')) #한글 제외 모든 문자열
print(re.findall("[ㄱ-ㅎ가-힣]+",'ㅋㅋㅋㅋsdㅋ캬234캬캬캬ㅎㅎ')) #한글만 추출




news="""
(서울=연합뉴스) 신선미 기자 = 국내 신종 코로나바이러스 감염증(코로나19) '3차 대유행'이 완만한 감소세로 접어든 가운데 이번 주 신규 확진자 발생 추이가 주목된다.

신규 확진자 감소세 지속이냐 재확산이냐의 흐름을 가늠해 볼 수 있기 때문이다.

지난달 말까지만 해도 연일 1천명 안팎으로 발생하던 신규 확진자는 새해 들어 600명대로 줄었다가 11일 400명대 중반까지 더 떨어진 뒤 12일에는 500명대로 소폭 증가한 상태다.

큰 틀의 통계만 보면 확실한 감소 내지 안정국면으로 접어드는 것 아니냐는 관측이 나온다.

하지만 신규 확진자가 400명∼500명대까지 낮아진 데는 주말과 휴일 검사건수 감소 영향도 있어 아직 상황을 낙관하기에는 이르다는 게 감염병 전문가들의 공통된 의견이다.

방역당국 역시 긴장의 끈을 풀기에는 위험 요인이 너무 많다며 국민 개개인의 지속적인 방역 협조를 당부하고 있다.
"""

#뉴스에서 한글만 추출
print(re.findall('[ㄱ-ㅎ가-힣]',news)) #한글자씩
print(re.findall('[ㄱ-ㅎ가-힣]+',news))  #단어별로

#코로나19 추출
print(re.findall('[ㄱ-ㅎ가-힣]+[0-9]+',news))
print(re.findall('[0-9]+[명]+',news))
print(re.findall('[0-9]+[명|천]+',news))


print(re.match("[^A-Z]+",'Hello')) # none
print(re.match("[^A-Z]+",'hello'))

print(re.match("[0-9]+",'hello119'))
print(re.match("[0-9]+$",'hello119')) #숫자로 끝나는것것


print(re.search('[*]','3*5'))  #*문자가 있는지
# print(re.search('*','3*5')) #error
print(re.search('[*]+','3**5'))

print(re.search('\*','3 * 5')) # 특수문자 앞 역슬래쉬(\)를 붙여주면됨
print(re.search('[*]+','3 ** 5'))

print(re.search('\*+','3 *** 5')) # * 여러개
print(re.search('[ * ]+','3*5')) # none 공백이 먼저 나와야함


print(re.search("\$","$(document)"))
print(re.search("\$\([a-z]+\)",'$(document)'))

print(re.search('[$()a-z]+','$(document)'))


# (문제)

# 'abcabcabc ok' 문자열  있을 때 abc가 있는지 조사

print(re.search('abc','abcabcabc ok'))

#abc 전체 다 찾기
print(re.search('(abc)+','abcabcabc ok'))

print(re.search("\w+\s+\d+[-]\d+[-]\d+",'kim 010-1234-1234'))
# 이름+" "+전화번호
# 이렇게 매치된 문자에서 이름만 뽑아내기

res = re.search("\w+\s+\d+[-]\d+[-]\d+",'kim 010-1234-1234')
print(type(res.group()))
print(res.group())
print(res.group().split()[0]) #split함수는 디폴트가 공백문자

#좀더 좋은 방법으로
# 매치객체.group(그룹숫자)
res = re.search("(\w)+\s+\d+[-]\d+[-]\d+",'kim 010-1234-1234')
print(res)
print(res.group(1))

#group(0)은 전체!
res = re.search("(\w)+\s+(\d+)[-]\d+[-]\d+",'kim 010-1234-1234')
print(res.group(2))

res = re.search("(\w)+\s+(\d+[-]\d+[-]\d+)",'kim 010-1234-1234')
print(res.group(2))

#그룹 이름 부여
res = re.search("(?P<name>\w+)\s+(\d+[-]\d+[-](?P<num>\d+))",'kim 010-1234-1234')
# 작성형식: (?P<그룹명>..)
print(res.group('name'))
print(res.group('num'))

print(re.findall('hello|hi','hello how are you hi bye'))