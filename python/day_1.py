# 1. 기초 연산
print(3//2)  #몫
print(3%2)   #나머지
print(divmod(3,2))   #몫&나머지

# 2. \n, \t
print("machine\n learning") #줄바꿈
print("deep \t learning")   #tap(4번 띄워쓰기)

# 3. sep 구분자
print("My","name","is","ryu",sep=" ")

# 4. end
print("python", end="$")
print("learning")

# 5. x,y=y,x
x=1; y=3
print(x,y)
x,y=y,x
print(x,y)

# 6. del
del x #변수 x삭제

# 7
x=3
x+=4   # -,*,/ 모두 해당
print(x)

# 8. input으로 두가지 값 반환하기
a,b= input("두 수 입력:").split()
print(a,b)

# 9. map함수
x1,x2= map(int,input("두 수 입력:").split())
print(x1+x2)

# 10. 문자형 표현 방법
x = """
I
HAD
DINNER"""

print(x)

#11. 문자열 포맷팅
x="three"
d=2
per=40

print("I ate %s oranges for %d days" %(x,d))
print("%d%%" %per)