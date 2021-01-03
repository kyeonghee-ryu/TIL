#!/usr/bin/env python
# coding: utf-8

# # titinic
# 
# #### reference: https://www.kaggle.com/startupsci/titanic-data-science-solutions

# In[1]:


# data analyzis and wrangling

import pandas as pd
import numpy as np
import random as rnd


# In[2]:


#visualization
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#machin learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


# In[4]:


#데이터 불러오기
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
combine = [train_df, test_df]


# In[5]:


combine


# In[6]:


train_df


# In[7]:


test_df


# In[8]:


#column 확인
print(train_df.columns.values)


# In[9]:


train_df.head()


# In[10]:


train_df.info()  #cabin, age, embarked 결측값 존재


# In[11]:


test_df.info() #cabin, age, fare 결측값 존재


# In[12]:


train_df.describe() #train set에서 생존률 38%


# In[13]:


train_df.describe(include=['O']) #범주형 컬럼만 describe


# In[14]:


train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)


# In[15]:


train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False) #성별차이 유의미해보임


# In[16]:


train_df[["SibSp", "Survived"]].groupby(['SibSp'], as_index=False).mean().sort_values(by='Survived', ascending=False)


# In[17]:


train_df[["Parch", "Survived"]].groupby(['Parch'], as_index=False).mean().sort_values(by='Survived', ascending=False)


# # 시각화

# In[19]:


#성별에 따른 생존률
g = sns.FacetGrid(train_df, col='Survived')
g.map(plt.hist, 'Age', bins=20)


# In[20]:


#Age, P-class에 따른 생존률
grid = sns.FacetGrid(train_df, col='Survived', row='Pclass', size=2.2, aspect=1.6)
grid.map(plt.hist, 'Age', alpha=.5, bins=20)
grid.add_legend();


# In[21]:


#Embarked,Pclass,Sex 와 생존률
grid = sns.FacetGrid(train_df, row='Embarked', size=2.2, aspect=1.6)
grid.map(sns.pointplot, 'Pclass', 'Survived', 'Sex', palette='deep')
grid.add_legend()


# In[22]:


grid = sns.FacetGrid(train_df, row='Embarked', col='Survived', size=2.2, aspect=1.6)
grid.map(sns.barplot, 'Sex', 'Fare', alpha=.5, ci=None)
grid.add_legend()


# # Feature engineering

# In[23]:


print("Before", train_df.shape, combine[0].shape,combine[1].shape)


# ## 1. 무의미한 column 삭제

# In[24]:


#무의미한 column 삭제
train_df = train_df.drop(['Ticket', 'Cabin'], axis=1)
test_df = test_df.drop(['Ticket', 'Cabin'], axis=1)
combine = [train_df, test_df]


# In[25]:


print("After", train_df.shape, combine[0].shape, combine[1].shape)


# ## 2 . Name 컬럼에 존재하는 title 분류

# In[26]:


for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand = False)


# In[27]:


pd.crosstab(train_df['Title'], train_df['Sex'])


# In[28]:


for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess', 'Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Title'] = dataset['Title'].replace('Mlle','Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')

train_df[['Title', 'Survived']].groupby('Title', as_index=False).mean()


# ### -분류한 TItle을 숫자 범주로 변환

# In[29]:


title_mapping = {'Mr':1, "Miss":2, "Mrs":3, "Master": 4, "Rare": 5}
for dataset in combine:
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)   #결측값은 0으로 채우기
    
train_df.head()


# ### -train set과 test set에서 Name 삭제 가능, train_set에 PassengerID 무의미해보이니 삭제

# In[30]:


train_df = train_df.drop(['Name', 'PassengerId'], axis=1)
test_df = test_df.drop('Name', axis=1)
combine = [train_df, test_df]
train_df.shape, test_df.shape


# In[31]:


train_df.shape, test_df.shape


# ## 3. 범주형 데이터(성별) 변환

# In[32]:


for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map({'female':1, 'male':0}).astype(int)
    
train_df.head()


# ### -성별, PCLASS, AGE 상관관계를 통해 결측값 채우기

# In[33]:


