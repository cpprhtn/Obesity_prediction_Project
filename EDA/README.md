# EDA 과정

### .txt파일을 .csv파일로 변환

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

- 가구소득(년 기준)이 14년부터 없어지고, 달소득만 남음
[문제해결 완료](https://github.com/cpprhtn/Obesity_prediction_Project/tree/master/data/Different_data%20_standards)


### 결측치 확인
```
> s_10.isna().sum()
Out[]:
bogun_cd    0
age         0
sex         0
apt_t       0
fma_19z1    1
fma_04z1    1
fma_12z1    1
sma_03z2    0
drb_01z2    5
pha_04z1    0
pha_07z1    0
phb_01z1    0
nua_01z1    0
nub_01z1    0
oba_01z1    0
obb_01z1    0
oba_02z1    0
oba_03z1    0
mtc_01z1    0
mta_01z1    0
mtb_01z1    0
hya_06z1    0
dia_06z1    0
ara_22z1    0
sod_02z1    0
dtype: int64
```
