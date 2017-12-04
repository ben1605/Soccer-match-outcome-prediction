#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:33:46 2017

@author: ZhengFeng
"""
import pandas as pd 
import numpy as np
match=pd.read_csv("Match.csv")
for i in range(1,12):  #clear match data
    match=match[np.invert(np.isnan(match['home_player_X'+str(i)]))] 
    match=match[np.invert(np.isnan(match['away_player_X'+str(i)]))]
    match=match[np.invert(np.isnan(match['home_player_Y'+str(i)]))] 
    match=match[np.invert(np.isnan(match['away_player_Y'+str(i)]))]
    match=match[np.invert(np.isnan(match['home_player_'+str(i)]))] 
    match=match[np.invert(np.isnan(match['away_player_'+str(i)]))]
match['result']=2
for i in range(len(match['result'])):   #add match result
    if(match.iloc[i,9]>match.iloc[i,10]):
        match.iloc[i,115]='win'
    elif(match.iloc[i,9]<match.iloc[i,10]):
        match.iloc[i,115]='lose'
    else:
        match.iloc[i,115]='draw'
        
home_forX=[]
home_forY=[]

home_pair=[[(0.,0.)]*11 for i in range(21361)]
for i in range(1,12):
    home_forX.append(list((match['home_player_X'+str(i)])))
    home_forY.append(list((match['home_player_Y'+str(i)])))

home_for1=[[0.]*11 for i in range(21361)]
home_for2=[[0.]*11 for i in range(21361)]

for i in range(21361):
    for j in range(11):
        home_for1[i][j]=home_forX[j][i]
        home_for2[i][j]=home_forY[j][i]
        
homeforward=[0.]*21361
homedefender=[0.]*21361
for i in range(21361):
    temp=home_for2[i]
    homeforward[i]=1
    defnum=temp[1]
    homedefender[i]=1
    fornum=temp[10]
    for j in range(2,len(temp)):
        if temp[j]==defnum:
            homedefender[i]+=1
        else:
            break
    for j in range(0,len(temp)-1):
        if temp[9-j]==fornum:
            homeforward[i]+=1
        else:
            break

away_forX=[]
away_forY=[]


for i in range(1,12):
    away_forX.append(list((match['away_player_X'+str(i)])))
    away_forY.append(list((match['away_player_Y'+str(i)])))

away_for1=[[0.]*11 for i in range(21361)]
away_for2=[[0.]*11 for i in range(21361)]

for i in range(21361):
    for j in range(11):
        away_for1[i][j]=away_forX[j][i]
        away_for2[i][j]=away_forY[j][i] 

       
awayforward=[0.]*21361
awaydefender=[0.]*21361
for i in range(21361):
    temp=away_for2[i]
    awayforward[i]=1
    defnum=temp[1]
    awaydefender[i]=1
    fornum=temp[10]
    for j in range(2,len(temp)):
        if temp[j]==defnum:
            awaydefender[i]+=1
        else:
            break
    for j in range(0,len(temp)-1):
        if temp[9-j]==fornum:
            awayforward[i]+=1
        else:
            break
        

player=pd.read_csv("Player_Attributes.csv")
player=player.sort_values(by=['player_api_id'],ascending=[True])

playerID=[]   #get list of player ID
for i in range(len(player['player_api_id'])):
    if not (player.iloc[i,2] in playerID):
        playerID.append(player.iloc[i,2])

rating=[]
rating.append([player.iloc[0,3],player.iloc[0,4]])
k=0
for i in range(1,len(player['player_api_id'])):
    if player.iloc[i,2]==player.iloc[i-1,2]:
        rating[k].append(player.iloc[i,3])
        rating[k].append(player.iloc[i,4])
    else:
        k+=1
        rating.append([player.iloc[i,3],player.iloc[i,4]])

table=dict(zip(playerID,rating))
 
history_home=[]
history_away=[]
history=[]

X0=[[0.]*27]*len(match)                
X=[[0.]*6]*len(match)  
X0=np.asmatrix(X0)
X=np.asmatrix(X)

for i in range(len(match)): 
    
    if i%2000==0:
        print(i)
       
    for j in range(55,77):                      #build X0
        rate_list=table[match.iloc[i,j]]
        date=match.iloc[i,5]
        if (np.isnan(rate_list[1])==True):
            m=2
        else:
            m=0
        for k in range(2,len(rate_list),2):
            if(abs(rate_list[k]-date)<abs(rate_list[m]-date) and np.isnan(rate_list[k+1])==False):
                m=k
        X0[i,j-55]=rate_list[m+1]
    count=0   #number of bets avaliable for each match
    bet=[0.]*3
    bet=np.asmatrix(bet)
    for j in range(85,97): #85-96
        if not np.isnan(match.iloc[i,j]):
            bet[0,(j-85)%3]+=1/match.iloc[i,j]
            count+=1
    for j in range(100,115): #100-114
        if not np.isnan(match.iloc[i,j]):
            bet[0,(j-100)%3]+=1/match.iloc[i,j]
            count+=1
    count=count/3
    if count!=0:
        if bet[0,0]>bet[0,1] and bet[0,0]>bet[0,2]:
            X0[i,22]=1
        elif bet[0,1]>bet[0,2]:
            X0[i,22]=0
        else:
            X0[i,22]=-1
    
    happen=False
    for j in range(len(history)):
        if (match.iloc[i,7]==history_home[j] and match.iloc[i,8]==history_away[j]):
            happen=True
            X0[i,24]=history[j][1]/history[j][0]
            X0[i,25]=history[j][2]/history[j][0]
            X0[i,26]=history[j][3]/history[j][0]
            history[j][0]+=1
            if match.iloc[i,115]=='win':
                history[j][1]+=1
            if match.iloc[i,115]=='lose':
                history[j][2]+=1
            if match.iloc[i,115]=='draw':
                history[j][3]+=1
            break
                
        if (match.iloc[i,8]==history_home[j] and match.iloc[i,7]==history_away[j]):
            happen=True
            X0[i,24]=float(history[j][2]/history[j][0])
            X0[i,25]=float(history[j][1]/history[j][0])
            X0[i,26]=float(history[j][3]/history[j][0])
            history[j][0]+=1
            if match.iloc[i,115]=='win':
                history[j][2]+=1
            if match.iloc[i,115]=='lose':
                history[j][1]+=1
            if match.iloc[i,115]=='draw':
                history[j][3]+=1
            break
    
    if not happen:
        history_home.append(match.iloc[i,7])
        history_away.append(match.iloc[i,8])
        if match.iloc[i,115]=='win':
                history.append([1,1,0,0])
        if match.iloc[i,115]=='lose':
                history.append([1,0,1,0])
        if match.iloc[i,115]=='draw':
                history.append([1,0,0,1])
        X0[i,24]=1/3.
        X0[i,25]=1/3.
        X0[i,26]=1/3.
        
      
    
    
    feature_rating=[11,11]    
    k=0
    for j in range(len(feature_rating)):
        X[i,j]=1
        for h in range(feature_rating[j]):
            X[i,j]*=X0[i,k]**(float(1/feature_rating[j]))
            k+=1
        
    X[i,2]=X0[i,k]
    X[i,3]=np.var(X0[i,0:11])
    X[i,4]=np.var(X0[i,11:22])
    X[i,5]=1
        
Y=np.asmatrix(match['result']).transpose()


def perceptron(X,y):
    
    w=np.random.rand(np.shape(X)[1])
    w=np.asmatrix(w).transpose()
    y0=np.sign(X*w)
    
    m=0
    maxsteps=1000
    while m<=maxsteps:
        i=1
        while y0[i,0]==y[i,0]:
            i+=1
        w=w+y[i,0]*X[i,:].transpose();
        y0=np.sign(X*w)
        m=m+1
        
    return w

w_1=perceptron(X_train,Y1_train)
w_2=perceptron(X_train,Y2_train)

Y1_test_predict_perceptron=np.sign(X_test*w_1)
Y2_test_predict_perceptron=np.sign(X_test*w_2)

error_1=0
error_2=0
error=0
        
for i in range(len(X_test)):
    if Y1_test_predict_perceptron[i]==1 and Y2_test_predict_perceptron[i]==1:
        Y1_test_predict_perceptron[i]==-1
        Y1_test_predict_perceptron[i]==-1
    if Y1_test_predict_perceptron[i]!=Y1_test[i] or Y2_test_predict_perceptron[i]!=Y2_test[i]:
        error+=1
    
    if Y1_test_predict_perceptron[i]!=Y1_test[i]:
        error_1+=1
    if Y2_test_predict_perceptron[i]!=Y2_test[i]:
        error_2+=1


    

from sklearn.ensemble import RandomForestClassifier  #decision tree
from sklearn.datasets import make_classification
clf = RandomForestClassifier(min_samples_split=15,n_estimators=3,criterion='gini',max_depth=10, random_state=0)
forest=clf.fit(X[0:17088,:],Y[0:17088])
y_test=clf.predict(X[17088:21361,:])
y_test.reshape([4273,1])
err=np.sum(np.asmatrix(y_test).transpose()!=Y[17088:21361])
print(err)



import statsmodels.api as sm  #linear regression
from scipy import stats
Y_linear=[[0.]]*len(Y)
Y_linear=np.asmatrix(Y_linear)
for i in range(len(Y)):
    if Y[i,0]=='win':
        Y_linear[i,0]=1
    if Y[i,0]=='lose':
        Y_linear[i,0]=-1
    if Y[i,0]=='draw':
        Y_linear[i,0]=0



fit = sm.OLS(Y_linear[0:17088], X[0:17088,:]).fit()
print(fit.summary())

w=fit.params
w=np.asmatrix(w).transpose()
Y_predict=X[17088:21361,:]*w

for i in range(50):
    error_linear=0
    for j in range(len(Y_predict)):
        if Y_predict[j,0]>=i*0.01:
            predict='win'
        elif Y_predict[j,0]<=-i*0.1:
            predict='lose'
        else:
            predict='draw'
        if predict!=Y[j+17088,0]:
            error_linear+=1
    print(error_linear)





X=[[0.]*6]*len(match) 
X=np.asmatrix(X)

for i in range(len(match)): 
    
    if i%2000==0:
        print(i)

    feature_rating=[11,11]    
    k=0
    for j in range(len(feature_rating)):
        X[i,j]=1
        for h in range(feature_rating[j]):
            X[i,j]*=X0[i,k]**(float(1/feature_rating[j]))
            k+=1
    
    X[i,2]=X0[i,k]
    X[i,3]=np.var(X0[i,0:11])
    X[i,4]=np.var(X0[i,11:22])
    X[i,5]=1
        

from sklearn.ensemble import RandomForestClassifier  #decision tree
from sklearn.datasets import make_classification
clf1 = RandomForestClassifier(min_samples_split=30,n_estimators=200,criterion='gini',max_depth=10, random_state=0)
forest1=clf1.fit(X[0:17088,:],Y1_train)
y1_test=clf1.predict(X[17088:21361,:])
y1_test.reshape([4273,1])
err1=np.sum(np.asmatrix(y1_test).transpose()!=Y1_test)
print(err1)

clf2 = RandomForestClassifier(min_samples_split=30,n_estimators=200,criterion='gini',max_depth=10, random_state=0)
forest2=clf2.fit(X[0:17088,:],Y2_train)
y2_test=clf2.predict(X[17088:21361,:])
y2_test.reshape([4273,1])
err2=np.sum(np.asmatrix(y2_test).transpose()!=Y2_test)
print(err2)

error_forest=0
        
for i in range(len(X_test)):
    if y1_test[i]==Y1_test[i] and y2_test[i]==Y2_test[i]:
        error_forest+=1
print(error_forest)



Y1=[0.]*len(Y) #multiclass linear classification
Y2=[0.]*len(Y)
for i in range(len(Y1)):
    if Y[i]=='win':
        Y1[i]=1
        Y2[i]=-1
    elif Y[i]=='draw':
        Y1[i]=-1
        Y2[i]=-1
    else:
        Y1[i]=-1
        Y2[i]=1

Y1=np.asmatrix(Y1).transpose()
Y2=np.asmatrix(Y2).transpose()

X_train=X[0:17088]
X_test=X[17088:21361]
Y1_train=Y1[0:17088]
Y2_train=Y2[0:17088]
Y1_test=Y1[17088:21361]
Y2_test=Y2[17088:21361]

def l_hinge_sg(x,y,w):
    if y*w.transpose()*x<1:
        g=-y*x
    elif y*w.transpose()*x==1:
        g=-np.random.rand()*y*x
    else:
        g=0

    return g


def hinge(x,y,w):
    if 1-y*w.transpose()*x>0:
        return 1-y*w.transpose()*x
    else:
        return 0
    
def l_logistic_sg(x,y,w):
    return y*x/(1+np.exp(y*w.transpose()*x))


def logistic(x,y,w):
    return np.log(1+np.exp(-y*w.transpose()*x))

def proximal_gradient(x,y):
    w_hinge=np.random.rand(x.shape[1])
    w_hinge=np.asmatrix(w_hinge).transpose()
    alpha=10
    for i in range(50):
        g=np.zeros(np.shape(x)[1])
        g=np.asmatrix(g).transpose()
        for j in range(len(x)):
            g+=l_hinge_sg(x[j,:].transpose(),y[j,0],w_hinge)
        g/=np.shape(x)[1]
        w_hinge=(w_hinge-alpha*g)/(1+2*alpha)
        alpha/=2
    return w_hinge

def proximal_gradient_2(x,y):
    w=np.random.rand(x.shape[1])
    w=np.asmatrix(w).transpose()
    alpha=10
    for i in range(50):
        g=np.zeros(np.shape(x)[1])
        g=np.asmatrix(g).transpose()
        for j in range(len(x)):
            g+=l_logistic_sg(x[j,:].transpose(),y[j,0],w)
        g/=np.shape(x)[1]
        w=(w-alpha*g)/(1+2*alpha)
        print(w)
    return w



w_hinge_1=proximal_gradient(X_train,Y1_train)
w_hinge_2=proximal_gradient(X_train,Y2_train)



Y1_test_predict_hinge=np.sign(X_test*w_hinge_1)
Y2_test_predict_hinge=np.sign(X_test*w_hinge_2)

error_logistic=0
error_hinge=0
error_1=0
error_2=0
        
for i in range(len(X_test)):

    if Y1_test_predict_hinge[i]!=Y1_test[i] or Y2_test_predict_hinge[i]!=Y2_test[i]:
        error_hinge+=1
        
    if Y1_test_predict_hinge[i]!=Y1_test[i]:
        error_1+=1
        
    if Y2_test_predict_hinge[i]!=Y2_test[i]:
        error_2+=1


print(error_hinge)
print(error_1)
print(error_2)