grid = sns.FacetGrid(train_df, row='Pclass', col='Sex', size = 2.2, aspect=1.6)
grid.map(plt.hist, 'Age', alpha=.5, bins=20)
grid.add_legend()


# In[34]:


guess_ages = np.zeros((2,3))
guess_ages


# In[35]:


for dataset in combine:
    for i in range(0, 2):
        for j in range(0, 3):
            guess_df = dataset[(dataset['Sex'] == i) &                                   (dataset['Pclass'] == j+1)]['Age'].dropna()

            # age_mean = guess_df.mean()
            # age_std = guess_df.std()
            # age_guess = rnd.uniform(age_mean - age_std, age_mean + age_std)

            age_guess = guess_df.median()

            # Convert random age float to nearest .5 age
            guess_ages[i,j] = int( age_guess/0.5 + 0.5 ) * 0.5
            
    for i in range(0, 2):
        for j in range(0, 3):
             dataset.loc[ (dataset.Age.isnull()) & (dataset.Sex == i) & (dataset.Pclass == j+1),'Age'] = guess_ages[i,j]

    dataset['Age'] = dataset['Age'].astype(int)

train_df.head()


# In[36]:


train_df['AgeBand']=pd.cut(train_df['Age'],5) #Age를 5개의 동일한 길이로 나눔
train_df[['AgeBand','Survived']].groupby(['AgeBand'],as_index=False).mean().sort_values(by='AgeBand', ascending=True)


# In[37]:


for dataset in combine:
    dataset.loc[dataset['Age']<=16, 'Age']=0
    dataset.loc[(dataset['Age']>16)&(dataset['Age']<=32),'Age']=1
    dataset.loc[(dataset['Age']>32)&(dataset['Age']<=48),'Age']=2
    dataset.loc[(dataset['Age']>48)&(dataset['Age']<=64),'Age']=3
    dataset.loc[dataset['Age']>64,'Age']=4
train_df.head()


# In[38]:


train_df = train_df.drop(['AgeBand'], axis=1)
combine=[train_df, test_df]
train_df.head()


# ## 4. Parch+SibSp = Family Size

# In[39]:


for dataset in combine:
    dataset['FamilySize']=dataset['SibSp']+dataset['Parch']+1  #가족, 형제자매 없을 떄 1인가구 =1명이기때문에 1을 더함

train_df[['FamilySize','Survived']].groupby(['FamilySize'],as_index=False).mean().sort_values(by='Survived',ascending=False)


# ### -혼자 온 사람들을 분류해보자

# In[40]:


for dataset in combine:
    dataset['IsAlone']=0
    dataset.loc[dataset['FamilySize']==1, 'IsAlone']=1

train_df[['IsAlone','Survived']].groupby(['IsAlone'], as_index=False).mean()    

#혼자면 생존률 0.30


# ### -혼자인 사람을 분류했으니 Parch, Sibsp, FamilySize 컬럼 삭제 (그래도 되는지 잘 모르겠음,,)

# In[41]:


train_df = train_df.drop(['Parch', 'SibSp', 'FamilySize'], axis=1)
test_df = test_df.drop(['Parch', 'SibSp', 'FamilySize'], axis=1)
combine = [train_df, test_df]

train_df.head()


# ## 5. Age*Pclass = Age*Class 컬럼 생성

# In[42]:


for dataset in combine:
    dataset['Age*Class'] = dataset.Age * dataset.Pclass

train_df.loc[:, ['Age*Class', 'Age', 'Pclass']].head(10)


# ## 6. Embarked 결측값 채우기 + 숫자로 변환

# In[43]:


freq_port = train_df.Embarked.dropna().mode()[0]
freq_port


# In[44]:


for dataset in combine:
    dataset['Embarked'] = dataset['Embarked'].fillna(freq_port)
    
train_df[['Embarked', 'Survived']].groupby(['Embarked'], as_index=False).mean().sort_values(by='Survived', ascending=False)


# In[45]:


