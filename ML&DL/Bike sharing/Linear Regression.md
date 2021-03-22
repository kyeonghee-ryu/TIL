# Linear Regression

### 1. 정의

-데이터를 가장 잘 설명하는 식 y=ax+b 찾기 (최적의 a,b 찾기)

### 2. MSE

-error: 실제값과 회귀선 (y = a hat + b hat)값의 차이

-error를 최소화하는 선형회귀식을 찾는 것이 목적

-최소화 방법은? MSE(mean square error)

-MSE: 오차의 제곱을 평균 낸 값

-MES가 가장 작은 값을 가질 때, a,b는 최적의 값을 가짐



### 3. Linear Regression Model

H(x) = Wx + b 

H(x) :**가설(Hypothesis)** 

-**W( Weight)**, **b(bias)** 의 값에 따라 선의 모양이 달라짐

-H(x) = Wx + b 이 각 데이터의 분포와의 차이를 계산하여 가장 적은 것이 이 모델에 적합한 선이다

-이를 **비용함수(Cost Function)** 라고 부른다.

-MSE -> 실제로 더 차이가 큰 값에는 더 큰 패널티를 줄 수 있도록 이러한 가중치를 자동적으로 부여함

-비용함수에 대한 식

![img](https://t1.daumcdn.net/cfile/tistory/2178CA335914A02B01)



결과적으로, 이 **회귀 분석(Linear Regression)**을 통하여 그래프 상에서 선을 그렸을 때 **W(가중치)** 값과 미세하게 조절되는 **b(바이어스)**의 값을 찾아 가설과 실제 데이터의 차가 가장 작은 은 최소값을 찾는 것이 머신러닝에서의 선형 회귀(Linear Regression)의 학습이라고 볼 수있다.



### 4. sklearn Linear Regession modeling

-참조:https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html



```
>>> import numpy as np
>>> from sklearn.linear_model import LinearRegression
>>> X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
>>> # y = 1 * x_0 + 2 * x_1 + 3 #x1,x2다항식
>>> y = np.dot(X, np.array([1, 2])) + 3
>>> reg = LinearRegression().fit(X, y) #Fit linear model
>>> reg.score(X, y) #예측값의 결정계수 리턴(선형식이 설명가능한 부분의 비율)
1.0
>>> reg.coef_  # a
array([1., 2.])
>>> reg.intercept_ # b
3.0000...
>>> reg.predict(np.array([[3, 5]]))  #위의 선형식에서 a =3, b=5일때
array([16.])
```