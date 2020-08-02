rm(list=ls())

library(MASS)
library(e1071)

setwd("/Users/cpprhtn/Desktop/git_local/Obesity_prediction_project")


read.csv("EDA/종속변수생성/b_10.csv",header = T,fileEncoding = "CP949") -> b_10
read.csv("EDA/종속변수생성/b_11.csv",header = T,fileEncoding = "CP949") -> b_11
read.csv("EDA/종속변수생성/b_12.csv",header = T,fileEncoding = "CP949") -> b_12
read.csv("EDA/종속변수생성/b_13.csv",header = T,fileEncoding = "CP949") -> b_13
read.csv("EDA/종속변수생성/b_14.csv",header = T,fileEncoding = "CP949") -> b_14
read.csv("EDA/종속변수생성/b_15.csv",header = T,fileEncoding = "CP949") -> b_15
read.csv("EDA/종속변수생성/b_16.csv",header = T,fileEncoding = "CP949") -> b_16
read.csv("EDA/종속변수생성/b_17.csv",header = T,fileEncoding = "CP949") -> b_17

names(b_14) <- names(b_10)
names(b_15) <- names(b_10)
names(b_16) <- names(b_10)
names(b_17) <- names(b_10)

naive_seoul = rbind(b_10,b_11,b_12,b_13,b_14,b_15,b_16,b_17)
str(naive_seoul)
for (i in 1:24) {
  naive_seoul[,i] <-factor(naive_seoul[,i]) 
  }
str(naive_seoul)
read.csv("Predict_Model/input_columns.csv",header = T, sep = ',') -> input
read.csv("Predict_Model/output_columns.csv",header = T,sep=',') -> output
read.csv("Predict_Model/Naive_Bayes/pre_output_bayes.csv",header = T,sep=',') -> pre_output


input_value = c(colnames(input))
output_value = c(colnames(output))
pre_value = c(colnames(pre_output))
form = as.formula(paste(paste(output_value, collapse = '+'),'~',paste(input_value, collapse = '+')))

train_data.lda=naiveBayes(form,data=naive_seoul)
pre=predict(train_data.lda,naive_seoul,type = 'raw')
dimnames(pre)=list(NULL,c(pre_value))
summary(pre)

pred_obs = cbind(naive_seoul,pre)
write.csv(pred_obs,'Predict_Model/Naive_Bayes/naive_Seoul.csv')
mean_seoul = read.csv('Predict_Model/Naive_Bayes/naive_Seoul.csv',header = T)
mean(mean_seoul$Underweight) -> Underweight
mean(mean_seoul$Normal) -> Normal
mean(mean_seoul$Obese) -> Obese
Name = c('Underweight','Normal','Obese')
Value = c(Underweight,Normal,Obese)
library(ggplot2)
df = data.frame(Name,Value)
ggplot(df, aes(x=Name,y=Value)) + geom_bar(stat='identity', fill='lightblue',colour='black') +
  ggtitle("Naive Bayes Classification Model") + theme(size = 16,plot.title = element_text(hjust = 0.5))






read.csv("EDA/종속변수생성/b_10.csv",header = T,fileEncoding = "CP949") -> b_10
read.csv("EDA/종속변수생성/b_11.csv",header = T,fileEncoding = "CP949") -> b_11
read.csv("EDA/종속변수생성/b_12.csv",header = T,fileEncoding = "CP949") -> b_12
read.csv("EDA/종속변수생성/b_13.csv",header = T,fileEncoding = "CP949") -> b_13
read.csv("EDA/종속변수생성/b_14.csv",header = T,fileEncoding = "CP949") -> b_14
read.csv("EDA/종속변수생성/b_15.csv",header = T,fileEncoding = "CP949") -> b_15
read.csv("EDA/종속변수생성/b_16.csv",header = T,fileEncoding = "CP949") -> b_16
read.csv("EDA/종속변수생성/b_17.csv",header = T,fileEncoding = "CP949") -> b_17

names(b_14) <- names(b_10)
names(b_15) <- names(b_10)
names(b_16) <- names(b_10)
names(b_17) <- names(b_10)

naive_seoul = rbind(b_10,b_11,b_12,b_13,b_14,b_15,b_16,b_17)
str(naive_seoul)
for (i in 1:24) {
  naive_seoul[,i] <-factor(naive_seoul[,i]) 
}
str(naive_seoul)

train_data.lda=naiveBayes(form,data=naive_seoul)
pre=predict(train_data.lda,naive_seoul,type = 'raw')
dimnames(pre)=list(NULL,c(pre_value))
summary(pre)



pred_obs = cbind(naive_seoul,pre)
write.csv(pred_obs,'Predict_Model/Naive_Bayes/naive_Seoul.csv')
mean_seoul = read.csv('Predict_Model/Naive_Bayes/naive_Seoul.csv',header = T)
mean(mean_seoul$Underweight)
mean(mean_seoul$Normal)
mean(mean_seoul$Obese)