for dataset in combine:
    dataset['Embarked'] = dataset['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).astype(int)

train_df.head()


# ## 7. Fare 범주화 + test set의 결측값 채우기

# In[46]:


test_df['Fare'].fillna(test_df['Fare'].dropna().median(), inplace=True)
test_df.head()


# In[47]:


train_df['FareBand'] = pd.qcut(train_df['Fare'], 4)  #4개의 범주 생성 ()
train_df[['FareBand', 'Survived']].groupby(['FareBand'], as_index=False).mean().sort_values(by='FareBand', ascending=True)


# In[48]:


for dataset in combine:
    dataset.loc[dataset['Fare']<=7.91, 'Fare']=0
    dataset.loc[(dataset['Fare']>7.91)&(dataset['Fare']<=14.454),'Fare']=1
    dataset.loc[(dataset['Fare']>14.454)&(dataset['Fare']<=31.0), 'Fare']=2
    dataset.loc[dataset['Fare']>31, 'Fare']=3
    dataset['Fare']=dataset['Fare'].astype(int)

train_df= train_df.drop(['FareBand'],axis=1)
combine = [train_df, test_df]

train_df.head(10)


# In[49]:


test_df.head()


# # 생존여부 예측

# In[52]:


X_train = train_df.drop('Survived',axis=1)
Y_train = train_df['Survived']
X_test = test_df.drop('PassengerId',axis=1).copy()
                      
X_train.shape, Y_train.shape, X_test.shape


# ### 1. Logistic Regressiong 

# In[55]:


logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
Y_pred = logreg.predict(X_test)
acc_log = round(logreg.score(X_train, Y_train)*100, 2)
acc_log


# In[57]:


coeff_df = pd.DataFrame(train_df.columns.delete(0))
coeff_df.columns = ['Feature']
coeff_df['Correlation']=pd.Series(logreg.coef_[0])


coeff_df.sort_values(by='Correlation', ascending=False)


# ### 2. SVM(support vector machine)

# In[59]:


svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train,Y_train)*100,2)
acc_svc


# ### 3. K-NN

# In[60]:


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
acc_knn = round(knn.score(X_train, Y_train)*100,2)
acc_knn


# ### 4. Gaussian Naive Bayes

# In[62]:


gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
Y_pred = gaussian.predict(X_test)
acc_gaussian = round(gaussian.score(X_train, Y_train)*100,2)
acc_gaussian


# ### 5. Perceptron

# In[65]:


perceptron = Perceptron()
perceptron.fit(X_train, Y_train)
Y_pred = perceptron.predict(X_test)
acc_perceptron = round(perceptron.score(X_train, Y_train)*100, 2)
acc_perceptron


# ### 6. Linear SVC

# In[66]:


linear_svc = LinearSVC()
linear_svc.fit(X_train, Y_train)
Y_pred = linear_svc.predict(X_test)
acc_linear_svc = round(linear_svc.score(X_train, Y_train)*100, 2)
acc_linear_svc


# ### 7. SGD( Stochastic Gradient Descent )

# In[67]:


sgd = SGDClassifier()
sgd.fit(X_train, Y_train)
Y_pred = sgd.predict(X_test)
acc_sgd = round(sgd.score(X_train,Y_train)*100, 2)
acc_sgd


# ### 8. Decision Tree

# In[71]:


decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, Y_train)
Y_pred = decision_tree.predict(X_test)
acc_decision_tree = round(decision_tree.score(X_train, Y_train)*100,2)
acc_decision_tree


# In[ ]:


### 9. Random Forest


# In[72]:


random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(X_train, Y_train)
Y_pred = random_forest.predict(X_test)
random_forest.score(X_train, Y_train)
acc_random_forest = round(random_forest.score(X_train, Y_train) * 100, 2)
acc_random_forest


# # Summary

# In[73]:


models = pd.DataFrame({
    'Model': ['Support Vector Machines', 'KNN', 'Logistic Regression', 
              'Random Forest', 'Naive Bayes', 'Perceptron', 
              'Stochastic Gradient Decent', 'Linear SVC', 
              'Decision Tree'],
    'Score': [acc_svc, acc_knn, acc_log, 
              acc_random_forest, acc_gaussian, acc_perceptron, 
              acc_sgd, acc_linear_svc, acc_decision_tree]})
models.sort_values(by='Score', ascending=False)

