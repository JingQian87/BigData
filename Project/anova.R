library(bigmemory)
data<-read.delim("~/Desktop/BigData_ProjectData/SPARCS-2017-Nobirth-Bias.csv")
sex<-as.factor(data$Gender)
race<-as.factor(data$Race)
age<-factor(data$Age.Group,order=TRUE,level=c('0 to 17', '18 to 29', '30 to 49', '50 to 69', '70 or Older'))
length<-as.numeric(data$Length.of.Stay)
area<-as.factor(data$Hospital.Service.Area)

y<-data$Total.Charges

fit1<-lm(y~sex+race+age+length+area)

anova(fit1)
anova(lm(y~race+sex+age+length+area))


