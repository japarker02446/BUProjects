# CS555 Data Analysis and Visualization
# Homework3.R
# Jefferson Parker, japarker@bu.edu
# 20180723

# 1. Save the data to a local file and read into R.
inputDir <- "C:/Users/jparker/Code/Input";
setwd(inputDir);
fishmerc <- read.table(file = "fishmeal_mercury_data.txt", header = TRUE);

# 2. Genereate a scatterplot (labels and title).
# 	Use the plot to describe the fomr, direction and strength of any association.
plot(x = fishmerc$Count.FishMeals,
		 y = fishmerc$Mercury.mgPerGram,
		 pch = 20,
		 xlab = "Meals Containing Fish (weekly)",
		 ylab = "Mercury in Head Hair (mg/g)",
		 main = "Mercury Present in Fisherman's Hair"
);

# 3. Calculate the correlation coefficient.
r.fish <- cor(fishmerc$Count.FishMeals, fishmerc$Mercury.mgPerGram);
r.fish;

# 4. Find the least square regression line.
# Write the equation for the line and add it to the plot.
regLine <- lm(fishmerc$Mercury.mgPerGram ~ fishmerc$Count.FishMeals);
regLine;

abline(regLine);

# 5. What are the estimates for beta1 and beta0.
regLine$coefficients;

# 6. Calculate the ANOVA table.
# 	Formally test beta1 = 0 by F-test or t-test at alpha = 0.10.
anova(regLine);
#summary(aov(fishmerc$Mercury.mgPerGram ~ fishmerc$Count.FishMeals));
# While anova(lm(formula)) and (aov(formula)) generate the ANOVA table in different
# ways, the results are within rounding differences identical.

qf(1 - 0.1, 1, nrow(fishmerc)-2);

# Calculate the table for standard error of b1hat.
betaTable <- fishmerc;
colnames(betaTable) <- c("x", "y");

# Calculate the fitted value yhat with the regression coefficients.
betaTable$yhat <- regLine$coefficients[1] + (regLine$coefficients[2] * betaTable$x);

# Calculate the terms of the SE of beta1(hat)
betaTable$y.min.yhat <- betaTable$y - betaTable$yhat;
betaTable$y.min.yhat2 <- betaTable$y.min.yhat^2;

betaTable$x.min.xbar <- betaTable$x - mean(betaTable$x);
betaTable$x.min.xbar2 <- betaTable$x.min.xbar^2;
betaTable;

# Also calculate R^2.
r2.fish <- r.fish^2;
r2.fish;

# Also calculate the 90% confidence interval for beta1.
#  First, calculate the standard error for beta1hat.
sebeta1hat.top <- sqrt(sum(betaTable$y.min.yhat2/(nrow(betaTable)-2)));
sebeta1hat.bot <- sqrt(sum(betaTable$x.min.xbar2));
se.beta1hat <- sebeta1hat.top/sebeta1hat.bot;

# Next, find our 2-sided t-statistic
t.confint <- qt(0.90, df = nrow(betaTable) - 2);

# Then, calculate the bounds of the confidence interval.
regLine$coefficients[2] + (t.confint * se.beta1hat);
regLine$coefficients[2] - (t.confint * se.beta1hat);
