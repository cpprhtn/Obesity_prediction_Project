# 예측모델
## Naive Bayes Model
### 2010년부터 2017년도 전체의 평균 비만도 예측
#### 서울
![Naive Bayes Seoul](https://user-images.githubusercontent.com/63298243/89190192-10d2e700-d5dc-11ea-9074-1904060b2da8.jpeg)
#### 부산
![Naive Bayes Busan](https://user-images.githubusercontent.com/63298243/89190198-13cdd780-d5dc-11ea-8612-1b40a7d5bbb7.jpeg)

### 2010 ~ 2017년의 비만 증가 추세
#### 서울
![Seoul Obesity Increasing Trend](https://user-images.githubusercontent.com/63298243/89190653-b8e8b000-d5dc-11ea-9ca4-c5185a510f9a.jpeg)
```
> Normal
[1] 0.7642353 0.7712017 0.7354073 0.7439590 0.7468153 0.7145772 0.6752943 0.7073633
> Obese
[1] 0.2035307 0.1948460 0.1668739 0.1867129 0.1901972 0.2359329 0.2403387 0.2451464
> Underweight
[1] 0.03223392 0.03395231 0.09771882 0.06932812 0.06298752 0.04948993 0.08436703 0.04749022
```
#### 부산
![Busan Obesity Increasing Trend](https://user-images.githubusercontent.com/63298243/89190666-bc7c3700-d5dc-11ea-8433-f436d6b6a2d3.jpeg)
```
> Normal
[1] 0.6332506 0.6279165 0.6972318 0.7041154 0.7301775 0.6496043 0.6367185 0.6407566
> Obese
[1] 0.2541053 0.2296292 0.2236139 0.2126584 0.2110230 0.2502606 0.2946640 0.2686587
> Underweight
[1] 0.11264411 0.14245434 0.07915427 0.08322619 0.05879953 0.10013501 0.06861748 0.09058465
```

## Logistic Regression Model
### 2010년부터 2017년도 전체의 평균 비만도 예측
#### 서울
![Logistic Seoul](https://user-images.githubusercontent.com/63298243/89545450-5393f980-d83e-11ea-90ef-b07917b34941.jpeg)

#### 부산
![Logistic Busan](https://user-images.githubusercontent.com/63298243/89545459-57278080-d83e-11ea-9d94-1a4fcbd6bc35.jpeg)

### 2010 ~ 2017년의 비만 증가 추세
#### 서울
![Seoul Increasing Trend(logistic)](https://user-images.githubusercontent.com/63298243/89545476-5d1d6180-d83e-11ea-9295-af2641687ed8.jpeg)
```
> Normal
[1] 0.7105944 0.7077007 0.7169374 0.6959538 0.6973727 0.6901536 0.6834833 0.6918254
> Obese
[1] 0.2250311 0.2250836 0.2256180 0.2382097 0.2452157 0.2538347 0.2615263 0.2565936
> Underweight
[1] 0.06437446 0.06721571 0.05744458 0.06583647 0.05741166 0.05601165 0.05499039 0.05158097
```
#### 부산
![Busan Increasing Trend(logistic)](https://user-images.githubusercontent.com/63298243/89545467-5a227100-d83e-11ea-9835-1ad8c2156863.jpeg)
```
> Normal
[1] 0.7158554 0.7036180 0.6938409 0.7008706 0.6905793 0.6899230 0.6775589 0.6802011
> Obese
[1] 0.2215315 0.2295913 0.2357890 0.2334277 0.2406405 0.2464792 0.2588679 0.2598124
> Underweight
[1] 0.06261309 0.06679071 0.07037012 0.06570164 0.06878027 0.06359789 0.06357315 0.05998656
```

## Random Forest Model
### 2010년부터 2017년도 전체의 평균 비만도 예측
- 각 칼럼의 종류가 5개가 넘어서 오류가 뜸
- 원-핫 인코딩을 시도했으나 에러가 계속 나옴
```
b_10.rf = randomForest(form, data= b_10, forest=FALSE, importance=TRUE)
Warning message:
In randomForest.default(m, y, ...) :
  The response has five or fewer unique values.  Are you sure you want to do regression?
> pre = predict(b_10.rf,b_10, type='prob')
Error in predict.randomForest(b_10.rf, b_10, type = "prob") :
  'prob' or 'vote' not meaningful for regression
```
## Decision Tree Model
- Random Forest와 이하 동일
