##1. boolean 연산자
#1) 비교연산자: (>,<,==)-> 결과: boolean타입
print(3>2)
print(3==2)

#2) is연산자 (==와 다름)
print(1 == 1.0) # True
print(1 is 1.0) # False

#3) 논리연산 ( 논리연산자: and, or, not)
print(1==1 and False)
print(bool('' or "srt"))

##2. 정렬
print("%10s"% "hi") #hi포함 10글자, 앞이 blank
print("%-10s"% "hi") # 위와 같지만 뒤가 blank
print("%.4f" % 3.142592) #소수 넷째자리까지
print("%10.4f" % 3.141592) #10글자 + 소수 넷째자리까지

##3.format()
#방법1. % formatting
day="three"
num=4
print("I ate %d eggs, so I was sick for %s days" %(num, day))

#방법2. .format
print("I ate {0} eggs, so I was sick for {1} days".format(3,"three"))
print("I ate {0} eggs, so I was sick for {1} days".format(day,num))

##4.count() : 특정 문자열 개수를 셀 수 있다.
a = "hello"
print(a.count('l'))

##5. find() : 위치 확인
print(a.find('l')) # 왼쪽부터  처음등장하는 위치 알려줌
#index()함수: 위치 확인(인덱스)
print(a.index('l')) #find와 같은 기능
#차이점:포함되지 않는 문자열 위치를 확인했을때 find는 -1, index는 에러

##6. join() : 문자열 삽입 시 이용
print(",".join('abcd'))
print(' '.join(['a','b']))

##7. 대/소문자 변환
a='abcd'
print(a.upper())
b='CDF'
print(b.lower())

##8. strip() : 공백제거
str = '., python,.'
print(str.lstrip(" .,"))
print(str.rstrip(",."))
print(str.strip(",. "))


##9. replace() : 문자열 치환
s = "Life is too short"
print(s.replace("Life", 'life'))

##10. split() : ()기준으로 분리
print(s.split())
sr = "too#early"
print(sr.split("#"))

##11. maketrans
t = str.maketrans('aeiou', '12345')
print('apple'.translate(t))

import string
print(str.strip(string.punctuation))
print(str.strip(string.punctuation+" "))

##12. 정렬 관련 함수 just()
str="hi"
print(str.rjust(10))
print(str.ljust(10))
print(str.center(10))
print(str.center(0))

##13. method chaining -> 코드 간결해짐
print('python'.rjust(10).upper())


#14. padding : 특정 값으로 자리채움
print("hello".zfill(10))