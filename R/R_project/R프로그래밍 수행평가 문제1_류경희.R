# 1차 문제
# 1. mtcars 데이터를 불러온 후,
# - 전체 32개의 관측치 중 25개를 train, 7개를 test 데이터로 나누어 작업
# - mpg를 종속변수로 두고 다양한 회귀 모델 작성


#분석방법: 전진선택법, 단계적 선택법으로 두 가지 모델 선정 후 결과 비교

#1. 데이터 확인 및 train,test set 분할
library(ggplot2)

data(mtcars)
str(mtcars)
summary(mtcars)
nrow(mtcars)

library(Amelia)
missmap(mtcars,col = c('red','grey'))  # 결측값 없음

set.seed(1)
index<-sample(1:32,25,replace = F)
mtcarsTrain<-mtcars[index,]
mtcarsTest<-mtcars[-index,]

mtcarsTrainLabels <-mtcars[index,'mpg']
mtcarsTestLabels <-mtcars[-index,'mpg']


#2. 데이터 분석

#2-1 mpg와 상관계수 파악
#install.packages('corrplot')
library(corrplot)
mtcor <- cor(mtcarsTrain)
mtcor<-round(mtcor, 2)
mtcor[,1]
# mpg   cyl  disp    hp  drat    wt  qsec    vs    am  gear  carb 
# 1.00 -0.84 -0.84 -0.83  0.68 -0.89  0.38  0.65  0.66  0.53 -0.60 


corrplot(mtcor, method='shade', shade.col=NA, tl.col='black', tl.srt=45)

## >> 음의 상관관계인변수 : cyl,disp,hp,wt,carb
## >> 양의 상관관계인 변수: drat,qsec,vs,am,gear


#2-2 변수별 분석
dev.off()

#cyl
plot(as.factor(mtcarsTrain$cyl),mtcarsTrain$mpg,
     main='mpg 와 cyl 상관관계')
abline(h=mean(mtcarsTrain$mpg))
# cyl 이 4>6>8 순으로 mpg가 높다.


#disp
plot(mtcarsTrain$disp,mtcarsTrain$mpg,
     col=c('red','blue','darkgreen')[as.factor(mtcarsTrain$cyl)],
     pch=c(16,17,18)[as.factor(mtcarsTrain$cyl)],
     main='mpg 와 disp 상관관계')
abline(lm(mpg~disp,mtcarsTrain))

legend(300,30,
       legend=c('cyl=4','cyl=6','cyl=8'),
       col=c('red','blue','darkgreen'),
       pch=c(16,17,18))

#hp
plot(mtcarsTrain$hp,mtcarsTrain$mpg,
     main='mpg 와 hp 상관관계')
abline(lm(mpg~hp,mtcarsTrain))

#wt
plot(mtcarsTrain$wt,mtcarsTrain$mpg,
     main='mpg 와 wt 상관관계')
abline(lm(mpg~wt,mtcarsTrain))



#3. modeling-전진선택법

#3-1 model1  : wt
# 가장 상관계수가 높은 wt 변수 하나를 가지고 회귀분석 실시
model1 <-lm(mpg~wt,mtcarsTrain)
model1

# Coefficients:
#   (Intercept)        wt  
#      38.912       -5.875  

summary(model1)

# Residuals:
#   Min      1Q  Median      3Q     Max 
# -4.4891 -2.5202 -0.0029  1.3982  6.4124 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)  38.9122     2.0426  19.051 1.39e-15 ***
#   wt           -5.8748     0.6148  -9.555 1.79e-09 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# ->회귀계수 모두 유의함

# Residual standard error: 2.91 on 23 degrees of freedom
# Multiple R-squared:  0.7988,	Adjusted R-squared:   0.79 
# F-statistic:  91.3 on 1 and 23 DF,  p-value: 1.791e-09
# -> 조정된 결정계수 0.79 -> 1에 가깝다 -> 통계적으로 유의하다고 볼 수 있음
# -> p-value < 0.05 -> 유의미한 결과

#3-2 model2 : wt + cyl

model2 <-lm(mpg~wt+cyl,mtcarsTrain)
model2
# Coefficients:
# (Intercept)    wt       cyl  
#    40.977    -4.002    -1.287  
summary(model2)

# Residuals:
#   Min     1Q Median     3Q    Max 
# -4.466 -1.772 -0.356  1.423  5.413 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)  40.9772     2.0009  20.479 8.12e-16 ***
#   wt           -4.0015     0.9147  -4.375 0.000242 ***
#   cyl          -1.2869     0.5014  -2.567 0.017588 *  
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# -> 회귀 계수 모두 유의미함 

# Residual standard error: 2.61 on 22 degrees of freedom
# Multiple R-squared:  0.8452,	Adjusted R-squared:  0.8311 
# F-statistic: 60.04 on 2 and 22 DF,  p-value: 1.227e-09

