#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:45:42 2020

@author: cpprhtn
"""

path = 'd:/test.txt'
with open(path, 'r', encoding='utf-16') as f:
    lines  = f.readlines()
import pandas as pd

'''
_a는 서울
_b는 부산

txt파일을 csv파일로 변환해줌
'''
file1 = pd.read_csv('chs08_a.txt', delimiter = '\t',  encoding = 'cp949')
file1.to_csv('seoul_08.csv', index=False)
file2 = pd.read_csv('chs08_b.txt', delimiter = '\t',  encoding = 'cp949')
file2.to_csv('busan_08.csv', index=False)



'''
chs18_b.txt파일만 cp949 적용이 안됨 
'utf-8' codec can't decode byte 0xbe in position 3204: invalid start byte

그래서 한글 포기하고 unicode_escape 이걸로 인코딩함
'''