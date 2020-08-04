rm(list=ls())

library(MASS)
library(nnet)
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

logistic_busan = rbind(b_10,b_11,b_12,b_13,b_14,b_15,b_16,b_17)

read.csv("Predict_Model/input_columns.csv",header = T, sep = ',') -> input
read.csv("Predict_Model/output_columns.csv",header = T,sep=',') -> output
read.csv("Predict_Model/Logistic_Regression/pre_output_logistic.csv",header = T,sep=',') -> pre_output
input_value = c(colnames(input))
output_value = c(colnames(output))
pre_value = c(colnames(pre_output))
form = as.formula(paste(paste(output_value, collapse = '+'),'~',paste(input_value, collapse = '+')))

form
i_logistic = multinom(form, data=logistic_busan)

pre = predict(i_logistic, logistic_busan, type = 'probs')
dimnames(pre)=list(NULL,c(pre_value))
summary(pre)

pred_obs = cbind(logistic_busan, pre)
write.csv(pred_obs,'Predict_Model/Logistic_Regression/logistic_Busan.csv')
mean_b = read.csv('Predict_Model/Logistic_Regression/logistic_Busan.csv',header = T)
mean(mean_b$Underweight) -> Underweight
mean(mean_b$Normal) -> Normal
mean(mean_b$Obese) -> Obese
Name = c('Underweight','Normal','Obese')
Value = c(Underweight,Normal,Obese)
df = data.frame(Name,Value)
ggplot(df, aes(x=Name,y=Value)) + geom_bar(stat='identity', fill='lightyellow',colour='black') +
  ggtitle("Logistic Regression Model (Busan)") + 
  theme(plot.title = element_text(size = 25,hjust = 0.5)) +
  geom_text(aes(label=Value),vjust=2,colour='red', size=5)




read.csv("EDA/종속변수생성/s_10.csv",header = T,fileEncoding = "CP949") -> s_10
read.csv("EDA/종속변수생성/s_11.csv",header = T,fileEncoding = "CP949") -> s_11
read.csv("EDA/종속변수생성/s_12.csv",header = T,fileEncoding = "CP949") -> s_12
read.csv("EDA/종속변수생성/s_13.csv",header = T,fileEncoding = "CP949") -> s_13
read.csv("EDA/종속변수생성/s_14.csv",header = T,fileEncoding = "CP949") -> s_14
read.csv("EDA/종속변수생성/s_15.csv",header = T,fileEncoding = "CP949") -> s_15
read.csv("EDA/종속변수생성/s_16.csv",header = T,fileEncoding = "CP949") -> s_16
read.csv("EDA/종속변수생성/s_17.csv",header = T,fileEncoding = "CP949") -> s_17

logistic_seoul = rbind(s_10,s_11,s_12,s_13,s_14,s_15,s_16,s_17)

i_logistic = multinom(form, data=logistic_seoul)

pre = predict(i_logistic, logistic_seoul, type = 'probs')
dimnames(pre)=list(NULL,c(pre_value))
summary(pre)

pred_obs = cbind(logistic_seoul,pre)
write.csv(pred_obs,'Predict_Model/Logistic_Regression/logistic_Seoul.csv')
mean_s = read.csv('Predict_Model/Logistic_Regression/logistic_Seoul.csv',header = T)
mean(mean_s$Underweight) -> Underweight
mean(mean_s$Normal) -> Normal
mean(mean_s$Obese) -> Obese
Name = c('Underweight','Normal','Obese')
Value = c(Underweight,Normal,Obese)
df2 = data.frame(Name,Value)

ggplot(df2, aes(x=Name,y=Value)) + geom_bar(stat='identity', fill='lightyellow',colour='black') +
  ggtitle("Logistic Regression Model (Seoul)") + 
  theme(plot.title = element_text(size = 25,hjust = 0.5)) +
  geom_text(aes(label=Value),vjust=2,colour='red', size=5)
