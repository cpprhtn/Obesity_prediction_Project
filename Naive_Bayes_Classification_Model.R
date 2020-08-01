rm(list=ls())

library(MASS)
library(e1071)

setwd("/Users/cpprhtn/Desktop/git_local/Obesity_prediction_project/EDA/2차_전처리")
read.csv("b_10.csv",header = T,fileEncoding = "CP949") -> tdata

#비만 유뮤 칼럼 제작

tdata
