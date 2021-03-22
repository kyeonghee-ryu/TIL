# 2. yahoo.finance.com¿¡¼­ ÃÖ±Ù 1³â µ¿¾ÈÀÇ(2020.3.18~2021.3.18) »ï¼ºÀüÀÚ ÁÖ½Ä µ¥ÀÌÅÍ¸¦ 
# ´Ù¿î·Îµå ÈÄ, Á¾°¡¸¦ ¿¹ÃøÇÏ´Â ¸ğµ¨À» ¸¸µå½Ã¿À. (À§ ±â°£À» ´Ù¸£°Ô ¼³Á¤ÇØµµ °ü°è¾ø½À´Ï´Ù)

#1. µ¥ÀÌÅÍ È®ÀÎ & train, test set ºĞ¸®

library(dplyr)
library(ggplot2)


samsung<-read.csv('./data/samsung_elec.csv',header = T)
str(samsung)
nrow(samsung)
summary(samsung)
colnames(samsung)

samsung$Date <- as.Date(samsung$Date)
str(samsung)

# date -> month ÄÃ·³ »ı¼º
samsung$Month <- format(samsung$Date, "%Y-%m")
str(samsung)


library(Amelia)
missmap(samsung,col = c('red','grey'))  # °áÃø°ª ¾øÀ½


samsungTrain<-samsung[samsung$Date<='2021-02-18',]
nrow(samsungTrain) # 228

samsungTest<-samsung[samsung$Date>'2021-02-18',]
nrow(samsungTest) # 19


samsungTrainLabels<-samsung[samsung$Date<='2021-02-18','Close']
samsungTestLabels<-samsung[samsung$Date>'2021-02-18','Close']

#2. µ¥ÀÌÅÍ ºĞ¼®

# 2-1 <ÀüÃ¼ ÁÖ°¡ ºĞ¼®>
install.packages('quantmod')
library(quantmod)
samsungTrainStock<-getSymbols(Symbols = "005930.KS",
                              from= "2020-03-18",
                              to = "2021-02-18",
                              auto.assign = FALSE)
samsungTrainStock
colnames(samsungTrainStock)<-c('open','high','low','close','volume','adjusted') #ÄÃ·³¸í º¯°æ
plot(samsungTrainStock$close) 
chartSeries(samsungTrainStock,up.col = 'red',dn.col='blue',theme='white',name='»ï¼ºÀüÀÚ') 
addBBands() 

#ÁÖ°¡ ÇØ´ç ±â°£µ¿¾È ²ÙÁØÈ÷ »ó½Â
#È¸»ö ±¸°£= º¼¸°Á®¹êµå: °ú¸Åµµ¿Í °ú¸Å¼ö ½ÅÈ£ Æ÷Âø °¡´É
#-ÁÖ°¡°¡ º¼¸°Á®¹êµå ÇÏºÎ¿¡ À§Ä¡ -> Áß½É¼±À¸·Î ´Ù½Ã È¸±ÍÇÒ °Í ¿¹Ãø -> ¸Å¼ö
#-ÁÖ°¡°¡ º¼¸°Á®¹êµå »óºÎ¿¡ À§Ä¡ -> Áß½É¼±À¸·Î ´Ù½Ã È¸±ÍÇÒ °Í ¿¹Ãø -> ¸Åµµ

#2-2 <¼¼ºÎ ÁÖ°¡ ºĞ¼®>

#2-2-1 ÀÏº° ÁÖ°¡ ºĞ¼®

## ÀÏº° Á¾°¡, ÃÖÀú°¡, ÃÖ°í°¡ ½Ã°¢È­
dev.off()
plot(samsungTrain$Date,samsungTrain$Close,type='l',
     main='ÀÏº° Á¾°¡, ÃÖÀú°¡, ÃÖ°í°¡ ºñ±³',
     xlab='ÀÏÀÚ',
     ylab='ÁÖ°¡')
lines(samsungTrain$Date,samsungTrain$High,col='red')
lines(samsungTrain$Date,samsungTrain$Low,col='blue')
legend("topleft",
              legend=c('Á¾°¡','ÃÖ°í°¡','ÃÖÀú°¡'),
              col=c('black','red','blue'),
              pch=c(16,16,16),
              cex=.7)

#ÀüÃ¼ ±â°£ Áß Á¾°¡°¡ ÃÖÀú,ÃÖ´ëÀÎ ³¯

samsungTrain[which.min(samsungTrain$Close),]
#         Date  Open  High   Low Close Adj.Close   Volume   Month
# 4 2020-03-23 42600 43550 42400 42500  40629.57 41701626 2020-03

