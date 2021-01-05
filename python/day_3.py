#1. 튜플 () : 리스트와 거의 동일/ 차이점: 튜플은 값 변경 불가능-> 자료 변경하지 않을 때 사용

#1-1 참조: 리스트와 동일하게 인덱싱, 슬라이싱 가능
t1 =(1,2,3,4)
print(t1[0:2])

#1-2 튜플끼리 덧셈가능, 상수와 곱셈 가능
t1 = (1,2)
t2 = (3,4,5)
print(t1+t2)
print(t2*3)

#1-3 len 사용 가능
print(len(t1))

#1-4 요소가 여러 타입이 될 수 있음
person = ('kim', 24, 100)

#1-5 작성 방법

t4 = () # 빈 튜플
# t4 = (7) -> 에러: 정수로 취급함
t4 = (7,)
# t5 = 5 8 -> 튜플이 되지만, 좋은 방법아님
print(tuple(range(5))) # rnage 이용해서 tuple생성

#1-6 값 변경 (리스트로 변경 후 값 변경)
t1 = (1,2,3)
tempt = list(t1)
tempt[0]=12
print(tempt)
t1 = tuple(tempt)
print(t1)

#1-7 문자열도 튜플 가능
print(tuple('hello'))


#2. sequence: 연속적으로 저장
## 리스트, 튜플 문자열, range, (bytes, bytearray)

#2-1 데이터 존재 유무 확인 (in)
a = (1,2,3)
print(3 in a)

#2-2 시퀀스 객체 연결 (덧셈 연산자 이용), 단 range는 불가능
a=[1,2]
b=[2,3,4]
print(a+b)

## range-> 굳이 덧셈연산을 이용하고 싶다면,
a = list(range(3))
b = list(range(2))
print(a+b)

##문자열
print("hi"+'hello')
print("Hi"+str(10)) # 숫자와 더할 때는 숫자를 문자형으로 변환 후 연산

##2-3 시퀀스 반복 (곱셈 연산자 이용), 단 range는 불가능
a =[10,20,30]
print(a*3)

##range를 쓰고 싶다면, list로 변환후 연산


##2-4 데이터 개수 세기 :len(시퀀스객체)
print(len([1,2,3]))
print(len("안녕"))
print(len('안녕'.encode('UTF-8'))) #한글 UTF-8일때, 한 글자당 3바이트

##2-5 시퀀스 객체 []로 참조
print(range(3,10,2)[3])

#단 인덱스 벗어나면 오류


##2-6 del 시퀀스객체[인덱스] -> 삭제, 단 튜플,range,문자열 불가능
b = [10,20,30,40,50]
del b[:3:2]
print(b)

##2-7 slice() : 슬라이싱
print(range(20)[slice(3,9,2)])
print(list(range(20)[slice(3,9,2)]))


## 2-8 또 다른 데이터 변경법

a = list(range(10))
print(a)
a[1:4]='a'
print(a)  #[0, 'a', 4, 5, 6, 7, 8, 9]

a = list(range(10))
a[1:4]=['a','b','c']
print(a)  #[0, 'a', 'b', 'c', 4, 5, 6, 7, 8, 9]

#단 참조하는 데이터보다 많거나 적을 때 에러
# a = list(range(10))
# a[2:7:2]=['x','y','z','q']
# print(a)   #참조하는 데이터 4개라서 에러

## 2-9 del+slice -> 삭제가능
a = list(range(10))
del a[2:5]
print(a)



#3. 딕셔너리: 자료 저장 및 관리
##시퀀스 객체 아님 -> []로 참조 불가능
##딕셔너리={키:값, 키:값,...}의 형태, 키에는 변하지 않는 값(문자상수, 숫자상수, 튜플 등 가능), 값에는 변하는 값
##연관 데이터로 저장하기 위한 용도의 자료형

##3-1 빈 딕셔너리 만드는 두 가지 방법
#방법 1
a = {}
print(a)

#방법2
b = dict()
print(b)

## 3-2 딕셔너리 만드는 방법

#방법1
dic1 = {'아이디':'홍길동', '나이':29}
#방법2
dic2 = dict(아이디='홍길동', 나이=29)
#방법3
dic3 = dict(zip(['아이디','나이'],['홍길동',27]))
#방법4
dic4 = dict({'아이디':'홍길동','나이':27})

#네 가지 모두 같은 결과


##3-3 데이터 추가
dic1['add']='seoul'
print(dic1)

##3-4 데이터 삭제: del 딕셔너리변수명[키]
del dic1['add']
print(dic1)
#단 시퀀스가 아니기 때문에 인덱스로 참조 불가능-> 리스트로 변환 후 사용가능
list_d = list(dic2)
print(list_d) # ['아이디', '나이']
print(list_d[0:1]) #['아이디']

##3-5 키,값 추출
print(dic1.keys()) # 키만 추출 (리스트형태)
print(dic1.values()) # 값만 추출 (리스트형태)
print(dic1.items)  #키+값 (리스트 안 튜플형태)


##3-6 딕셔너리 값 추가
dic2['나이']=27
print(dic2)

##3-7 해당 값 추출하기
print(dic3['아이디'])
# 단 없는 키 참조하면 에러

##3-8 해당 키 있는지 확인
# 방법1.
print(dic3.keys())
#방법 2.
print('아이디'in dic3)

##3-9 len() 사용 가능
print(len(dic3)) # 요소(키, 값)길이