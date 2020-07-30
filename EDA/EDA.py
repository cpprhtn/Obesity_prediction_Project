#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:28:28 2020

@author: cpprhtn
"""

import pandas as pd
# 최대 줄 수 설정
pd.set_option('display.max_rows', 10000)
# 최대 열 수 설정
pd.set_option('display.max_columns', 10000)
# 표시할 가로의 길이
pd.set_option('display.width', 10000)

busan_08 = pd.read_csv('busan_08.csv',  encoding = 'cp949')
seoul_08 = pd.read_csv('seoul_08.csv',  encoding = 'cp949')

busan_08.columns




'bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','sma_03z2','drb_01z2',
'pha_04z1','pha_07z1','phb_01z1','nua_01z1','nub_01z1','oba_01z1','obb_01z1','oba_02z1',
'oba_03z1','mtc_01z1','mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1'


busan_10 = pd.read_csv('busan_10.csv',  encoding = 'cp949')
seoul_10 = pd.read_csv('seoul_10.csv',  encoding = 'cp949')

b_10 = busan_10[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','sma_03z2','drb_01z2',
                 'pha_04z1','pha_07z1','phb_01z1','nua_01z1','nub_01z1','oba_01z1','obb_01z1','oba_02z1',
                 'oba_03z1','mtc_01z1','mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]
s_10 = seoul_10[['bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_12z1','sma_03z2','drb_01z2',
                 'pha_04z1','pha_07z1','phb_01z1','nua_01z1','nub_01z1','oba_01z1','obb_01z1','oba_02z1',
                 'oba_03z1','mtc_01z1','mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1']]

b_10.isna().sum()
s_10.isna().sum()

b_10.to_csv('b_10.csv', index=False)
s_10.to_csv('s_10.csv', index=False)