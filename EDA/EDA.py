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
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z2']]
s_14 = seoul_14[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z2']]

b_14.isna().sum()
s_14.isna().sum()

b_14.to_csv('b_14.csv', index=False)
s_14.to_csv('s_14.csv', index=False)





busan_15 = pd.read_csv('busan_15.csv',  encoding = 'cp949')
seoul_15 = pd.read_csv('seoul_15.csv',  encoding = 'cp949')

b_15 = busan_15[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z2']]
s_15 = seoul_15[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z2']]

b_15.isna().sum()
s_15.isna().sum()

b_15.to_csv('b_15.csv', index=False)
s_15.to_csv('s_15.csv', index=False)




busan_16 = pd.read_csv('busan_16.csv',  encoding = 'cp949')
seoul_16 = pd.read_csv('seoul_16.csv',  encoding = 'cp949')

b_16 = busan_16[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z2']]
s_16 = seoul_16[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z2']]

b_16.isna().sum()
s_16.isna().sum()

b_16.to_csv('b_16.csv', index=False)
s_16.to_csv('s_16.csv', index=False)



busan_17 = pd.read_csv('busan_17.csv')
seoul_17 = pd.read_csv('seoul_17.csv')

b_17 = busan_17[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z2']]
s_17 = seoul_17[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1',
                 'sma_03z2','drb_01z2','pha_04z1','pha_07z1','phb_01z1','nua_01z1',
                 'nub_01z1','oba_01z1','obb_01z1','oba_02z1','oba_03z1','mtc_01z1',
                 'mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z2']]

b_17.isna().sum()
s_17.isna().sum()

b_17.to_csv('b_17.csv', index=False)
s_17.to_csv('s_17.csv', index=False)









#8/1
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

#'oba_02z1','oba_03z1'
#키, 몸무게
def BMI(A):
    A['Obesity']=A['oba_03z1']/((A['oba_02z1']/100)**2)

        
def Oba(x):
    if x>=25: return 3
    elif x<18.5: return 1
    else: return 2
        
def Change_Oba(A):
    BMI(A)
    A['Obesity'] = A['Obesity'].apply(Oba)
    del A['oba_03z1']
    del A['oba_02z1']
    
    
Change_Oba(b_10)
Change_Oba(b_11)
Change_Oba(b_12)
Change_Oba(b_13)
Change_Oba(b_14)
Change_Oba(b_15)
Change_Oba(b_16)
Change_Oba(b_17)

Change_Oba(s_10)
Change_Oba(s_11)
Change_Oba(s_12)
Change_Oba(s_13)
Change_Oba(s_14)
Change_Oba(s_15)
Change_Oba(s_16)
Change_Oba(s_17)

b_10.to_csv('b_10.csv', index=False)
b_11.to_csv('b_11.csv', index=False)
b_12.to_csv('b_12.csv', index=False)
b_13.to_csv('b_13.csv', index=False)
b_14.to_csv('b_14.csv', index=False)
b_15.to_csv('b_15.csv', index=False)
b_16.to_csv('b_16.csv', index=False)
b_17.to_csv('b_17.csv', index=False)

s_10.to_csv('s_10.csv', index=False)
s_11.to_csv('s_11.csv', index=False)
s_12.to_csv('s_12.csv', index=False)
s_13.to_csv('s_13.csv', index=False)
s_14.to_csv('s_14.csv', index=False)
s_15.to_csv('s_15.csv', index=False)
s_16.to_csv('s_16.csv', index=False)
s_17.to_csv('s_17.csv', index=False)




