rm(list=ls())

library(MASS)
library(e1071)
library(ggplot2)
library(caret)
library(kernlab)
setwd("/Users/cpprhtn/Desktop/git_local/Obesity_prediction_project")


read.csv("EDA/종속변수생성/b_10.csv",header = T,fileEncoding = "CP949") -> b_10
read.csv("EDA/종속변수생성/b_11.csv",header = T,fileEncoding = "CP949") -> b_11
read.csv("EDA/종속변수생성/b_12.csv",header = T,fileEncoding = "CP949") -> b_12
read.csv("EDA/종속변수생성/b_13.csv",header = T,fileEncoding = "CP949") -> b_13
read.csv("EDA/종속변수생성/b_14.csv",header = T,fileEncoding = "CP949") -> b_14
read.csv("EDA/종속변수생성/b_15.csv",header = T,fileEncoding = "CP949") -> b_15
read.csv("EDA/종속변수생성/b_16.csv",header = T,fileEncoding = "CP949") -> b_16
read.csv("EDA/종속변수생성/b_17.csv",header = T,fileEncoding = "CP949") -> b_17


data = rbind(b_10,b_11,b_12,b_13,b_14,b_15,b_16,b_17)

read.csv("Predict_Model/input_columns.csv",header = T, sep = ',') -> input
read.csv("Predict_Model/output_columns.csv",header = T,sep=',') -> output

input_value = c(colnames(input))
output_value = c(colnames(output))
form = as.formula(paste(paste(output_value, collapse = '+'),'~',paste(input_value, collapse = '+')))

svm.model = svm(form, data= data, kernel='radial')
summary(svm.model)
pre = predict(svm.model,data,type=prob)
p_Underweight=pre


write.csv(pred_obs,'Predict_Model/svm_Busan.csv')
mean_b = read.csv('Predict_Model/svm_Busan.csv',header = T)
mean(mean_b$p_Underweight)