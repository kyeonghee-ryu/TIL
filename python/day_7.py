#1. 내장함수

#1-1 abs() : 절댓값
print(abs(-1.2))

#1-2 all(): 모두 참 -> 참/ 하나라도 거짓 -> 거짓
print(all([' ',1,2]))

#1-3 any(): 하나라도 참-> 참/ 모두 거짓 -> 거짓
print(any([0,1,2]))
print(any([]))

#1-4 chr(): 아스키코드 -> 문자출력
print(chr(65))
#<->ord(): 문자 -> 아스키코드
print(ord('A'))

#1-5 enumerate(): 열거형 데이터 표현
#for문과 함께 많이 사용
#리스트, 튜플 문자열 데이터 (시퀀스) -> 입력 -> 인덱스 포함하는 enumerate 객체 생성

for idx, i in enumerate(['aa','bb','cc']):
    print(idx, i)

#1-6 eval(): 문자열로 구성된 수식 -> 입력 -> 문자열 실행결과 출력
print(eval('10+20'))
print(eval('divmod(4,2)'))

#1-7 filter(): 원하는 데이터 걸러내는 함수 (람다함수랑 많이 사용)
# filter(함수이름, 1번째인수에 있는 함수에 입력될 반복가능한 자료)

#<filter 사용 하지 않은 경우>
def pos(a):
    res=[]
    for i in a:
        if i>0:
            res.append(i)
    return res
print(pos([1,3,-5,7,9]))

#<filter 사용>
def pos1(a):
    return a>0

print(filter(pos1,[1,3,-5,7,9]))

#filter, lambda
print(list(filter(lambda a:a>0,[1,3,-7,9])))

#1-8 hex()
print(hex(234))


#1-9 int()
print(int('2'))
print(float('3.4'))
print(int('ea',16)) # ea를 16진수로 출력


#1-10 generator()

#1) 리스트 내포 (list comprehension)

#<일반적인 리스트 저장>
num= []
for n in range(11):
    num.append(n)
print(num)

#<리스트 내포>
print([n for n in range(11)])




#<일반적인 리스트 저장>
evenNum=[]
for i in range(1,11):
    if i%2==0:
        evenNum.append(i)
print(evenNum)


#<리스트 내포>
print([i for i in range(1,11) if i%2==0])




#<일반적인 리스트 저장>
li = []
for x in ['a','b','c']:
    for y in [1,2,3]:
        li.append((x,y))
print(li)

#<리스트 내포>
print([(x,y) for x in ['a','b','c'] for y in [1,2,3]])




#<리스트 내포 + if문 중첩 사용>
# 0~9까지 수 중, 5보다 작고 2로 나누어떨어지는 수
print([x for x in range(10) if x<5 if x%2==0])



#2) set comprehension {}
print({x+y for x in range(10) for y in range(10)})

#3) dictionary comprehension {}

print({x+y:'값' for x in range(10) for y in range(10)})

scores= {'철수':80,'영희':70}
print({name:score for name, score in scores.items() if name!='영희'})

#4) comprehension 응용
words = ['Computer','Cake','Bread']
#모두 대문자로 출력
print([w.upper() for w in words])


#a에 저장된 값이 0보다 크면 a값, 작으면 0 저장
a = [1,-5,2,4,-2,10]
print([i if i>0 else 0 for i in a])

#조건문 여러개일떄
#a=1이면 pass, 2이면 fail, 나머지는 no
a = [1,2,3,4,5]
print(['pass' if i==0 else 'fail' if i==2 else 'no' for i in a])




#2. 딕셔너리 응용

#2-1 setdefault()
x = {'a':10, 'b':20,'c':30}
x.setdefault('d')  #d: none 저장

#2-2 딕셔너리 값 변겅 : 기존에 있으면 변겅, 없으면 생성
#방법1
x['a']=100

#방법2 : update , 여러개 한번에 변경 가능
x.update(b=200)
print(x)

x.update(d=400, e=4)
# 또는
x.update({'d':400, 'e':4})

print(x)


#2-3 update, zip활용

# (zip)의 기능
print(list(zip([1,2],['one','two']))) #리스트 안에 튜플

x = {'a':10, 'b':20,'c':30}
x.update(zip(['aa','c'],['999','777']))
print(x)


#2-4 딕셔너리 데이터 삭제 (pop, del, clear)
x = {'a':10,'b':20,'c':30}

#1. pop()
x.pop('c')
print(x)  #{'a': 10, 'b': 20}

s = x.pop('b')
print(x)  #{'a': 10}
print(s)   #20

print(x.pop('z',0)) # 키 없으면 0 리턴

#2. del
x = {'a':10,'b':20,'c':30}
del x['b']
print(x)

#3. clear 전부 삭제
x.clear()
print(x)



#2-5 fromkeys() :  리스트 또는 튜플 -> 딕셔너리 생성
li = ['a','b','c']

d = dict.fromkeys(li)
print(d)

d2 =dict.fromkeys(li,10)
print(d2)


#2-6 defaultdict()

from collections import defaultdict
d2 = {'a':10, 'b':20, 'c':30}

# print(d2['z'])

d2 = defaultdict(int) # defualt가 int 인 딕셔너리
print(d2['z'])  # 없으면 디폴트 0



#2-7 키,값 출력
keys=['a','b','c']
print(dict.fromkeys(keys))

# for key,value in dict.fromkeys(keys):
#     print(key, value)  #value값 에러

for key,value in dict.fromkeys(keys).items():
    print(key, value)

#set comprehension으로 나타내기
d4 = {key:value for key,value in dict.fromkeys(keys).items() }
print(d4)



#2-8 set comprehension 응용

# 문제) newx에 x의 'b' 뺀 나머지 저장
x=['a','b','c']
x = dict.fromkeys(keys)
print(x)

newx = {k:v for k,v in x.items() if k!='b'}
print(newx)


#2-9 중첩 딕셔너리

# 딕셔너리 = {키1:{키 a: 값 a}, 키2:{키b : 값 b}}

#2-10 중첩 딕셔너리, copy()
x = {'a':{'python':3.8},'b':{'python':2.7}}
y = x.copy()
y['a']['python'] = 3.9
print(x);print(y)   # x값도 변경됨

#해결방법: copy 모듈의 deepcopy() 사용
import copy
y = copy.deepcopy(x)
y['a']['python'] = 4.0
print(y);print(x)  #y만 변경됨


