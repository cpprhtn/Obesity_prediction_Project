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

seoul['Obesity'].value_counts()



X_train = busan[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
            'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
            'nub_01z1','oba_01z1','obb_01z1','mtc_01z1','mta_01z1','mtb_01z1',
            'hya_06z1','dia_06z1','ara_22z1','sod_02z1']]
y_train = busan["Obesity"]