samsungTrain[which.max(samsungTrain$Close),]
#           Date  Open  High   Low Close Adj.Close   Volume   Month
# 202 2021-01-11 90000 96800 89500 91000     91000 90306177 2021-01

#Á¾°¡ ÃÖÀúÀÎ ³¯ : 2020-03-23
#Á¾°¡ ÃÖ°íÀÎ ³¯ : 2021-01-11


## ÀÏº° Á¾°¡, ½Ã°¡ Â÷ÀÌ

plot(samsungTrain$Date,samsungTrain$Close,type='l',
     xlab='ÀÏÀÚ',
     ylab='ÁÖ°¡',
     main='ÀÏº° ½Ã°¡ Á¾°¡ ºñ±³')
lines(samsungTrain$Date,samsungTrain$Open,col='red')
legend("topleft",
       legend=c('Á¾°¡','½Ã°¡'),
       col=c('black','red'),
       pch=c(16,16))
#µÎ ¼±ÀÇ Â÷ÀÌ°¡ Å¬¼ö·Ï ÇÏ·ç º¯µ¿ÀÌ Å«°Í
#2021³â 1¿ù,2¿ù¿¡ ÇÏ·ç º¯µ¿ ÆøÀÌ Å©´Ù


## ÀÏº° Á¾°¡, ¼öÁ¤Á¾°¡ ºñ±³

plot(samsungTrain$Date,samsungTrain$Close,type='l',
     xlab='ÀÏÀÚ',
     ylab='ÁÖ°¡',
     main='ÀÏº° Á¾°¡, ¼öÁ¤Á¾°¡ ºñ±³')
lines(samsungTrain$Date,samsungTrain$Adj.Close,col='blue')
legend("topleft",
       legend=c('Á¾°¡','¼öÁ¤ Á¾°¡'),
       col=c('black','blue'),
       pch=c(16,16),
       cex=.7)
# Á¾°¡: ½ÃÀåÀÌ ¸¶°¨µÇ±â Àü¿¡ ¸¶Áö¸·À¸·Î °Å·¡µÈ °¡°İÀÇ Çö±İ °¡Ä¡ÀÎ ¿ø½Ã °¡°İ
# ¼öÁ¤ ÁÖ°¡: ±â¾÷ È°µ¿À» °í·ÁÇÑ µÚ ÇØ´ç ÁÖ½ÄÀÇ °¡Ä¡¸¦ ¹İ¿µÇÏ±â À§ÇØ ÁÖ½ÄÀÇ Á¾°¡¸¦ ¼öÁ¤ÇÑ °Í



# 2-2-2 ¿ùº° ÁÖ°¡ ºñ±³

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

#¿ùÆò±Õ Á¾°¡ ÃÖ¼ÒÀÎ ´Ş
month.mean[which.min(month.mean$x),]

#    Month     x
# 1 2020-03 46375

#¿ùÆò±Õ Á¾°¡ ÃÖ´ëÀÎ ´Ş
month.mean[which.max(month.mean$x),]

#     Month     x
# 11 2021-01 86565


plot(as.yearmon(month.mean$Month),month.mean$x,type='o',
     xlab='¿ù',
     ylab='Á¾°¡ Æò±Õ',
     main='¿ùÆò±Õ Á¾°¡')
abline(h=mean(samsungTrain$Close),col='darkgreen')
abline(h=min(month.mean$x),col='red')
abline(h=max(month.mean$x),col='blue')
legend("topleft",
       legend=c('Á¾°¡ Æò±Õ','ÀüÃ¼ Á¾°¡ Æò±Õ','¿ùÆò±Õ ÃÖÀú Á¾°¡','¿ùÆò±Õ ÃÖ°í Á¾°¡'),
       col=c('black','darkgreen','red','blue'),
       pch=c(16,16,16,16),
       cex=.55)


#¿ùº° Á¾°¡ boxplot
ggplot(data = samsungTrain, aes(x = Month, y = Close,color=Month))+
  geom_boxplot(size = 0.7)+
  labs(x='´ÜÀ§: ¿ù', y='Á¾°¡',title='¿ùº° Á¾°¡ ºĞÆ÷')+
  theme(plot.title = element_text(size=15))

#2020³â 3¿ùÀÌÈÄ ¿ùÆò±Õ Á¾°¡ ²ÙÁØÈ÷ »ó½Â 
#Æò±Õº¸´Ù Á¾°¡ ³ôÀº ´Ş : 2020-11¿ù ÀÌÈÄ
#2020-11 º¯µ¿ ÆøÀÌ Å­-> ÁÖ°¡ º¯µ¿ÀÌ ¸¹¾Ò´Ù 
#2020-12 º¯µ¿ÆøÀÌ Á¼Áö¸¸,ÀÌ»óÄ¡ ¸¹ÀÌ Á¸ÀçÇÔ
#2020-12 ¿¡¼­ 2021-01¿¡ ÁÖ°¡ Å©°Ô »ó½ÂÇÔ


