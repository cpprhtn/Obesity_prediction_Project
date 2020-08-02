rm(list=ls())

library(MASS)
library(e1071)

setwd("/Users/cpprhtn/Desktop/git_local/Obesity_prediction_project/EDA")


read.csv("종속변수생성/b_10.csv",header = T,fileEncoding = "CP949") -> b_10
read.csv("종속변수생성/b_11.csv",header = T,fileEncoding = "CP949") -> b_11
read.csv("종속변수생성/b_12.csv",header = T,fileEncoding = "CP949") -> b_12
read.csv("종속변수생성/b_13.csv",header = T,fileEncoding = "CP949") -> b_13
read.csv("종속변수생성/b_14.csv",header = T,fileEncoding = "CP949") -> b_14
read.csv("종속변수생성/b_15.csv",header = T,fileEncoding = "CP949") -> b_15
read.csv("종속변수생성/b_16.csv",header = T,fileEncoding = "CP949") -> b_16
read.csv("종속변수생성/b_17.csv",header = T,fileEncoding = "CP949") -> b_17

names(b_14) <- names(b_10)
names(b_15) <- names(b_10)
names(b_16) <- names(b_10)
names(b_17) <- names(b_10)

naive_data = rbind(b_10,b_11,b_12,b_13,b_14,b_15,b_16,b_17)

read.csv("Predict_Model/input_region.csv",header = T,fileEncoding = "CP949") -> input
read.csv("Predict_Model/output_region.csv",header = T,sep=',') -> output
read.csv("Predict_Model/output_bayes.csv",header = T,sep=',') -> p_output


input_vars = c(colnames(input))
output_vars = c(colnames(output))
p_output_vars = c(colnames(p_output))
form = as.formula(paste(paste(output_vars, collapse = '+'),'~',paste(input_vars, collapse = '+')))

train_data.lda=naiveBayes(form,data=naive_data)
p=predict(train_data.lda,naive_data,type = 'raw')
dimnames(p)=list(NULL,c(p_output_vars))
summary(p)

pred_obs = cbind(naive_data,p)
write.csv(pred_obs,'naive_Seoul.csv')
m_data = read.csv('obesity_naive.csv',header = T)
mean(m_data$Underweight)
mean(m_data$Normal)
mean(m_data$Obese)

