# CS555 Data Analysis and Visualization
# Homework4.R
# Jefferson Parker, japarker.bu.edu
# 20180728

# 1. Save the data to .csv file and read into R for analysis.
setwd('C:/Users/jparker/Code/Input/');
canjobdata <- read.csv(file = "Canada_JobData.csv", header = TRUE);

# Remove extra periods from colname(s)
colnames(canjobdata) <- c("Job.Title", "Years.Education", "Income", "Perc.Women", "Prestige.Score");

# 2. Plot the assocation between Years of Education and Prestige Score
# 	Calculate the Correlation
plot(x = canjobdata$Years.Education, 
		 y = canjobdata$Prestige.Score, 
		 main = "Prestige by Years Education",
		 xlab = "Years of Education",
		 ylab = "Prestige Score", 
		 pch = 20
);

cor(canjobdata$Years.Education, canjobdata$Prestige.Score);


# 3. Perform a simple linear regression.
# 	Generate a residual plot.
# 
# Determine if the model assumptions were met.
# 1.	The relationship is linear without major outliers.
# 2.	The observations are INDEPENDENT.
# 3. 	The variation of the response around the regression line is CONSTANT.
# 4.	The residuals are NORMALLY DISTRIBUTED.
job.model <- lm(Prestige.Score ~ Years.Education, data = canjobdata);
job.resid <- resid(job.model);
plot(x = canjobdata$Years.Education, 
		 y = job.resid, 
		 xlab = "Years Education",
		 ylab = "Residual",
		 main = "Residuals, Prestige by Years Education",
		 pch = 20
);
abline(h = 0);
hist(job.resid);

# Are there any outliers or influence points?
# If so, identify them by ID and comment on their effect.
# 
# The influence.measures() function returns three lists.
# The second ($is.inf) contains six logical vectors of values,
# within this, the cov.r column marks the influencer values.
job.influence <- data.frame(influence.measures(job.model)$is.inf);
canjobdata[which(job.influence$cov.r),];

summary(job.model);
summary(lm(Prestige.Score ~ Years.Education, data = canjobdata[-41, ]));
summary(lm(Prestige.Score ~ Years.Education, data = canjobdata[-46, ]));
summary(lm(Prestige.Score ~ Years.Education, data = canjobdata[-53, ]));

# 4. Calculate the Least Squares Regression model to predicte Prestige
# 	from Education, Income and Percentage of Women.
prestige.model <- lm(Prestige.Score ~ Years.Education + Income + Perc.Women, data = canjobdata);
summary(prestige.model);

# Formally test whether these predictors are associated with Prestige 
# at alpha = 0.05.
anova(prestige.model);

# 5. Calculate the 95% Confidence intervals for significant variables.
# Reference: https://stat.ethz.ch/pipermail/r-help/2008-April/160538.html
# How to extract coefficient standard errors from a linear model.
prestige.coef <- data.frame(coef(summary(prestige.model)));
rownames(prestige.coef);
prestige.coef$upper.95 <- prestige.coef$Estimate + (prestige.coef$t.value * prestige.coef$Std..Error);
prestige.coef$lower.95 <- prestige.coef$Estimate - (prestige.coef$t.value * prestige.coef$Std..Error);
prestige.coef;

# 6. Generate a residuals plot showing the fitted values from teh regression against the residuals.
plot(x = prestige.model$fitted.values,
		 y = prestige.model$residuals,
		 xlab = "Fitted values",
		 ylab = "Residuals",
		 main = "Prestige Regression, Residuals vs Fits",
		 pch = 20
);
abline(h = 0);

# 7. Are there any outliers or influence points?
prestige.influence <- data.frame(influence.measures(prestige.model)$is.inf);
canjobdata[which(prestige.influence$cov.r),];
