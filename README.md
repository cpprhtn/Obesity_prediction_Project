# Obesity_prediction_Project

## 시작하게된 계기
코로나 사태가 지속됨에 따라 외부 활동량이 줄면서 살 찌는 사람이 늘어났다.<br>
여러 커뮤니티에는 확찐자라는 말이 돌아다니고 있다.<br>
평소에 살이 안찌는 나였지만, 4달넘는 기간 사이에 4kg가 찌면서 운동을 시작했다.<br>
그와 동시에, 비만이 미치는 효과등을 알아보고, 이를 통한 비만 예측 모델을 만들어 보고 싶어서 시작하게 되었다.

## 이론적 배경
세계보건기구(WHO)에서는 비만을 '건강을 해칠 정도로 지방조직에 비정상적인 또는 과도한 지방질이 축적되는 상태'라고 정의하고 있다. <br>
비만을 질병으로 인식하는 이유는 비만이 여러가지 대사성 질환(당뇨병, 고혈압 등)과 밀접한 관련이 있기 때문이다.<br>
2013년 미국 의학 협회에서는 비만을 질병으로 공식 선언하였고, 비만은 새로운 공중보건 문제로 보고 있으며 심각한 건강 문제로 정의하고 있다.<br>


비만은 비만으로 그치는 것이 아니라 각종 질병의 원인이 될 수 있으며, 정신적인 질병까지 유발할 수 있다.<br>
제2형 당뇨병, 이상지질혈증, 고혈압, 지방간, 담낭질환, 관상동맥질환(협심증, 심근경색증), 뇌졸중, 수면무호흡증, 통풍, 골관절염, 월경이상, 대장암, 유방암 등이 대표적인 비만과 관련된 질병이다.

대한비만학회는 기존에는 BMI가 18.5 미만이면 저체중, 18.5∼23은 정상, 23~25이면 과체중, 25∼30은 경도비만, 30∼35는 중등도비만, 35 이상이면 고도비만으로 구분했었으나, 2018년 비만진료지침에서 단계별 용어가 새롭게 변경되어 18.5 미만이면 저체중, 18.5∼25 미만은 정상, 25∼30 미만은 '1단계 비만', 30∼40 미만은 '2단계 비만', 40 이상이면 '3단계 비만'으로 구분한다.
- 비만여부 종속변수 생성시
  - 18.5 미만 **저체중**
  - 18.5∼25 미만 **정상**
  - 25∼30 미만 **비만**

### 종속변수
- 비만여부
### 독립변수
505개의 항목 중 이론적 배경에 따라 비만에 영향을 주는 요인을 중심으로 선정하였고, 08~10 총 11년간 연속적으로 측정되어 비만을 분류하는대ㅔ 영향을 미칠 수 있는 항목 중 항목별 범주의 빈도가 학습에 충분한 항목을 선정하였다.

### 비만도 분포율
- 1 : 저체중
- 2 : 정상
- 3 : 비만
```
busan['Obesity'].value_counts()
Out[]:
2    76374    # 0.6986662275646304
3    26480    # 0.24223795671185758
1     6460    # 0.059095815723512087
Name: Obesity, dtype: int64

seoul['Obesity'].value_counts()
Out[]:
2    111777   # 0.6926966814364949
3     39098   # 0.2422954172218263
1     10490   # 0.0650079013416788
Name: Obesity, dtype: int64
```
## 일지
|Date|Description|Remark|
|:---:|:---|---|
|07_24|Start Project||
|07_24|[Data request](./Progress_img/README.md)|[질병관리본부](https://chs.cdc.go.kr/chs/rdr/rdrInfoProcessMain.do) 에 자료신청|
|07_27|[Data Transformation 1](./EDA/1차_전처리)|1차 전처리 완료 (.txt -> .csv)|
|ㄴ|[EDA 1차 전처리 설명](./EDA)||
|07_28|Theoretical background||
|ㄴ|[dependent variable, independent variable](./EDA/README.md)||
|07_29|[Find Common Columns](./data/원시자료_이용지침서)||
|ㄴ|[Pull Only Required Common Columns](./data/README.md)||
|ㄴ|[Data Transformation 2](./EDA/2차_전처리)|Apply common column |
|ㄴ|[EDA 2차 전처리 설명](./EDA)||
|07_30|[Data Transformation 2](./EDA/2차_전처리)|2010 ~ 2014년까지 변환중 데이터의 문제점 발생|
|ㄴ|[Different data standards before and after 14's](https://github.com/cpprhtn/Obesity_prediction_Project/tree/master/data/Different_data%20_standards)|문제 해결 과정|
|07_31|[Data Transformation 2](./EDA/2차_전처리)|2차 전처리 완료|
|ㄴ|2010~2013년과 2014 이후의 결혼여부 칼럼명 다른거 수정|sod_02z1 -> sod_02z2|
|08_01|종속변수 생성|비만여부 칼럼 생성|
|ㄴ|[EDA 종속변수 생성과정 설명](./EDA)|아래로 스크롤 필요|
|08_02|[Naive Bayes Model](./Predict_Model)|R로 제작|
|ㄴ|[]결혼여부 칼럼명을 sod_02z1 칼럼으로 일치화시킴](./EDA/README.md)|아래로 스크롤 필요|
|08_03|[Naive Bayes Model Visualization](./Predict_Model)||
|ㄴ|Naive Bayes Model Finish|나이브 베이즈 모델 완료|
|08_04|[Logistic Regression Model](./Predict_Model)|R로 제작|
|08_05|Finish Logistic Regression Model|모델 제작 완료|
|08_06|[Random Forest Model](./Predict_Model)|R로 제작|
