# 2. yahoo.finance.com에서 최근 1년 동안의(2020.3.18~2021.3.18) 삼성전자 주식 데이터를 
# 다운로드 후, 종가를 예측하는 모델을 만드시오. (위 기간을 다르게 설정해도 관계없습니다)

#1. 데이터 확인 & train, test set 분리

library(dplyr)
library(ggplot2)


samsung<-read.csv('./data/samsung_elec.csv',header = T)
str(samsung)
nrow(samsung)
summary(samsung)
colnames(samsung)

samsung$Date <- as.Date(samsung$Date)
str(samsung)

# date -> month 컬럼 생성
samsung$Month <- format(samsung$Date, "%Y-%m")
str(samsung)


library(Amelia)
missmap(samsung,col = c('red','grey'))  # 결측값 없음


samsungTrain<-samsung[samsung$Date<='2021-02-18',]
nrow(samsungTrain) # 228

samsungTest<-samsung[samsung$Date>'2021-02-18',]
nrow(samsungTest) # 19


samsungTrainLabels<-samsung[samsung$Date<='2021-02-18','Close']
samsungTestLabels<-samsung[samsung$Date>'2021-02-18','Close']

#2. 데이터 분석

# 2-1 <전체 주가 분석>
install.packages('quantmod')
library(quantmod)
samsungTrainStock<-getSymbols(Symbols = "005930.KS",
                              from= "2020-03-18",
                              to = "2021-02-18",
                              auto.assign = FALSE)
samsungTrainStock
colnames(samsungTrainStock)<-c('open','high','low','close','volume','adjusted') #컬럼명 변경
plot(samsungTrainStock$close) 
chartSeries(samsungTrainStock,up.col = 'red',dn.col='blue',theme='white',name='삼성전자') 
addBBands() 

#주가 해당 기간동안 꾸준히 상승
#회색 구간= 볼린져밴드: 과매도와 과매수 신호 포착 가능
#-주가가 볼린져밴드 하부에 위치 -> 중심선으로 다시 회귀할 것 예측 -> 매수
#-주가가 볼린져밴드 상부에 위치 -> 중심선으로 다시 회귀할 것 예측 -> 매도

#2-2 <세부 주가 분석>

#2-2-1 일별 주가 분석

## 일별 종가, 최저가, 최고가 시각화
dev.off()
plot(samsungTrain$Date,samsungTrain$Close,type='l',
     main='일별 종가, 최저가, 최고가 비교',
     xlab='일자',
     ylab='주가')
lines(samsungTrain$Date,samsungTrain$High,col='red')
lines(samsungTrain$Date,samsungTrain$Low,col='blue')
legend("topleft",
              legend=c('종가','최고가','최저가'),
              col=c('black','red','blue'),
              pch=c(16,16,16),
              cex=.7)

#전체 기간 중 종가가 최저,최대인 날

samsungTrain[which.min(samsungTrain$Close),]
#         Date  Open  High   Low Close Adj.Close   Volume   Month
# 4 2020-03-23 42600 43550 42400 42500  40629.57 41701626 2020-03

samsungTrain[which.max(samsungTrain$Close),]
#           Date  Open  High   Low Close Adj.Close   Volume   Month
# 202 2021-01-11 90000 96800 89500 91000     91000 90306177 2021-01

#종가 최저인 날 : 2020-03-23
#종가 최고인 날 : 2021-01-11


## 일별 종가, 시가 차이

plot(samsungTrain$Date,samsungTrain$Close,type='l',
     xlab='일자',
     ylab='주가',
     main='일별 시가 종가 비교')
lines(samsungTrain$Date,samsungTrain$Open,col='red')
legend("topleft",
       legend=c('종가','시가'),
       col=c('black','red'),
       pch=c(16,16))
#두 선의 차이가 클수록 하루 변동이 큰것
#2021년 1월,2월에 하루 변동 폭이 크다


## 일별 종가, 수정종가 비교

