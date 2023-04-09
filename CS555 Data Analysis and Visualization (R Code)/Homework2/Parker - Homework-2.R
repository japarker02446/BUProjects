# CS555 Data Analysis and Visualization
# Homework2.R
# Jefferson Parker, japarker@bu.edu
# 20180713

# Load the calorie intake data.
inputDir <- "C:/Users/jparker/Code/Input";
setwd(inputDir);
inCalories <- read.table(file = "CalorieIntakeForparticipants.txt", header = TRUE);
outCalories <- read.table(file = "CalorieIntakeForNon-participants.txt", header = TRUE);

# Add some labeling and annotation.
colnames(inCalories) <- "calories";
inCalories$Group <- rep("In", length(inCalories$calories));
colnames(outCalories) <- "calories";
outCalories$Group <- rep("Out", length(outCalories$calories));
calData <- rbind(inCalories, outCalories);

# 1. Summarize the data by participation status.
#   Use an appropriately labeled table and visualization.
#   Describe the distribution shape and comment on similarities.

summary(inCalories);
summary(outCalories);
boxplot(calories ~ Group, data = calData, main = "Calorie Intake by Study Participant Class");
hist(inCalories$calories, xlim = c(100,700), main = "Calorie Intake, Participants", xlab = "Calories");
hist(outCalories$calories, xlim = c(100,700), main = "Calorie Intake, Non-Participants", xlab = "Calories");

# 2. For participants, test if the mean is different (two sided) from 425 with alpha = 0.05.
#   Use the t-test because n < 30 and we do not know population standard deviation.
qt(0.05, length(inCalories$calories) -1, lower.tail = FALSE);
t.test(inCalories$calories, mu = 425, alternative = 'two.sided', conf.level = 0.05);

# 3. Calculate and interpret the 90% confidence interval for participants.
#   The confidence interval is independent of the test value, so we don't need to compare to any mean.
#   90% confidence level requires alpha = 0.1.
#   OR If calculating manually to make sure the t.test with mu = 0, use P = 0.45 (half the area).
t.test(inCalories$calories, alternative = 'two.sided', conf.level = 0.1);

xbar <- mean(inCalories$calories);
se.xbar <- sd(inCalories$calories)/sqrt(length(inCalories$calories));
t.crit <- qt(0.45, length(inCalories$calories)-1);

ci.upper <- xbar + (t.crit*se.xbar);
ci.lower <- xbar - (t.crit*se.xbar);

ci.lower;
ci.upper;

# 4. Test whether participants consumed MORE than non-participants at alpha = 0.05.
t.test(x = inCalories$calories, y = outCalories$calories, alternative = 'greater', conf.level = 0.05);

# 5. Test the data for the presence of outliers.
find.outliers <- function(x){
  fiveNum <- fivenum(x);
  firstQuartile <- fiveNum[2];
  thirdQuartile <- fiveNum[4];
  iqrVal <- fiveNum[4] - fiveNum[2];
  
  upperBound <- thirdQuartile + (1.5 * iqrVal);
  lowerBound <- firstQuartile - (1.5 * iqrVal);
  return(sort(x[x <= lowerBound | x >= upperBound]));
}

find.outliers(outCalories$calories);
find.outliers(inCalories$calories);
