# Obesity_prediction_Project

R 프로젝트를 기획중이다.

Start 20.07.24 ~

질병관리본부에 데이터 요청을 한 상태이다.
허가가 떨어진다면 바로 프로젝트 진행을 해볼 예정 - 7.25

# 시작하게된 계기
코로나 사태가 지속됨에 따라 외부 활동량이 줄면서 살 찌는 사람이 늘어났다.<br>
여러 커뮤니티에는 확찐자라는 말이 돌아다니고 있다.<br>
평소에 살이 안찌는 나였지만, 4달넘는 기간 사이에 4kg가 찌면서 운동을 시작했다.<br>
그와 동시에, 비만이 미치는 효과등을 알아보고, 이를 통한 비만 예측 모델을 만들어 보고 싶어서 시작하게 되었다.

# 이론적 배경
세계보건기구(WHO)에서는 비만을 '건강을 해칠 정도로 지방조직에 비정상적인 또는 과도한 지방질이 축적되는 상태'라고 정의하고 있다. <br>
비만을 질병으로 인식하는 이유는 비만이 여러가지 대사성 질환(당뇨병, 고혈압 등)과 밀접한 관련이 있기 때문이다.<br>
2013년 미국 의학 협회에서는 비만을 질병으로 공식 선언하였고, 비만은 새로운 공중보건 문제로 보고 있으며 심각한 건강 문제로 정의하고 있다.<br>


비만은 비만으로 그치는 것이 아니라 각종 질병의 원인이 될 수 있으며, 정신적인 질병까지 유발할 수 있다.<br>
제2형 당뇨병, 이상지질혈증, 고혈압, 지방간, 담낭질환, 관상동맥질환(협심증, 심근경색증), 뇌졸중, 수면무호흡증, 통풍, 골관절염, 월경이상, 대장암, 유방암 등이 대표적인 비만과 관련된 질병이다.

# 일지
|Date|Description|Remark|
|:---:|:---|---|
|07_24|Start Project||
|07_24|[Data request](./Progress_img/README.md)|[질병관리본부](https://chs.cdc.go.kr/chs/rdr/rdrInfoProcessMain.do)|
|07_27|[Data Transformation 1](./EDA/1차_전처리)|1차 전처리 완료 (.txt -> .csv)|
|07_28|Theoretical background||
|ㄴ|[dependent variable, independent variable](./EDA/README.md)||
|07_29|[Find Common Columns](./data/원시자료_이용지침서)||
|ㄴ|[Pull Only Required Common Columns](./data/README.md)||
|ㄴ|[Data Transformation 2](./EDA/2차_전처리)|Apply common column |
|07_30|[Data Transformation 2](./EDA/2차_전처리)|2010 ~ 2014년까지 변환중 데이터의 문제점 발생|
|ㄴ|[Different data standards before and after 14's](https://github.com/cpprhtn/Obesity_prediction_Project/tree/master/data/Different_data%20_standards)|문제 해결 과정|
|07_31|[Data Transformation 2](./EDA/2차_전처리)|2차 전처리 완료|
|ㄴ|2010~2013년과 2014 이후의 결혼여부 칼럼명 다른거 수정|sod_02z1 -> sod_02z2|
