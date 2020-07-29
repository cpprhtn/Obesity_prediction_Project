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
busan_08.isna().sum()

busan_08.columns

# 보건소 번호, 주택유형, 세대유형, 기초생활수급자 여부, 가구소득, 현재 흡연여부, 음주빈도,
# 나이, 성별, 걷기 일수, 저염선호 - 평상시 소금섭취 수준, 본인인지체형, 체중조절 시도경험, 키,
# 체중 주관적 스트레스 수준, 우울감 경험, 자살생각 경험, 고혈압 의사진단여부, 당뇨병 의사진단여부
# 경제활동여부, 혼인상태
b_08 = busan_08[['bogun_cd','apt_t','fma_19z1','fma_04z1','fma_12z1','sma_03z1','drb_01z1',
                 'age','sex','phb_01z1','nub_01z1','oba_01z1','obb_01z1','oba_02z1',
                 'oba_03z1','mta_01z1','mtb_01z1','mtd_01z1','hya_04z1','dia_05z1',
                 'soa_01z1','sod_02z1']]
b_08.isna().sum()

s_08 = seoul_08[['bogun_cd','apt_t','fma_19z1','fma_04z1','fma_12z1','sma_03z1','drb_01z1',
                 'age','sex','phb_01z1','nub_01z1','oba_01z1','obb_01z1','oba_02z1',
                 'oba_03z1','mta_01z1','mtb_01z1','mtd_01z1','hya_04z1','dia_05z1',
                 'soa_01z1','sod_02z1']]
s_08.isna().sum()