# 2-2-3 ºĞ±âº° ÁÖ°¡ ºñ±³

# ºĞ±â ÄÃ·³ »ı¼º
install.packages('lubridate')
library('lubridate')
quarter<-paste(year(samsungTrain$Date),'Q',quarter(samsungTrain$Date),seq='')
samsungTrain<-cbind(samsungTrain,quarter)
str(samsungTrain)
# ºĞ±âº° Á¾°¡ ºĞ¼®
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


#ºĞ±âº° ¼öÁ¤ Á¾°¡ ºĞ¼®
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

#Á¾°¡, ¼öÁ¤Á¾°¡ ¸ğµÎ 2020³â 1ºĞ±â Æò±ÕÀÌ °¡Àå ³·°í, 2021³â 1ºĞ±â Æò±ÕÀÌ °¡Àå ³ô´Ù.


#½Ã°¢È­
ggplot(data = samsungTrain, aes(x =quarter, y = Close,color=quarter))+
  geom_boxplot(size = 0.7)+
  labs(x='´ÜÀ§: ºĞ±â', y='Á¾°¡',title='ºĞ±âº° Á¾°¡ ºĞÆ÷')+
  theme(plot.title = element_text(size=15))

#2020³â 4ºĞ±â Á¾°¡ º¯µ¿ÀÌ ¸Å¿ì Å©´Ù -> ¿øÀÎÀ» Ã£¾Æº¼ ÇÊ¿ä ÀÖÀ½


## 2-2-4 °Å·¡·® ºĞ¼®
par(mfrow=c(1,2))
plot(samsungTrain$Date,samsungTrain$Volume,type='l',
     xlab='¿ù(Month)',
     ylab='°Å·¡·®',
     main='ÀÏº° °Å·¡·®')
plot(samsungTrain$Date,samsungTrain$Close,type='l',
     xlab='¿ù(Month)',
     ylab='Á¾°¡',
     main='ÀÏº° Á¾°¡')

#Á¾°¡°¡ ¿À¸¥ ÈÄ, °Å·¡·®ÀÌ ±ŞÁõÇÏ´Â °ÍÀ» ¾Ë ¼ö ÀÖ´Ù


#3. ´ÙÇ×È¸±Í ¸ğµ¨¸µ

#3-1 º¯¼ö¼±ÅÃ(´Ü°èÀû ¼±ÅÃ¹ı) ¹× ¸ğµ¨¸µ
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
#   Signif. codes:  0 ¡®***¡¯ 0.001 ¡®**¡¯ 0.01 ¡®*¡¯ 0.05 ¡®.¡¯ 0.1 ¡® ¡¯ 1
#¸ğµç È¸±Í °è¼ö°¡ À¯ÀÇÇÏ´Ù

# Residual standard error: 496.9 on 223 degrees of freedom
# Multiple R-squared:  0.9984,	Adjusted R-squared:  0.9984 
# F-statistic: 3.438e+04 on 4 and 223 DF,  p-value: < 2.2e-16

#Á¶Á¤ °áÁ¤ °è¼ö ±²ÀåÈ÷ ³ô´Ù

#3-2 train set Á¤È®µµ Å×½ºÆ®


PredTrain.modelStep<-predict(modelStep,data.frame(samsungTrain[,c('Open','High','Low','Volume')]))

dev.off()

plot(samsungTrain$Date, samsungTrainLabels,type='l',
     main='È¸±Í¸ğµ¨ Train Set Á¤È®µµ ºñ±³',
     xlab='¿ù(Month)',
     ylab='Á¾°¡')
lines(samsungTrain$Date,as.numeric(PredTrain.modelStep),col='red')
legend("topleft",
       legend=c('½ÇÁ¦ Á¾°¡','¿¹Ãø Á¾°¡'),
       col=c('black','red'),
       pch=c(16,16),
       cex=.7)


# 3-3 Test set ¿¹Ãø
PredTest.modelStep<-predict(modelStep,data.frame(samsungTest[,c('Open','High','Low','Volume')]))
dev.off()
plot(as.Date(samsungTest$Date), samsungTestLabels,type='l',
     main='È¸±Í¸ğµ¨ Test set Á¤È®µµ ºñ±³',
     xlab='ÀÏÀÚ',
     ylab='Á¾°¡')
