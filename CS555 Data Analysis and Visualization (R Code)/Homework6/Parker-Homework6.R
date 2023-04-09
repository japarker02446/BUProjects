# CS555 Data Analysis and Visualization
# Homework6.R
# Jefferson Parker, japarker@bu.edu
# 20180806

# Load libraries
library(aod);
library(pROC);

# Load data
inputDir <- 'C:/Users/jparker/Code/Input';
setwd(inputDir);
tempData <- read.table(file = "heartTempBySex.txt", header = TRUE, stringsAsFactors = FALSE, sep = "\t");

# 1. We are interested in the proportion of body temperature greater than 98.6.
# 	Create a dichotomous body temperature variable to capture this.
tempData$temp_level <- ifelse(tempData$temp >= 98.6, 1, 0);

# 2. Summarize the data relating body temperature level by sex.
table(tempData$temp_level, tempData$sex, dnn = c("TempLevel", "Sex"));

# 3. Calculate the risk difference
# 
# Proportion(high temp & male) - Proportion(high temp & female);
(14/65) - (35/65);

# Test if the proportion(s) of people with higher temperature (a = 0.05) is 
# the same across males and females.
# 
# Males is first proportion (1,2).
prop.test(x = c(14, 35), n = c(65, 65), alternative = 'less', conf.level = 0.05, correct = FALSE);

# Do females have higher body temperatures than males?
# This is asking about the actual body temperatures of our sample, not the proportions, so we need
# ANOVA.
summary(aov(tempData$temp ~ as.factor(tempData$sex)));
pairwise.t.test(tempData$temp, as.factor(tempData$sex), p.adjust.method = 'none', alternative = 'greater');

# 4. Perform a logistic regression with sex as the only explanatory variable.
mSex <- glm(temp_level ~ sex, data = tempData, family = 'binomial');
summary(mSex);

# Odds Ratio and 95% Confidence Interval (1 unit difference)
exp(cbind(OR = coef(mSex), confint.default(mSex)));

# What is the c-statistic of the model?
# 	Generate the ROC curve to get AUC.
tempData$probSex <- predict(mSex, type = c("response"));
rSex <- roc(tempData$temp_level ~ tempData$probSex);
rSex;
plot.roc(rSex, print.auc = TRUE);
grid();

# 5. Perform a multiple logistic regression predicting body temperature level from sex and heart rate.
mBoth <- glm(temp_level ~ sex + Heart.rate, data = tempData, family = 'binomial');
summary(mBoth);

# What is the odds ratio for sex and heart rate (10 beat increase).
# CI = exp(beta +/- z(1 - alpha/2) + SE(beta) * proportion_difference)
rbind(
	# Sex
	cbind(
		OR = exp(summary(mBoth)$coefficients[2, 1]),
		'2.5 %' = exp((summary(mBoth)$coefficients[2, 1] - qnorm(0.975) * summary(mBoth)$coefficients[2, 2])),
		'97.5 %' = exp((summary(mBoth)$coefficients[2, 1] + qnorm(0.975) * summary(mBoth)$coefficients[2, 2]))
	),
	
	# Heart rate
	cbind(
		OR = exp(summary(mBoth)$coefficients[3, 1] * 10),
		'2.5 %' = exp((summary(mBoth)$coefficients[3, 1] - qnorm(0.975) * summary(mBoth)$coefficients[3, 2]) * 10),
		'97.5 %' = exp((summary(mBoth)$coefficients[3, 1] + qnorm(0.975) * summary(mBoth)$coefficients[3, 2]) * 10)
	)
);


# What is the c-statistic for this model.
tempData$probBoth <- predict(mBoth, type = c("response"));
rBoth <- roc(tempData$temp_level ~ tempData$probBoth);
rBoth;
plot.roc(rBoth, print.auc = TRUE);
grid();
