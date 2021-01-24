<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script>
// 1. 배열 (Array)
//크기와 타입이 동일한 기억장소를 여러개 나열한 것 & 여러개의 값 저장소 , 파이썬의 리스트와 비슷

//1-1 선언방법

/// 방법 1.
var myarr = [];


/// 방법 2.
var myarr=[1,3,5,7] ;

/// 방법 3.
var myarr = new Array(2,4,6,8);

//1-2 배열 길이 확인
document.write(myarr.length);


//1-3 배열 데이터 추가 & 삭제
myarr.push(5); //맨 마지막에 추가
myarr.unshift(99); // 맨 앞에 추가

myarr.pop(); // 맨 마지막 데이터 삭제
myarr.shift() ;// 맨 앞 데이터 삭제


//1-4 정렬 함수
var fruits = ['apple','orange','banana'];
fruits.sort();  //오름차순 정렬
fruits.reverse();  // 오름차순 후 reverse -> 내림차순 정렬

//1-5 인덱스로 추출
document.write(myarr.indexOf(2)); // 값 2에 해당하는  인덱스 추출



//2. 함수

//예시 1
function numbering(){
var i=0;
while(i<5){
for(var j=0;j<10;j++){
document.write(j);
}
document.write("<br/>")
i++;
}
}
numbering()

//예시 2
function blue(){
           for(var i=0;i<10;i++){
        for(var j=0;j<10;j++){
            document.write("<font color='blue'>"+i+j+"</font>"+"<p>");
            }
        }
                 }
blue();


//3. 클래스, 객체
//3-1 객체 생성 방법
/// 방법 1.
var hgd={};
hgd['name']='honggildong';
hgd['age']=28;
hgd['gender']='m';


/// 방법 2.
var hgd={
'name':'honggildong',
'age':28,
'gender':'m'
};
document.write(hgd['name']);


/// 방법 3.
var hgd = new Object();
hgd['name']='honggildong';
hgd['age']=28;
hgd['gender']='m';



//3-2 객체 데이터 접근(추가 방법)

/// 방법 1. []
hgd['birth']='04-27';

/// 방법 2. .
hgd.birth = '04-27';


    </script>
</head>
<body>

</body>
</html>