# ->결정계수 model 1보다 높음
# -> p-value < 0.05 이므로 유의미한 모델



#3-3 model3 :wt + cyl + disp
model3 <-lm(mpg~wt+cyl+disp,mtcarsTrain)
model3
summary(model3)

# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 42.142938   3.110846  13.547 7.54e-12 ***
#   wt          -4.347172   1.163103  -3.738  0.00121 ** 
#   cyl         -1.521754   0.696232  -2.186  0.04031 *  
#   disp         0.006072   0.012251   0.496  0.62530    
# ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# -> disp 회귀계수 > 0.05 이므로 통계적으로 유의하지 않다 

# Residual standard error: 2.656 on 21 degrees of freedom
# Multiple R-squared:  0.8469,	Adjusted R-squared:  0.8251 
# F-statistic: 38.74 on 3 and 21 DF,  p-value: 9.69e-09

## -> 조정된 결정계수도 model2 가 더 높다 -> model 2선택



# 4.modeling- 단계적 선택법

model.step<- lm(mpg~., data = mtcarsTrain)
model.step


# Coefficients:
#   (Intercept)          cyl         disp           hp         drat           wt         qsec  
# 19.893129     0.616178     0.007371    -0.027480    -0.921551    -3.949660     0.676159  
# vs           am         gear         carb  
# 1.540558     3.888045     0.719783    -0.747669  

res <- step(model.step, direction = "both")

# Start:  AIC=50.53
# mpg ~ cyl + disp + hp + drat + wt + qsec + vs + am + gear + carb
# 
# Df Sum of Sq     RSS    AIC
# - disp  1    1.1196  79.374 48.882
# - gear  1    1.4513  79.706 48.987
# - drat  1    1.5888  79.843 49.030
# - cyl   1    2.1386  80.393 49.201
# - vs    1    3.3511  81.605 49.575
# - carb  1    4.3724  82.627 49.886
# - qsec  1    4.5058  82.760 49.927
# <none>               78.254 50.527
# - hp    1    7.6142  85.868 50.849
# - am    1   16.4388  94.693 53.294
# - wt    1   22.1810 100.435 54.766
# 
# Step:  AIC=48.88
# mpg ~ cyl + hp + drat + wt + qsec + vs + am + gear + carb
# 
# Df Sum of Sq     RSS    AIC
# - drat  1     1.399  80.773 47.319
# - gear  1     1.559  80.933 47.369
# - cyl   1     3.095  82.469 47.839
# - vs    1     3.189  82.563 47.867
# - qsec  1     3.598  82.971 47.990
# - hp    1     6.540  85.914 48.862
# <none>               79.374 48.882
# + disp  1     1.120  78.254 50.527
# - carb  1    13.993  93.367 50.942
# - am    1    17.019  96.393 51.739
# - wt    1    33.215 112.588 55.622
# 
# Step:  AIC=47.32
# mpg ~ cyl + hp + wt + qsec + vs + am + gear + carb
# 
# Df Sum of Sq     RSS    AIC
# - gear  1     1.257  82.030 45.705
# - vs    1     2.613  83.386 46.115
# - qsec  1     3.585  84.358 46.405
# - cyl   1     3.821  84.594 46.475
# <none>               80.773 47.319
# - hp    1     6.741  87.514 47.323
# + drat  1     1.399  79.374 48.882
# + disp  1     0.930  79.843 49.030
# - am    1    15.704  96.477 49.761
# - carb  1    16.076  96.849 49.857
# - wt    1    31.822 112.595 53.623
# 
# Step:  AIC=45.71
# mpg ~ cyl + hp + wt + qsec + vs + am + carb
# 
# Df Sum of Sq     RSS    AIC
# - cyl   1     2.873  84.903 44.566
# - vs    1     2.896  84.926 44.573
# - qsec  1     3.610  85.640 44.782
# - hp    1     5.692  87.723 45.383
# <none>               82.030 45.705
# + gear  1     1.257  80.773 47.319
# + drat  1     1.097  80.933 47.369
# + disp  1     1.038  80.992 47.387
# - carb  1    15.696  97.726 48.082
# - am    1    24.497 106.527 50.238
# - wt    1    36.328 118.358 52.871
# 
# Step:  AIC=44.57
# mpg ~ hp + wt + qsec + vs + am + carb
# 
# Df Sum of Sq     RSS    AIC
# - vs    1     1.234  86.137 42.927
# - qsec  1     1.710  86.613 43.064
# - hp    1     4.248  89.152 43.787
# <none>               84.903 44.566
# + cyl   1     2.873  82.030 45.705
# + disp  1     1.873  83.031 46.008
# + drat  1     1.815  83.089 46.026
# + gear  1     0.310  84.594 46.475
# - carb  1    18.994 103.897 47.613
# - am    1    22.702 107.606 48.490
# - wt    1    34.011 118.914 50.988
# 
# Step:  AIC=42.93
# mpg ~ hp + wt + qsec + am + carb
# 
# Df Sum of Sq     RSS    AIC
# - hp    1     3.913  90.050 42.037
# - qsec  1     5.664  91.801 42.519
# <none>               86.137 42.927
# + disp  1     1.479  84.658 44.494
# + vs    1     1.234  84.903 44.566
# + cyl   1     1.211  84.926 44.573
# + drat  1     1.031  85.106 44.626
# + gear  1     0.596  85.541 44.753
# - carb  1    18.060 104.197 45.685
# - am    1    22.063 108.201 46.628
# - wt    1    51.531 137.668 52.649
# 
# Step:  AIC=42.04
# mpg ~ wt + qsec + am + carb
# 
# Df Sum of Sq     RSS    AIC
# <none>               90.050 42.037
# + hp    1     3.913  86.137 42.927
# + drat  1     1.203  88.847 43.701
# + vs    1     0.898  89.152 43.787
# + cyl   1     0.549  89.501 43.884
# + gear  1     0.122  89.928 44.003
# + disp  1     0.004  90.046 44.036
# - carb  1    19.064 109.114 44.838
# - am    1    31.404 121.454 47.517
# - qsec  1    34.918 124.968 48.229
# - wt    1    91.758 181.808 57.602
res
# Call:
#   lm(formula = mpg ~ hp + wt + vs + am, data = mtcarsTrain)
# 
# Coefficients:
# (Intercept)           hp           wt           vs           am  
#      27.24730     -0.03187     -1.72819      3.17699      4.21165  

