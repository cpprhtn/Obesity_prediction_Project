#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:29:57 2020

@author: cpprhtn
"""



import pandas as pd

b_10 = pd.read_csv('b_10.csv',  encoding = 'cp949')
b_11 = pd.read_csv('b_11.csv',  encoding = 'cp949')
b_12 = pd.read_csv('b_12.csv',  encoding = 'cp949')
b_13 = pd.read_csv('b_13.csv',  encoding = 'cp949')
b_14 = pd.read_csv('b_14.csv',  encoding = 'cp949')
b_15 = pd.read_csv('b_15.csv',  encoding = 'cp949')
b_16 = pd.read_csv('b_16.csv',  encoding = 'cp949')
b_17 = pd.read_csv('b_17.csv',  encoding = 'cp949')

s_10 = pd.read_csv('s_10.csv',  encoding = 'cp949')
s_11 = pd.read_csv('s_11.csv',  encoding = 'cp949')
s_12 = pd.read_csv('s_12.csv',  encoding = 'cp949')
s_13 = pd.read_csv('s_13.csv',  encoding = 'cp949')
s_14 = pd.read_csv('s_14.csv',  encoding = 'cp949')
s_15 = pd.read_csv('s_15.csv',  encoding = 'cp949')
s_16 = pd.read_csv('s_16.csv',  encoding = 'cp949')
s_17 = pd.read_csv('s_17.csv',  encoding = 'cp949')


busan = pd.concat([b_10,b_11,b_12,b_13,b_14,b_15,b_16,b_17])
busan.isna().sum()


seoul = pd.concat([s_10,s_11,s_12,s_13,s_14,s_15,s_16,s_17])
seoul.isna().sum()

busan['Obesity'].value_counts()
6460/109314 #0.059095815723512087
76374/109314 #0.6986662275646304
26480/109314 #0.24223795671185758

seoul['Obesity'].value_counts()
10490/161365 #0.0650079013416788
111777/161365 #0.6926966814364949
39098/161365 #0.2422954172218263

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(busan, target, test_size=0.3)
busan.shape()


col = [['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
            'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
            'nub_01z1','oba_01z1','obb_01z1','mtc_01z1','mta_01z1','mtb_01z1',
            'hya_06z1','dia_06z1','ara_22z1','sod_02z1']]
target = busan["Obesity"]

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

# Predict
pred = model.predict(x_test)

# Accuracy
(pred == y_test).mean()
#Out[]: 1.0

from sklearn.tree import export_graphviz
# .dot 파일로 export 해줍니다

# .dot 파일로 export 해줍니다
export_graphviz(model, out_file='tree.dot')

# 생성된 .dot 파일을 .png로 변환
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'decistion-tree.png', '-Gdpi=600'])

# jupyter notebook에서 .png 직접 출력
from IPython.display import Image
Image(filename = 'tree.dot')
