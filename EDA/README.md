# EDA 과정

## 1차 전처리
- .txt파일을 .csv파일로 변환
### Data coloumns 확인
```
> busan_08.columns
Out[]:
Index(['id', 'fma_12z1', 'fma_20z1', 'city_cd', 'bogun_cd', 'jijum_cd', 'gagu_cd', 'gaguw_cd', 'town_t', 'apt_t',
       ...
       'i1a_02z1', 'i2a_01z1', 'i2a_02z1', 'i3a_01z1', 'i3a_02z1', 'i4a_01z1', 'i4a_02z1', 'i5a_01z1', 'i5a_02z1', 'h_admincode'], dtype='object', length=505)
```
### 필요한 컬럼만 찾기
> 보건소 번호, 주택유형, 세대유형, 기초생활수급자 여부, 가구소득, 현재 흡연여부, 음주빈도, 나이, 성별, 걷기 일수, 저염선호 - 평상시 소금섭취 수준, 본인인지체형, 체중조절 시도경험, 키, 체중 주관적 스트레스 수준, 우울감 경험, 자살생각 경험, 고혈압 의사진단여부, 당뇨병 의사진단여부 경제활동여부, 혼인상태 등

### 2008 ~ 2018년까지의 공통 칼럼들 (비만 관련)
> 보건소 번호, 만나이, 성별, 주택유형, 세대유형, 기초생활수급자 여부, 가구소득, 현재 흡연 여부, 연간 음주 빈도, 격렬한 신체활동 일수(09~17), 중등도 신체활동 일수(09~17),걷기 실천 일수, 주간 아침식사 일수(10~), 평상시 소금섭취 수준-저염선호(~17), 본인인지체형, 체중조절 경험여부, 키, 몸무게, 수면시간, 주관적 스트레스 수준, 우울감 경험 여부, 고혈압 현재 치료 여부(~17), 당뇨병 현재 치료 여부(~17), 관절염 현재 치료 여부(~17), 혼인상태 <br>
> 'bogun_cd','age','sex','apt_t','fma_19z1','fma_04z1','fma_24z1','sma_03z2','drb_01z2',
'pha_04z1','pha_07z1','phb_01z1','nua_01z1','nub_01z1','oba_01z1','obb_01z1','oba_02z1',
'oba_03z1','mtc_01z1','mta_01z1','mtb_01z1','hya_06z1','dia_06z1','ara_22z1','sod_02z1'
**10 ~ 17년 데이터 사용시 원하는 칼럼 모두 사용가능**

## 2차 전처리
- 가구소득(년 기준)이 14년부터 없어지고, 달소득만 남음 <br>
[문제해결 완료](https://github.com/cpprhtn/Obesity_prediction_Project/tree/master/data/Different_data%20_standards) <- 보러가기
### 결측치 확인
```
> b_17.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 14521 entries, 0 to 14520
Data columns (total 25 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   bogun_cd  14521 non-null  int64  
 1   age       14521 non-null  int64  
 2   sex       14521 non-null  int64  
 3   apt_t     14521 non-null  int64  
 4   fma_19z1  14521 non-null  int64  
 5   fma_04z1  14521 non-null  int64  
 6   fma_24z1  14521 non-null  int64  
 7   sma_03z2  14521 non-null  int64  
 8   drb_01z2  14521 non-null  int64  
 9   pha_04z1  14521 non-null  int64  
 10  pha_07z1  14521 non-null  int64  
 11  phb_01z1  14521 non-null  int64  
 12  nua_01z1  14521 non-null  int64  
 13  nub_01z1  14521 non-null  int64  
 14  oba_01z1  14521 non-null  int64  
 15  obb_01z1  14521 non-null  int64  
 16  oba_02z1  14521 non-null  float64
 17  oba_03z1  14521 non-null  float64
 18  mtc_01z1  14521 non-null  int64  
 19  mta_01z1  14521 non-null  int64  
 20  mtb_01z1  14521 non-null  int64  
 21  hya_06z1  14521 non-null  int64  
 22  dia_06z1  14521 non-null  int64  
 23  ara_22z1  14521 non-null  int64  
 24  sod_02z2  14521 non-null  int64  
dtypes: float64(2), int64(23)
```

## 종속변수 생성
### BMI 지수 적용
BMI=몸무게/((키/100)\*\*2)
```
def BMI(A):
    A['Obesity']=A['oba_03z1']/((A['oba_02z1']/100)**2)
```

### 비만여부 다항변수 처리
```
def Oba(x):
    if x>=25: return 3
    elif x<18.5: return 1
    else: return 2
```

### 전체작업 함수 (기존의 키, 몸무게 칼럼도 제거)
```
def Change_Oba(A):
    BMI(A)
    A['Obesity'] = A['Obesity'].apply(Oba)
    del A['oba_03z1']
    del A['oba_02z1']
```


# 10~13년과 14~17년 칼럼의 동일화
- R로 처리
```
names(b_14) <- names(b_10)
names(b_15) <- names(b_10)
names(b_16) <- names(b_10)
names(b_17) <- names(b_10)
```
