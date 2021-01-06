#1. 함수
# def 함수명(매개변수):
#     문장1
#     문장2

##1-1 def함수 종류

#1) 입력값, 출력값 모두 있는 함수
def add(a,b):
    return a+b
res=add(1,2)
print(res) #3

#2) 입력값이 없는 함수
def say():
    return 'hello'
print(say())  #hello

#3) 출력값이 없는 함수 (return뒤에 값이 없음-> return 생략가능)
def add(a,b):
    print("두 수의 합:",a+b)
add(3,4) #두 수의 합: 7

#4) 입력값, 출력값 모두 없는 함수
def say():
    print('hello')
say()  #hello


##1-2. 매개변수 초기값 설정
def add(a,b=3):
    return a+b
res = add(2)
print(res) #5
print(add(2,5)) #7 #매개변수 지정되어 있어도, 인수가 입력되면 인수 우선
#디폴트값을 두고, 인수 있으면 인수를 지정할 때 유용
#단, 인수의 수 > 매개변수의 수 이면 에러!


##1-3. 함수로 전잘되는 인수의 개수가 정해지지 않은 경우: *arg
def add(*arg):
    res=0
    for i in arg:
        res+=i
    return res

print(add(1,2,3,4))

#(문제) add와 mul 결합된 함수 만들기
def addmul(op,*arg):
    if op=='add':
        res=0
        for i in arg:
            res+=i
        return res
    elif op=='mul':
        res=1
        for i in arg:
            res*=i
        return res
print(addmul('add',1,4,4))
print(addmul('mul',3,2,4))


##1-4. 함수 결과를 각각 저장
def am(a,b):
    return a+b, a*b

print(am(2,3)) # (5, 6)

#방법1
res=am(2,3)
r1=res[0]
r2=res[1]
print(r1,r2) #5 6

#방법2
r1,r2=am(2,3)
print(r1)
print(r2)

##1-5) return의 기능
def prn(a):
    if a=='안녕':
        return
    print('반가워')
prn('안녕') #return에서 다시 여기로 돌아옴
prn('안뇽') #return 지나치지 않고 print

#(문제)
def info(name,age,man=True):
    print("내 이름은",name)
    print("나이는", age)
    if man:
        print('성별은 남자')
    else:
        print('성별은 여자')

info('홍길동',25, True)
info('제니',25,False)

##1-6 변수의 범위(scope)

#함수 안 변수가 밖에서도 영향을 받으려면?

#방법1 return
a=1
def add(a):
    a=a+1
    return a
a = add(a)
print(a) #2

#방법2 global
a=1
def test():
    global a #밖의 a가 됨
    a=a+1
test()
print(a) #2

##1-7 람다함수: def와 동일한 기능 수행하는 예약어 (def가 일반적, def사용하지 못하는 상황에서 사용)

#(def)
def myadd(a,b):
    return a+b
print(myadd(1,2))

#(람다)
myadd=lambda a,b :a+b
print(myadd(2,4))

#(문제):최대값 구하는 함수 만들어보자
def mymax(*arg):
    m=0
    for i in range(len(arg)):
        if m <arg[i]:
            m=arg[i]
    return m
print(mymax(2,4,8))

#람다함수 자체 바로 호출 -> 함수이름 정의할 필요 없다
print((lambda x,y:x+y)(1,2))

#람다함수 내에서 변수 생성 불가능
# (lambda x,y=3:x+y)(1) #문법 오류

#인수 부분에 간단한 함수 적용하는 경우

# def pt(x):
#     return x+10
# print(pt([2,3,3])) # 문법오류 [1,2,3]+10

#해결해보자
#(def)
def pt(x):
    return x+10
print(list(map(pt,[1,2,3])))

#(lambda)
print(list(map(lambda x:x+10,[1,3,4])))