#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:33:46 2017

@author: WeijiaMao
"""

import pandas as pd
import numpy as np
match=pd.read_csv("Match.csv")
for i in range(1,12):  #clear match data
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

select_total=np.min(match.groupby(['result']).id.count())
match_test=pd.DataFrame()
match_train=pd.DataFrame()
for i,j in match.groupby(['result']):
    idx=np.random.randint(0,len(j),select_total)
    j=j.iloc[idx,:]
    idx_all=[k for k in range(len(j))]
    idx_test=np.random.randint(0,len(j),int(len(j)*0.2))
    j_test=j.iloc[idx_test,:]
    idx_train=list(set(idx_all)-set(idx_test))
    j_train=j.iloc[idx_train,:]
    match_train=match_train.append(j_train)
    match_test=match_test.append(j_test)

match=match_train.append(match_test)

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

X=[[0.]*24]*16508                #build X
X=np.asmatrix(X)
for i in range(16508): #55-76
    if i%2000==0:
        print(i)
    for j in range(55,77):  
        rate_list=table[match.iloc[i,j]]
        date=match.iloc[i,5]
        if (np.isnan(rate_list[1])==True):
            m=2
        else:
            m=0
        for k in range(2,len(rate_list),2):
            if(abs(rate_list[k]-date)<abs(rate_list[m]-date) and np.isnan(rate_list[k+1])==False):
                m=k
        X[i,j-55]=rate_list[m+1]
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
            X[i,22]=1
        elif bet[0,1]>bet[0,2]:
            X[i,22]=0
        else:
            X[i,22]=-1
        
X[:,23]=1
Y=np.asmatrix(match['result']).transpose()
#



    
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
clf = RandomForestClassifier(min_samples_split=10,n_estimators=500,criterion='gini',max_depth=9, random_state=0)
forest=clf.fit(X[0:13206,:],Y[0:13206])
y_test=clf.predict(X[13206:16508,:])
err=np.sum(np.asmatrix(y_test).transpose()!=Y[13206:16508])

print(clf.score(X[13206:16508,:],Y[13206:16508]))
cut_error=100000
cut=[0,1,-0.7]




#for j in range(1,10):
#    print(j)
#    for k in range(-10,-1):
#        for i in range(21374):
#            if y_[i]>j/10.:
#                y_[i]=1
#            elif y_[i]<k/10.:
#                y_[i]=-1
#            else:
#                y_[i]=0
#        err=np.sum(y_!=Y)
#        if cut_error>err:
#            cut_error=err
#            cut[0]=j
#            cut[1]=k

#from sklearn import tree
#i_tree = 0
#for tree_in_forest in forest.estimators_:
#    with open('tree_' + str(i_tree) + '.dot', 'w') as my_file:
#        my_file = tree.export_graphviz(tree_in_forest, out_file = my_file)
#        i_tree = i_tree + 1

Y1=0
c1=0
Y0=0
c0=0
Y_1=0
c_1=0
ctest=0

for i in range(13206,16508):
    if y_test[i-13206]=='draw':
        ctest+=1
    if Y[i]=='win':
        Y1+=1
        if y_test[i-13206]==Y[i]:
            c1+=1
    if Y[i]=='draw':
        Y0+=1
        if y_test[i-13206]==Y[i]:
            c0+=1
    if Y[i]=='lose':
        Y_1+=1
        if y_test[i-13206]==Y[i]:
            c_1+=1


    











    
    