plot(samsungTrain$Date,samsungTrain$Close,type='l',
     xlab='일자',
     ylab='주가',
     main='일별 종가, 수정종가 비교')
lines(samsungTrain$Date,samsungTrain$Adj.Close,col='blue')
legend("topleft",
       legend=c('종가','수정 종가'),
       col=c('black','blue'),
       pch=c(16,16),
       cex=.7)
# 종가: 시장이 마감되기 전에 마지막으로 거래된 가격의 현금 가치인 원시 가격
# 수정 주가: 기업 활동을 고려한 뒤 해당 주식의 가치를 반영하기 위해 주식의 종가를 수정한 것



# 2-2-2 월별 주가 비교

month.mean<-aggregate(samsungTrain$Close,list(Month=samsungTrain$Month), mean)
month.mean
#     Month        x
# 1  2020-03 46375.00
# 2  2020-04 49045.00
# 3  2020-05 49100.00
# 4  2020-06 52986.36
# 5  2020-07 54726.09
# 6  2020-08 56980.00
# 7  2020-09 58176.19
# 8  2020-10 59736.84
# 9  2020-11 63419.05
# 10 2020-12 73619.05
# 11 2021-01 86565.00
# 12 2021-02 83308.33

#월평균 종가 최소인 달
month.mean[which.min(month.mean$x),]

#    Month     x
# 1 2020-03 46375

#월평균 종가 최대인 달
month.mean[which.max(month.mean$x),]

#     Month     x
# 11 2021-01 86565


plot(as.yearmon(month.mean$Month),month.mean$x,type='o',
     xlab='월',
     ylab='종가 평균',
     main='월평균 종가')
abline(h=mean(samsungTrain$Close),col='darkgreen')
abline(h=min(month.mean$x),col='red')
abline(h=max(month.mean$x),col='blue')
legend("topleft",
       legend=c('종가 평균','전체 종가 평균','월평균 최저 종가','월평균 최고 종가'),
       col=c('black','darkgreen','red','blue'),
       pch=c(16,16,16,16),
       cex=.55)


#월별 종가 boxplot
ggplot(data = samsungTrain, aes(x = Month, y = Close,color=Month))+
  geom_boxplot(size = 0.7)+
  labs(x='단위: 월', y='종가',title='월별 종가 분포')+
  theme(plot.title = element_text(size=15))

#2020년 3월이후 월평균 종가 꾸준히 상승 
#평균보다 종가 높은 달 : 2020-11월 이후
#2020-11 변동 폭이 큼-> 주가 변동이 많았다 
#2020-12 변동폭이 좁지만,이상치 많이 존재함
#2020-12 에서 2021-01에 주가 크게 상승함


# 2-2-3 분기별 주가 비교

# 분기 컬럼 생성
install.packages('lubridate')
library('lubridate')
quarter<-paste(year(samsungTrain$Date),'Q',quarter(samsungTrain$Date),seq='')
samsungTrain<-cbind(samsungTrain,quarter)
str(samsungTrain)
# 분기별 종가 분석
quarter.closeMean<-aggregate(samsungTrain$Close,list(Quarter=samsungTrain$quarter), mean)
quarter.closeMean
#    Quarter        x
# 1 2020 Q 1  46375.00
# 2 2020 Q 2  50483.61
# 3 2020 Q 3  56562.50
# 4 2020 Q 4  65783.61
# 5 2021 Q 1  85343.75

quarter.closeMean[which.min(quarter.closeMean$x),]
#     Month     x
# 1 2020 Q 1  46375
quarter.closeMean[which.max(quarter.closeMean$x),]
#   Month        x
# 5 2021 Q 1  85343.7


#분기별 수정 종가 분석
quarter.adjcloseMean<-aggregate(samsungTrain$Adj.Close,list(Month=samsungTrain$quarter), mean)
quarter.adjcloseMean
#    Month        x
# 1 2020 Q 1  44401.51
# 2 2020 Q 2  48629.25
# 3 2020 Q 3  54847.46
# 4 2020 Q 4  64232.80
# 5 2021 Q 1  85343.75

