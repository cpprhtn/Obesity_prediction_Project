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

busan_08.isna().sum()

busan_08.columns
