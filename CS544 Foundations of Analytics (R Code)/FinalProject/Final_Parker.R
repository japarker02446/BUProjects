# CS544 Final Project
# Jefferson Parker
# japarker@bu.edu
# 
# Data source, kaggle.com
# https://www.kaggle.com/uciml/breast-cancer-wisconsin-data/data
# 
# The data was downloaded and saved to a local directory as a .csv file.

# Load libraries for analysis
library(prob);
library(sampling);

# Initialize local function to identify outliers.
find.outliers <- function(x){
  fiveNum <-fivenum(x);
  firstQuartile <- fiveNum[2];
  thirdQuartile <- fiveNum[4];
  iqrVal <- fiveNum[4] - fiveNum[2];
  
  upperBound <- thirdQuartile + (1.5 * iqrVal);
  lowerBound <- firstQuartile - (1.5 * iqrVal);
  return (sort(x[x <= lowerBound | x >= upperBound]));
}

###############################################################################
# Read the data file
setwd("C:/Users/Jefferson/Code/Input");
kagdata <- read.csv(file = "data.csv", header = TRUE, stringsAsFactors = FALSE);

# Remove the empty character column from the data file.
kagdata$X <- NULL;

# Look at the data
summary(kagdata);

# Create a categorical variable, id.nchar, which counts the number of characters
# in the ID variable.  It is my hypothesis that the number of characters is
# meaningful, either indicating a time of patient intake or a research center
# location.
kagdata$id.nchar <- nchar(kagdata$id);

# What is the frequency of diagnosis by ID.NChar?
# Use both a two-way table and a bar-plot.
table(kagdata$diagnosis, kagdata$id.nchar);

barplot(
  table(kagdata$diagnosis, kagdata$id.nchar),
  beside = TRUE,
  ylim = c(0,250),
  main = "Cases by ID Char Length",
  xlab = "ID.NCHAR",
  ylab = "Cases",
  legend = c("Benign", "Malignant")
);
abline(h = 0);

# From the data summary, the 'area_mean' variable looks like it 
# contains outliers.
# Use a histogram and boxplot to show the relationship of the data.
hist(kagdata$area_mean);
abline(h = 0);
boxplot(kagdata$area_mean);

# Question, is there a difference in area_mean by diagnosis?
boxplot(area_mean ~ diagnosis, 
        data = kagdata, 
        xlab = "Diagnosis",
        ylab = "Area Mean"
);

# What are the outlier values for each diagnosis group?
find.outliers(kagdata$area_mean[kagdata$diagnosis == "B"]);
find.outliers(kagdata$area_mean[kagdata$diagnosis == "M"]);

# Is there any interaction between ID.NChar and Diagnosis?
boxplot(area_mean ~ id.nchar + diagnosis, 
        data = kagdata, 
        xlab = "ID.NChar and Diagnosis",
        ylab = "Area Mean"
);

###############################################################################
# Data distribution, sampling and the Central Limit Theorem.
# The texture_mean variable measures the standard deviation of
# greyscale values from sample images.
hist(kagdata$texture_mean);
mean(kagdata$texture_mean);
sd(kagdata$texture_mean);

# Draw 200 samples of size two.  Show the histogram of the densities of the 
# sample means.  Compute the mean and standard deviation of the sample means.
samples <- 200;
sample.size <- 2;

# Generate a numeric array to hold the sample means.
xbar2 <- numeric(samples);

# Randomly select five values from the query data set.
# Calculate the mean of the five number sample
for(i in 1:samples){
  sample <- kagdata$texture_mean[runif(sample.size, min = 1, max = nrow(kagdata))];
  xbar2[i] <- mean(sample);
}
hist(xbar2, main = paste0("Mean Texture_mean ", sample.size), xlab = "Mean", ylab = "Frequency");
mean(xbar2);
sd(xbar2);

# Draw 200 samples of size 5.  Show the histogram of the densities of the 
# sample means.  Compute the mean and standard deviation of the sample means.
samples <- 200;
sample.size <- 5;

# Generate a numeric array to hold the sample means.
xbar5 <- numeric(samples);

# Randomly select five values from the query data set.
# Calculate the mean of the five number sample
for(i in 1:samples){
  sample <- kagdata$texture_mean[runif(sample.size, min = 1, max = nrow(kagdata))];
  xbar5[i] <- mean(sample);
}
hist(xbar5, main = paste0("Mean Texture_mean ", sample.size), xlab = "Mean", ylab = "Frequency");
mean(xbar5);
sd(xbar5);

# Draw 200 samples of size 10.  Show the histogram of the densities of the 
# sample means.  Compute the mean and standard deviation of the sample means.
samples <- 200;
sample.size <- 10;

# Generate a numeric array to hold the sample means.
xbar10 <- numeric(samples);

# Randomly select five values from the query data set.
# Calculate the mean of the five number sample
for(i in 1:samples){
  sample <- kagdata$texture_mean[runif(sample.size, min = 1, max = nrow(kagdata))];
  xbar10[i] <- mean(sample);
}
hist(xbar10, main = paste0("Mean Texture_mean ", sample.size), xlab = "Mean", ylab = "Frequency");
mean(xbar10);
sd(xbar10);

# Draw 200 samples of size 20.  Show the histogram of the densities of the 
# sample means.  Compute the mean and standard deviation of the sample means.
samples <- 200;
sample.size <- 20;

# Generate a numeric array to hold the sample means.
xbar20 <- numeric(samples);

# Randomly select five values from the query data set.
# Calculate the mean of the five number sample
for(i in 1:samples){
  sample <- kagdata$texture_mean[runif(sample.size, min = 1, max = nrow(kagdata))];
  xbar20[i] <- mean(sample);
}
hist(xbar20, main = paste0("Mean Texture_mean ", sample.size), xlab = "Mean", ylab = "Frequency");
mean(xbar20);
sd(xbar20);

###############################################################################
# Sampling Methods
# What is the proportion of each ID.NChar in the entire population?
prop.table(table(kagdata$id.nchar));

# For a sample size of 20:
sample.size <- 20;

# Using Simple Random Sampling WithOut Replacment,
# Show the sample, frequency of each ID.NChar and the
# percent of each with respect to the ENTIRE dataset.
sample <-srswor(sample.size, nrow(kagdata));
kagdata.s1 <- kagdata[sample != 0, ];
#kagdata.s1;

table(kagdata.s1$id.nchar);
prop.table(table(kagdata.s1$id.nchar));

# Use systematic sampling, show the frequency of each 
# ID.NChar and the percentage of these relative to the
# ENTIRE dataset.
N <- nrow(kagdata);
n <- sample.size;
k <- floor(N/n);
r <- sample(k, 1);

# Select the kth item from each Grouping of n items.
sample <- seq(r, by = k, length = n);
kagdata.s2 <- kagdata[sample, ];
#kagdata.s2;

# Determine the frequency and percentage of each
# ID.NChar in this sample.
table(kagdata.s2$id.nchar);
prop.table(table(kagdata.s2$id.nchar));
