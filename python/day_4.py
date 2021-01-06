#1. 딕셔너리 (day 3 이어서)
##1-1 clear() 모든 요소 제거/ 웹프로그래밍에서 종종 사용
dic={'아이디':'홍길동', '레벨':10}
dic.clear()
print(dic)

##1-2 키에 해당하는 값 가져오기
dic={'아이디':'홍길동', '레벨':10}
###방법 1
print(dic['아이디'])
###방법 2
print(dic.get('아이디'))

#차이점: 방법 1의 경우 존재x -> 에러, 방법2-> None

#if 문과 결합  -> "",None, 0은 거짓으로 분류됨
if dic.get('아이디'):
    print('아이디 존재')
else:
    print("아이디 존재x")
# 다른 응용
print(dic.get('기술',0)) # '기술'이라는 키 없으면 디폴트값 0


#2.set(집합) {}
##중복 제거되어야 함

##2-1 집합 만드는 법
s = set('hello')
print(s) #시퀀스 아니라서 순서가 없음
ss = set([1,2,3])
print(ss)

#빈 세트 만드는 법
s1 = {}
s2 = set()
print(s1)
print(s2)

##2-2 집합연산 (교집합, 합집합, 차집합)
s1 ={1,2,3,4}
s2={3,4,5}
#교집합
print(s1&s2)
print(s1.intersection(s2))
#합집합
print(s1|s2)
print(s.union(s2))
#차집합
print(s1-s2)
print(s1.difference(s2))


##2-3 집합에 데이터 추가
s3 = set()
#방법1
s3.add(3) # 값 한개씩만 추가 가능
print(s3)
#방법2
s3.update([1,2,3]) #여러개 추가 가능
print(s3)

##2-4 데이터 제거
s3.remove(1) #하나씩만 제거 가능
print(s3)


#3.bool 자료형: 참 or 거짓
##거짓: "", None, 0,[],(),{}  #뭐가 거짓인지 헷갈리면 print(bool(검색))

#예시
a = [1,2,3]
while a:
    print(a.pop())
print('반복문 종료')

if []:
    print('참')
else:
    print('거짓')


#4. 복사(copy)
a = [1,2,3]
b = a
print(id(a))
print(id(b))  # a와b 메모리상 주소 동일
print(a is b)

#b변수가 a값을 가져오면서 다른 주소를 가리키려면?
#방법1
a =[1,2]
b = a[:]
print(a is b)
#방법2
#copy모듈에 있는 copy함수 사용
from copy import copy
a = [1,2]
b = copy(a)
print(a is b)

#5.if 문

money=1000
card=True

if money>=5000 or card:
    print('taxi')
else:
    print('버스')


if card!=False:
    print('택시')
else:
    print('버스')


if not money <= 5000:
    print('택시')
else:
    print('버스')


if money > 3000:
    print('택시')
elif card:  #3000원 이하의 돈을 가지고 있지만, 카드를 가지고 있다면
    print('버스')
else:  #  3000원 이상도 없고, 카드도 없다
    print('도보')


s = 60
if s >=60:msg='pass'
else:msg='fail'
print(msg)

#시간 단축 코드
msg='pass' if s>=60 else "fail"
print(msg)


#6. 반복문 (while, for)

##6-1 while
i = 0
while i<6:
    i+=1
    print(i,"번째 수행")

# 무한 루프
# while True:
#     i=i+1
#     print(i)

#홀수만 print
a = 0
while a <10:
    a+=1
    if a%2==0:continue
    print(a)

#4의 배수 합 출력 ( 100 이하)
i =0
sum = 0
while i<=100:
    i+=1
    if i%4==0:
        sum= sum+i
print(sum)


##6-2 for문
# for 변수 in 리스트(문자열,튜플):
#     문장1
#     문장2

#예시
for i in 'data':
    print(i)

for i in [(1,2),(2,3)]:
    print(i)
#튜플 안의 요소 하나하나씩 출력할 때,
for i,j in [(1,2),(2,3)]:
    print(i)
    print(j)

a = [5,6,7,8]
for i in range(len(a)):  #range(4)
    print(i)

#구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=' ')
    print('')


#2~100 소수만 출력
for i in range(2,101):
    for j in range(2,i+1):
        if i==j:
            print(i)
        elif i%j==0:
            break


# 자판기(커피 한 잔에 300원이라 가정, 초기 커피는 10개)
# 돈을 넣어 주세요: 500
# 거스름돈 200를 주고 커피를 줍니다.
# 돈을 넣어 주세요: 300
# 커피를 줍니다.
# 돈을 넣어 주세요: 100
# 돈을 다시 돌려주고 커피를 주지 않습니다.
# 남은 커피의 양은 8개입니다.
# 돈을 넣어 주세요: 0
# 종료합니다


n=10
while n!=0:
    print("돈을 넣어주세요")
    pay = int(input())
    if pay >300:
        print("거스름돈은 %d을 주고 커피를 줍니다." %(pay-300))
        n-=1
        print ( "남은 커피의 양은 %d개 입니다." % n )
    elif pay ==300:
        print("커피를 줍니다.")
        n-=1
        print ( "남은 커피의 양은 %d개 입니다." % n )
    elif pay<300 and pay!=0:
        print("돈을 다시 돌려주고, 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % n)
    else:
        print("종료합니다")