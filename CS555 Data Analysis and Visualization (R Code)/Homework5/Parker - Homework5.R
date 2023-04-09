# CS555 Data Analysis and Visualization
# Homework5.R
# Jefferson Parker, japarker@bu.edu
# 20180803

# Load libraries.
library(car);
library(lsmeans);

# Save the student data to a file and load to R.
inputDir <- "C:/Users/jparker/Code/Input";
setwd(inputDir);
studentData <- read.table(file = "studentIq.txt", header = TRUE, sep = "\t");

# 1. How many students are in each group.
#		Summarize the data relating to both test score and age by group.
aggregate(studentData, by = list(studentData$group), summary);
boxplot(age ~ group, data = studentData, main = "Age per Student Group");
boxplot(iq ~ group, data = studentData, main = "IQ per Student Group");

# 2. Do test scores vary by group?
# Critical F value
qf(0.05, 2, 42, lower.tail = FALSE);
testModel <- aov(iq ~ group, data = studentData);
summary(testModel);

# If the overall model is significant, perform pairwise testing.
# 	Note of confusion.  The homework says use Tukey's adjustment method but that is
# 	not an option for pairwise.t.test.  I am using both pairwise.t.test and TukeyHSD
# 	to check both methods.
pairwise.t.test(studentData$iq, studentData$group, p.adjust.method = 'bonferroni');
TukeyHSD(testModel);

# 3. Create the appropriate number of dummy variables for student group
# and re-run the one way ANOVA using the lm function.
# Set 'Chemistry student' as the reference group.
studentData$gC <- ifelse(studentData$group == 'Chemistry student', 1, 0);
studentData$gM <- ifelse(studentData$group == 'Math student', 1, 0);
studentData$gP <- ifelse(studentData$group == 'Physics student', 1, 0);

lineModel <- lm(iq ~ gM + gP, data = studentData);
summary(lineModel);

# 4. Re-do the one way ANOVA adjusting for age (ANCOVA).
Anova(lm(iq ~ group + age, data = studentData), type = 3);

# set our categorical variable options.
options(contrasts = c("contr.treatment", "contr.poly"));

# Measure pairwise differences between groups, accounting for differences in age.
lsmeans(lm(iq ~ group + age, data = studentData), pairwise ~ group, adjust = 'Tukey');

# Just checking
# install.packages("emmeans");
library(emmeans);
emmeans(lm(iq ~ group + age, data = studentData), pairwise ~ group, adjust = 'Tukey');
