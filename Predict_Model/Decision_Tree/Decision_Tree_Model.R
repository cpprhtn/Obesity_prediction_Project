rm(list=ls())

library(MASS)
library(party)
library(ggplot2)
setwd("/Users/cpprhtn/Desktop/git_local/Obesity_prediction_project")


read.csv("EDA/종속변수생성/b_10.csv",header = T,fileEncoding = "CP949") -> b_10
read.csv("EDA/종속변수생성/b_11.csv",header = T,fileEncoding = "CP949") -> b_11
read.csv("EDA/종속변수생성/b_12.csv",header = T,fileEncoding = "CP949") -> b_12
read.csv("EDA/종속변수생성/b_13.csv",header = T,fileEncoding = "CP949") -> b_13
read.csv("EDA/종속변수생성/b_14.csv",header = T,fileEncoding = "CP949") -> b_14
read.csv("EDA/종속변수생성/b_15.csv",header = T,fileEncoding = "CP949") -> b_15
read.csv("EDA/종속변수생성/b_16.csv",header = T,fileEncoding = "CP949") -> b_16
read.csv("EDA/종속변수생성/b_17.csv",header = T,fileEncoding = "CP949") -> b_17

dt_busan = rbind(b_10,b_11,b_12,b_13,b_14,b_15,b_16,b_17)

#다항의 decision tree model로 예층하기위해서 종속변수의 범주는 string format를 주기로 함
#1=G_underweight, 2=G_normal, 3=G_obesity
dt_busan[,"Multinomial"] <- 'G_obesity'
for (i in 1:109314){
  if (dt_busan$Obesity[i] == 1){
    dt_busan$Multinomial[i] <- 'G_underweight'
  }
  else if (dt_busan$Obesity[i] == 2){
    dt_busan$Multinomial[i] <- 'G_normal'
  }
}
str(dt_busan$Multinomial)
read.csv("Predict_Model/input_columns.csv",header = T, sep = ',') -> input
read.csv("Predict_Model/output_multinomial.csv",header = T,sep=',') -> output
input_value = c(colnames(input))
output_value = c(colnames(output))
form = as.formula(paste(paste(output_value, collapse = '+'),'~',paste(input_value, collapse = '+')))


i_ctree = ctree(form,dt_busan)
pre_Normal = sapply(predict(i_ctree,dt_busan,type='prob'),'[[',2)
pre_Obese = sapply(predict(i_ctree,dt_busan,type='prob'),'[[',3)
pre_Underweight = sapply(predict(i_ctree,dt_busan,type='prob'),'[[',1)
summary(pre_Normal)
summary(pre_Underweight)