summary(res)

# Call:
#   lm(formula = mpg ~ hp + wt + vs + am, data = mtcarsTrain)

# Residuals:
#   Min      1Q  Median      3Q     Max 
# -4.8625 -1.3944  0.2124  1.1397  4.5069 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 27.24730    3.74234   7.281 4.84e-07 ***
#   hp          -0.03187    0.01109  -2.873   0.0094 ** 
#   wt          -1.72819    0.95340  -1.813   0.0849 .  
# vs           3.17699    1.56202   2.034   0.0554 .  
# am           4.21165    1.54435   2.727   0.0130 *  
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 

# Residual standard error: 2.422 on 20 degrees of freedom
# Multiple R-squared:  0.8939,	Adjusted R-squared:  0.8727 
# F-statistic: 42.13 on 4 and 20 DF,  p-value: 1.795e-09

# -> 조정된 결정계수가 전진선택법보다 높게 나왔다.



#5. 두 모델의 train set 예측 결과 비교

#전진선택법 모델

PredTrain.model2<-predict(model2,data.frame(mtcarsTrain[,c('wt','cyl')]))
PredTrain.model2<-as.numeric(PredTrain.model2)

PredTrain.modelStep<-predict(res,data.frame(mtcarsTrain[,c('wt','qsec','am','carb')]))
PredTrain.modelStep<-as.numeric(PredTrain.modelStep)


dev.off()
plot(mtcarsTrain$mpg,type='l',
     main='전진선택법, 단계적 선택법 train set 예측 결과 비교')
lines(PredTrain.model2,col='red')
lines(PredTrain.modelStep,col='blue')


legend("topright",
       legend=c('전진선택법','단계적전택법'),
       col=c('red','blue'),
       pch=c(16,16),
       cex=.7)

#-> train set에서 단계적 선택법 모델이 좀 더 예측을 잘한다는 것을 알 수 있음


#6. Test set 예측 및 정확도 평가

#6-1 Test set 예측

#전진선택법 
PredTest.model2<-predict(model2,data.frame(mtcarsTest[,c('wt','cyl')]))

#단계적 선택법
PredTest.modelStep<-predict(res,data.frame(mtcarsTest[,c('wt','qsec','am','carb')]))

#6-2 정확도 평가

#시각화 결과 비교
dev.off()
plot(mtcarsTestLabels,type='l',
     main='전진선택법, 단계적 선택법 test set 예측 결과 비교')
lines(as.numeric(PredTest.model2),col='red')
lines(as.numeric(PredTest.modelStep),col='blue')


legend("topright",
       legend=c('전진선택법','단계적선택법'),
       col=c('red','blue'),
       pch=c(16,16),
       cex=.7)

# 그래프로 봤을 때, test set에서는 전진 선택법이 더 예측을 잘 하는 것으로 보인다


# 잔차 분석 결과 비교
model2Rss<-sum((mtcarsTestLabels-as.numeric(PredTest.model2))^2)
model2Rss # 50.53165

modelStepRss<-sum((mtcarsTestLabels-as.numeric(PredTest.modelStep))^2)
modelStepRss # 92.25231

# -> 전진선택법 model2(wt + cyl)이 단계적선택법 모델보다 RSS 가 더 작다 
# -> 전진 선택법 모델이 더 적합한 모델이라고 할 수 있다.