lines(samsungTest$Date,as.numeric(PredTest.modelStep),col='red')
legend("topleft",
       legend=c('½ÇÁ¦ Á¾°¡','¿¹Ãø Á¾°¡'),
       col=c('black','red'),
       pch=c(16,16),
       cex=.7)

#3-4 ºĞ¼® °á°ú

# ÀÜÂ÷ ºĞ¼® °á°ú ºñ±³
modelStepRss<-sum((as.numeric(PredTest.modelStep)-samsungTestLabels)^2)
modelStepRss # 5473548

#°áÁ¤°è¼ö
1-modelStepRss/sum((samsungTestLabels-mean(samsungTestLabels))^2) #0.6819457
# -> ´Ü°èÀû ¼±ÅÃ¹ıÀ¸·Î ±¸ÇÑ È¸±Í ¸ğµ¨ÀÌ ¸ğµ¨ÀÇ ¾à 0.68À» ¼³¸íÇÑ´Ù



#4. Ãß°¡ºĞ¼®
#º¯µ¿ÆøÀÌ Å« 2020³â 11¿ù~ 2020³â 1¿ù 
#»ï¼ºÀü°¡ °ü·Ã ´º½º Á¦¸ñ Å©·Ñ¸µ ÈÄ -> ¸¹ÀÌ »ç¿ëµÈ ´Ü¾î ºĞ¼® -> ÁÖ°¡º¯µ¿¿äÀÎ Ãß·Ğ


library(tm)
library(wordcloud)
newsTitle<-read.csv('./data/newsSamsung.csv',header=T,encoding='UCS-2LE')

str(newsTitle)

newsTitle$Date <- as.Date(newsTitle$Date)
newsTitle$month<- format(newsTitle$Date, "%Y-%m")
unique(newsTitle$month)
rownames(newsTitle)<-c(1:nrow(newsTitle))
newsTitle

# 2020-11 ~ 2021-02 ¿ùº° corpus »ı¼º

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

#ÇÑ±ÛÀÚ Á¦¿Ü
nov20Corpus<-tm_map(nov20Corpus,removeWords,'[°¡-ÆR]{1}')
dec20Corpus<-tm_map(dec20Corpus,removeWords,'[°¡-ÆR]{1}')
jan21Corpus<-tm_map(jan21Corpus,removeWords,'[°¡-ÆR]{1}')
feb21Corpus<-tm_map(feb21Corpus,removeWords,'[°¡-ÆR]{1}')


#wordcloud °á°ú
wordcloud(nov20Corpus,min.freq = 25, random.order=F,colors=brewer.pal(3,'Dark2'))
wordcloud(dec20Corpus,min.freq = 25, random.order=F,colors=brewer.pal(3,'Dark2'))
wordcloud(jan21Corpus,min.freq = 25, random.order=F,colors=brewer.pal(3,'Dark2'))
wordcloud(nov20Corpus,min.freq = 25, random.order=F,colors=brewer.pal(3,'Dark2'))

# -2020³â 12¿ù¿¡ Á¾°¡¿¡¼­ ÀÌ»óÄ¡°¡ ¸¹¾Ò´Âµ¥, ´ç½Ã ±â»ç¿¡¼­ °¡Àå ¸¹ÀÌ ¾ğ±ŞµÈ ´Ü¾î Áß 
# ÄÚ·Î³ª, »ó¼Ó¼¼, ÆÄ±âÈ¯¼Û½É Æ÷ÇÔµÇ¾î ÀÖ´Ù.
# 
# -2020³â 12¿ù¿¡ ºñÇØ 2021³â 1¿ù ÁÖ°¡°¡ ±ŞµîÇß´Ù. ¶ÇÇÑ 2021³â Á¾°¡ º¯µ¿ÆøÀÌ ¸Å¿ì ÄÇ´Ù. 
# 2020³â 12¿ù¿¡´Â ¾ğ±ŞµÇÁö ¾Ê¾ÒÁö¸¸ 2021³â 1¿ù¿¡ ¾ğ±ŞµÈ ´Ü¾î Áß ºóµµ¼ö°¡ ³ôÀº °ÍÀº
# »çÀü¿¹¾à, °¶·°½Ã µîÀÌ ÀÖ´Ù.
# »ï¼ºÀüÀÚÀÇ ½ÅÁ¦Ç° Ãâ½Ã¿¡ ÀÇÇÑ ¿µÇâÀÎÁö´Â Ãß°¡ ºĞ¼®ÀÌ ÇÊ¿äÇØ º¸ÀÎ´Ù
