#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:28:28 2020

@author: cpprhtn
"""

import pandas as pd
import math
pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 10000)
pd.set_option('display.width', 10000)


'''
10~13년까지는 fma_12z1, fma_20z1을 이용하여 
14~ 의 형식에 맞도록 정제할 예정

1  50미만
2  ~100미만
3  ~200미만
4  ~300미만
5  ~400미만
6  ~500미만
7  ~600미만
8  600이상
77 응답거부
99 모름
'''


busan_10 = pd.read_csv('busan_10.csv',  encoding = 'cp949')

b_10 = busan_10[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','fma_20z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]

b_10.isna().sum()

idx_nm = b_10[b_10['fma_12z1']!=2].index
b_10 = b_10.drop(idx_nm)
b_10.reset_index(inplace = True)


#14년 이후의 형식으로 변환
b_10['fma_20z1'] = b_10['fma_20z1']/100 + 2
def fma(x):
    if x<2.5: return 1
    elif x<3: return 2
    elif x>8: return 8
    else: return math.trunc(x)
        
b_10['fma_20z1'] = b_10['fma_20z1'].apply(fma)


b_10.rename(columns = {'fma_20z1' : 'fma_24z1'}, inplace = True)
del b_10['index']
del b_10['fma_12z1']
b_10.to_csv('b_10.csv', index=False)






seoul_10 = pd.read_csv('seoul_10.csv',  encoding = 'cp949')
s_10 = seoul_10[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','fma_20z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]

s_10.isna().sum()
#s_10의 결측치 제거
s_10.dropna(inplace = True)

idx_nm = s_10[s_10['fma_12z1']!=2].index
s_10 = s_10.drop(idx_nm)
s_10.reset_index(inplace = True)

s_10['fma_20z1'] = s_10['fma_20z1']/100 + 2
        
s_10['fma_20z1'] = s_10['fma_20z1'].apply(fma)

s_10.rename(columns = {'fma_20z1' : 'fma_24z1'}, inplace = True)
del s_10['index']
del s_10['fma_12z1']
s_10.to_csv('s_10.csv', index=False)










busan_11 = pd.read_csv('busan_11.csv',  encoding = 'cp949')
seoul_11 = pd.read_csv('seoul_11.csv',  encoding = 'cp949')

b_11 = busan_11[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','fma_20z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]
s_11 = seoul_11[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','fma_20z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]

b_11.isna().sum()
s_11.isna().sum()

idx_nm = b_11[b_11['fma_12z1']!=2].index
b_11 = b_11.drop(idx_nm)
b_11.reset_index(inplace = True)

b_11['fma_20z1'] = b_11['fma_20z1']/100 + 2
b_11['fma_20z1'] = b_11['fma_20z1'].apply(fma)

b_11.rename(columns = {'fma_20z1' : 'fma_24z1'}, inplace = True)
del b_11['index']
del b_11['fma_12z1']
b_11.to_csv('b_11.csv', index=False)



idx_nm = s_11[s_11['fma_12z1']!=2].index
s_11 = s_11.drop(idx_nm)
s_11.reset_index(inplace = True)

s_11['fma_20z1'] = s_11['fma_20z1']/100 + 2
s_11['fma_20z1'] = s_11['fma_20z1'].apply(fma)

s_11.rename(columns = {'fma_20z1' : 'fma_24z1'}, inplace = True)
del s_11['index']
del s_11['fma_12z1']
s_11.to_csv('s_11.csv', index=False)






busan_12 = pd.read_csv('busan_12.csv',  encoding = 'cp949')
seoul_12 = pd.read_csv('seoul_12.csv',  encoding = 'cp949')

b_12 = busan_12[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','fma_20z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]
s_12 = seoul_12[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','fma_20z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]

b_12.isna().sum()
s_12.isna().sum()

idx_nm = b_12[b_12['fma_12z1']!=2].index
b_12 = b_12.drop(idx_nm)
b_12.reset_index(inplace = True)

b_12['fma_20z1'] = b_12['fma_20z1']/100 + 2
b_12['fma_20z1'] = b_12['fma_20z1'].apply(fma)

b_12.rename(columns = {'fma_20z1' : 'fma_24z1'}, inplace = True)
del b_12['index']
del b_12['fma_12z1']
b_12.to_csv('b_12.csv', index=False)



idx_nm = s_12[s_12['fma_12z1']!=2].index
s_12 = s_12.drop(idx_nm)
s_12.reset_index(inplace = True)

s_12['fma_20z1'] = s_12['fma_20z1']/100 + 2
s_12['fma_20z1'] = s_12['fma_20z1'].apply(fma)

s_12.rename(columns = {'fma_20z1' : 'fma_24z1'}, inplace = True)
del s_12['index']
del s_12['fma_12z1']
s_12.to_csv('s_12.csv', index=False)







busan_13 = pd.read_csv('busan_13.csv',  encoding = 'cp949')
seoul_13 = pd.read_csv('seoul_13.csv',  encoding = 'cp949')

b_13 = busan_13[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','fma_20z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]
s_13 = seoul_13[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','fma_20z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]

b_13.isna().sum()
s_13.isna().sum()

idx_nm = b_13[b_13['fma_12z1']!=2].index
b_13 = b_13.drop(idx_nm)
b_13.reset_index(inplace = True)

b_13['fma_20z1'] = b_13['fma_20z1']/100 + 2
b_13['fma_20z1'] = b_13['fma_20z1'].apply(fma)

b_13.rename(columns = {'fma_20z1' : 'fma_24z1'}, inplace = True)
del b_13['index']
del b_13['fma_12z1']
b_13.to_csv('b_13.csv', index=False)



idx_nm = s_13[s_13['fma_12z1']!=2].index
s_13 = s_13.drop(idx_nm)
s_13.reset_index(inplace = True)

s_13['fma_20z1'] = s_13['fma_20z1']/100 + 2
s_13['fma_20z1'] = s_13['fma_20z1'].apply(fma)

s_13.rename(columns = {'fma_20z1' : 'fma_24z1'}, inplace = True)
del s_13['index']
del s_13['fma_12z1']
s_13.to_csv('s_13.csv', index=False)






#14년부터는 fma_24z1 이용(월 소득)
busan_14 = pd.read_csv('busan_14.csv',  encoding = 'cp949')
seoul_14 = pd.read_csv('seoul_14.csv',  encoding = 'cp949')

b_14 = busan_14[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]
s_14 = seoul_14[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]

b_14.isna().sum()
s_14.isna().sum()

b_14.to_csv('b_14.csv', index=False)
s_14.to_csv('s_14.csv', index=False)