quarter.adjcloseMean[which.min(quarter.adjcloseMean$x),]
#   Month        x
# 1 2020 Q 1  44401.51
quarter.adjcloseMean[which.max(quarter.adjcloseMean$x),]
#   Month        x
# 5 2021 Q 1  85343.75

#종가, 수정종가 모두 2020년 1분기 평균이 가장 낮고, 2021년 1분기 평균이 가장 높다.


#시각화
ggplot(data = samsungTrain, aes(x =quarter, y = Close,color=quarter))+
  geom_boxplot(size = 0.7)+
  labs(x='단위: 분기', y='종가',title='분기별 종가 분포')+
  theme(plot.title = element_text(size=15))

#2020년 4분기 종가 변동이 매우 크다 -> 원인을 찾아볼 필요 있음


## 2-2-4 거래량 분석
par(mfrow=c(1,2))
plot(samsungTrain$Date,samsungTrain$Volume,type='l',
     xlab='월(Month)',
     ylab='거래량',
     main='일별 거래량')
plot(samsungTrain$Date,samsungTrain$Close,type='l',
     xlab='월(Month)',
     ylab='종가',
     main='일별 종가')

#종가가 오른 후, 거래량이 급증하는 것을 알 수 있다


#3. 다항회귀 모델링

#3-1 변수선택(단계적 선택법) 및 모델링
model.step<- lm(Close~Open+High+Low+Volume, data = samsungTrain)
model.step
# Coefficients:
#   (Intercept)         Open         High          Low       Volume  
#      7.834e+02   -6.043e-01    8.393e-01    7.553e-01   -1.293e-05  
modelStep <- step(model.step, direction = "both")
# Start:  AIC=2835.98
# Close ~ Open + High + Low + Volume
# 
# Df Sum of Sq       RSS    AIC
# <none>                 55064082 2836.0
# - Volume  1   1370154  56434236 2839.6
# - Low     1  21361986  76426069 2908.7
# - Open    1  26644205  81708287 2924.0
# - High    1  46084542 101148624 2972.6

summary(modelStep)

# Residuals:
#   Min       1Q   Median       3Q      Max 
# -3067.34  -274.83    15.66   255.99  1991.85 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)  7.834e+02  1.909e+02   4.104 5.71e-05 ***
#   Open        -6.043e-01  5.817e-02 -10.388  < 2e-16 ***
#   High         8.393e-01  6.143e-02  13.661  < 2e-16 ***
#   Low          7.553e-01  8.120e-02   9.301  < 2e-16 ***
#   Volume      -1.293e-05  5.489e-06  -2.356   0.0194 *  
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#모든 회귀 계수가 유의하다

# Residual standard error: 496.9 on 223 degrees of freedom
# Multiple R-squared:  0.9984,	Adjusted R-squared:  0.9984 
# F-statistic: 3.438e+04 on 4 and 223 DF,  p-value: < 2.2e-16

#조정 결정 계수 굉장히 높다

#3-2 train set 정확도 테스트


PredTrain.modelStep<-predict(modelStep,data.frame(samsungTrain[,c('Open','High','Low','Volume')]))

dev.off()

plot(samsungTrain$Date, samsungTrainLabels,type='l',
     main='회귀모델 Train Set 정확도 비교',
     xlab='월(Month)',
     ylab='종가')
lines(samsungTrain$Date,as.numeric(PredTrain.modelStep),col='red')
legend("topleft",
       legend=c('실제 종가','예측 종가'),
       col=c('black','red'),
       pch=c(16,16),
       cex=.7)


# 3-3 Test set 예측
PredTest.modelStep<-predict(modelStep,data.frame(samsungTest[,c('Open','High','Low','Volume')]))
dev.off()
plot(as.Date(samsungTest$Date), samsungTestLabels,type='l',
     main='회귀모델 Test set 정확도 비교',
     xlab='일자',
     ylab='종가')
