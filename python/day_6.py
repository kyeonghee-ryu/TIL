# #1.파일 입출력
# ##입출력 종류: 표준,파일, 네트워크
# ##그 중 파일 입출력: open -> read/write-> close
#
# ##1-1 파일에 문자열 쓰기/읽기
# #방법1
# #(쓰기)
# f=open('hello.txt','w')
# f.write('hello world')
# f.close()
#
# #(읽기)
# f=open('hello.txt','r')
# s = f.read()
# print(s)
# f.close()
#
# #방법 2 : with as 구문(파일 사용한 뒤 자동으로 닫아줌)
# with open('hello.txt','w')as f:
#     for i in range(10):
#         f.write('hello world{0}\n'.format(i+1))

##1-2 리스트 내용을 파일에 출력
li = ['hello\n','nice\n','meet\n']
# with open('hello.txt','w') as f:
#     f.write(li)    #문법 오류! w모드는 str만 입력 가능

# 리스트 내용 출력할 때 : writelines()
with open('hello.txt','w') as f:
    f.writelines(li)

##1-3 readline(): 파일을 한줄 씩 읽음
with open('hello.txt','r') as f:
    s=f.readline()
    print(s) #hello (첫줄만 읽는다)

#여러줄 읽으려면? for, while과 함께 사용
with open('hello.txt','r') as f:
    line = f.readlines()
    for i in line:
        print(i.strip('\n'))

#2. 피클(pickle): 파이썬 객체를 파일로 저장하고자 하는 경우에 사용되는 모듈
#피클링: 객체 -> 파일
#언피클링: 파일->객체

##2-1 객체 파일로 저장하기 (피클 모듈 사용)
import pickle
내용='단팥'
색상='파랑'
너비='20cm'
가족명단={'잉어':30, '붕어':20}

#객체 저장은 wb
with open('myfish.p','wb') as f:
    pickle.dump(내용,f)
    pickle.dump (색상,f )
    pickle.dump (너비,f )
    pickle.dump (가족명단,f )


#3. class

#예시) 마트 계산대
res1=0
res2=0
def add1(n):
    global res1
    res1+=n
    return res1

def add2(n):
    global res2
    res2+=n
    return res2

print(add1(300))
print(add1(200))

print(add2(200))
print(add2(200))

#계산대 n개이면 함수 n개 작성해야함 -> 비효율적

#해결방법: class 사용

class Calculator:
    def __init__(self):
        self.res=0
        print('init 함수 호출됨')
    def add(self,n):
        self.res+=n
        return self.res


cal1=Calculator()
cal2=Calculator()

print(cal1.add(3000))
print(cal2.add(2000))



#3. 다른 파이썬 파일 함수 사용

def madd(a,b):
    return a+b
def msub(a,b):
    return a-b

if __name__=="__main__":
    print('__name값__',__name__)
    print(madd(3,2))
    print(msub(3,2))


# <다른 파일에서 불러오기>

import day_6 as d
print(d.madd(3,4))