lines(samsungTest$Date,as.numeric(PredTest.modelStep),col='red')
legend("topleft",
       legend=c('실제 종가','예측 종가'),
       col=c('black','red'),
       pch=c(16,16),
       cex=.7)

#3-4 분석 결과

# 잔차 분석 결과 비교
modelStepRss<-sum((as.numeric(PredTest.modelStep)-samsungTestLabels)^2)
modelStepRss # 5473548

#결정계수
1-modelStepRss/sum((samsungTestLabels-mean(samsungTestLabels))^2) #0.6819457
# -> 단계적 선택법으로 구한 회귀 모델이 모델의 약 0.68을 설명한다



#4. 추가분석
#변동폭이 큰 2020년 11월~ 2020년 1월 
#삼성전가 관련 뉴스 제목 크롤링 후 -> 많이 사용된 단어 분석 -> 주가변동요인 추론


library(tm)
library(wordcloud)
newsTitle<-read.csv('./data/newsSamsung.csv',header=T,encoding='UCS-2LE')

str(newsTitle)

newsTitle$Date <- as.Date(newsTitle$Date)
newsTitle$month<- format(newsTitle$Date, "%Y-%m")
unique(newsTitle$month)
rownames(newsTitle)<-c(1:nrow(newsTitle))
newsTitle

# 2020-11 ~ 2021-02 월별 corpus 생성

nov20<-c()
for(index in as.vector(rownames(newsTitle[newsTitle$month=='2020-11',]))){
  index<-as.numeric(index)
  nov20<-c(nov20,newsTitle[index,'title'])
}


dec20<-c()
for(index in as.vector(rownames(newsTitle[newsTitle$month=='2020-12',]))){
  index<-as.numeric(index)
  dec20<-c(dec20,newsTitle[index,'title'])
}

jan21<-c()
for(index in as.vector(rownames(newsTitle[newsTitle$month=='2021-01',]))){
  index<-as.numeric(index)
  jan21<-c(jan21,newsTitle[index,'title'])
}

feb21<-c()
for(index in as.vector(rownames(newsTitle[newsTitle$month=='2021-02',]))){
  index<-as.numeric(index)
  feb21<-c(feb21,newsTitle[index,'title'])
}

nov20
dec20
jan21
feb21

nov20Corpus<-VCorpus(VectorSource(nov20))
dec20Corpus<-VCorpus(VectorSource(dec20))
jan21Corpus<-VCorpus(VectorSource(jan21))
feb21Corpus<-VCorpus(VectorSource(feb21))

#한글자 제외
nov20Corpus<-tm_map(nov20Corpus,removeWords,'[가-힣]{1}')
dec20Corpus<-tm_map(dec20Corpus,removeWords,'[가-힣]{1}')
jan21Corpus<-tm_map(jan21Corpus,removeWords,'[가-힣]{1}')
feb21Corpus<-tm_map(feb21Corpus,removeWords,'[가-힣]{1}')


#wordcloud 결과
wordcloud(nov20Corpus,min.freq = 25, random.order=F,colors=brewer.pal(3,'Dark2'))
wordcloud(dec20Corpus,min.freq = 25, random.order=F,colors=brewer.pal(3,'Dark2'))
wordcloud(jan21Corpus,min.freq = 25, random.order=F,colors=brewer.pal(3,'Dark2'))
wordcloud(nov20Corpus,min.freq = 25, random.order=F,colors=brewer.pal(3,'Dark2'))

# -2020년 12월에 종가에서 이상치가 많았는데, 당시 기사에서 가장 많이 언급된 단어 중 
# 코로나, 상속세, 파기환송심 포함되어 있다.
# 
# -2020년 12월에 비해 2021년 1월 주가가 급등했다. 또한 2021년 종가 변동폭이 매우 컸다. 
# 2020년 12월에는 언급되지 않았지만 2021년 1월에 언급된 단어 중 빈도수가 높은 것은
# 사전예약, 갤럭시 등이 있다.
# 삼성전자의 신제품 출시에 의한 영향인지는 추가 분석이 필요해 보인다
