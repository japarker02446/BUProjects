# CS544, Summer 2018
# Jefferson Parker
# japarker@bu.edu
# Homework 5

# Initialize libraries
library(prob);
library(sampling);

#####
# Part 1, Central Limit Theorem

# For the sequence 1 - 20, show the following plots in 1 row:
par(mfrow = c(1,3));
seq <- 1:20;

# a) plot the histogram of densities for the distribution.
hist(seq, freq = FALSE);

# b) Using all samples of size 2, plot the 
# histogram of the densities of sample means.
seq2 <- combn(seq, 2);
xbar2 <- apply(seq2, 2, FUN = mean);
hist(xbar2, freq = FALSE, ylim = c(0, 0.1));

# c) Using all samples of size 5, plot the
# histogram of the densities of sample means.
seq5 <- combn(seq, 5);
xbar5 <- apply(seq5, 2, FUN = mean);
hist(xbar5, freq = FALSE, xlim = c(0,20), ylim = c(0, 0.2));

# Restore R to default setting of one plot per window.
par(mfrow = c(1,1));

# d) compare the means and standard deviations of the three distributions.
mean(seq);
mean(xbar2);
mean(xbar5);
sd(seq);
sd(xbar2);
sd(xbar5);

#####
# Part 2, Central Limit Theoerm - queries.csv data file.
# Read the online data table of number of queries in Google per day for one year (365 days).
query <- read.table("http://kalathur.com/cs544/data/queries.csv", header = TRUE);

# a) Show the histogram of the distribution of number of queries.
# Calculate the mean and standard deviation of the number of queries.
hist(query$queries, ylim = c(0,50), main = "Google queries per day", xlab = "Count", ylab = "Frequency");
mean(query$queries);
sd(query$queries);

# b) Draw 1000 samples of size five.  Show the histogram of the densities of the 
# sample means.  Compute the mean and standard deviation of the sample means.
samples <- 1000;
sample.size <- 5;

# Generate a numeric array to hold the sample means.
xbar5 <- numeric(samples);

# Randomly select five values from the query data set.
# Calculate the mean of the five number sample
for(i in 1:samples){
	sample <- query$queries[runif(sample.size, min = 1, max = nrow(query))];
	xbar5[i] <- mean(sample);
}
hist(xbar5, main = "Mean number of queries from five days", xlab = "Mean", ylab = "Frequency");
mean(xbar5);
sd(xbar5);

# c) Draw 1000 samples of size 20.  Show the histogram of the densities of the 
# sample means.  Compute the mean and standard deviation of the sample means.
samples <- 1000;
sample.size <- 20;

# Generate a numeric array to hold the sample means.
xbar20 <- numeric(samples);

# Randomly select five values from the query data set.
# Calculate the mean of the five number sample
for(i in 1:samples){
	sample <- query$queries[runif(sample.size, min = 1, max = nrow(query))];
	xbar20[i] <- mean(sample);
}
hist(xbar20,main = "Mean number of queries from 20 days", xlab = "Mean", ylab = "Frequency");
mean(xbar20);
sd(xbar20);

#####
# Part 3, Central Limit Theorem with Negative Binomial Distribution.
s <- 5;			# size
p <- 0.5;		# probability

# a) Generate 1000 random numbers from this distribution, show the barplot 
# with the proportions of the distinct values of this distribution.
seq <- rnbinom(0:1000, size = s, prob = p);
barplot(table(seq), main = "Negative Binomial Values", xlab = "values", ylab = "frequencies");
abline(h = 0);

# b) For sample sizes of 10, 20, 30 and 40, generate data for 5000 samples
# Show histograms of the densities of their means in a 2 x 2 layout.
samples <- 5000;
par(mfrow = c(2,2));

# Generate a numeric array to hold the sample means.
xbar <- numeric(samples);

# Plot the histogram of the densities of sample means.
for(sample.size in c(10, 20, 30, 40)){
	for(i in 1:samples){xbar[i] <- mean(rnbinom(sample.size, size = s, prob = p));}
	hist(
		xbar, prob = TRUE, xlim = c(0,10),
		main = paste0("Sample Size ", sample.size), 
		xlab = "xbar", 
		ylab = "Density"
	);
	
	print(paste0("Mean of sample size ", sample.size, " is ", mean(xbar)));
	print(paste0("SD of sample size ", sample.size, " is ", sd(xbar)));
}

par(mfrow = c(1,1));

# c) Compare the means and standard deviations of data from a nad b.
seq <- rnbinom(0:1000, size = s, prob = p);
print(paste0("Mean of sample size 5 is ", mean(seq)));
print(paste0("SD of sample size 5 is ", sd(seq)));

#####
# Part 4, Sampling
# Using the MU284 data set in the sampling package with a sample size of 20 for each of the following:
data(MU284);
sample.size <- 20;

# a) Using Simple Random Sampling WithOut Replacment,
# Show the sample, frequency of each (REG)ion and the
# percent of each with respect to the ENTIRE dataset.
sample <-srswor(sample.size, nrow(MU284));
MU284.s1 <- MU284[sample != 0, ];
MU284.s1;

table(MU284.s1$REG);
prop.table(table(MU284.s1$REG));
prop.table(table(MU284$REG));

# b) Use systematic sampling, show the frequency of each 
# (REG)ion and the percentage of these relative to the
# ENTIRE dataset.
N <- nrow(MU284);
n <- sample.size;
k <- floor(N/n);
r <- sample(k, 1);

# Select the kth item from each Grouping of n items.
sample <- seq(r, by = k, length = n);
MU284.s2 <- MU284[sample, ];
MU284.s2;

# Determine the frequency and percentage of each
# REGion in this sample.
table(MU284.s2$REG);
prop.table(table(MU284.s2$REG))

# c) Calculate the inclusion probabilities using the S82 variable.
# Using these, show the sample using Systematic Sampling.
# Show the frequences and percentages of the total for each REGion.
pik <- inclusionprobabilities(MU284$S82, sample.size);

sample <- UPsystematic(pik);
MU284.s3 <- MU284[sample != 0, ];
MU284.s3;

table(MU284.s3$REG);
prop.table(table(MU284.s3$REG));
prop.table(table(MU284$REG));

# d) Order the data by the REG variable.
# Draw a stratified sample using proportional sizes based on the REG variable.
# Show the frequencies for each region.
# Show the percentages of these with respect to the entire data set.
MU284.o <- MU284[order(MU284$REG), ];

# Calculate the stratum proportions of each REGion.
freq <- table(MU284.o$REG);
sizes <- sample.size * freq / sum(freq);

# Select the stratified sample, proportional to the Region
sample <- strata(MU284.o, stratanames = c("REG"), size = sizes, method = "srswor", description = TRUE);

# Show the frequencies and percentage of each region relative
# to the entire data set.
table(sample$REG);
MU284.s4 <-getdata(MU284.o, sample);
MU284.s4;

table(MU284.s4$REG);
prop.table(table(MU284.s4$REG));
prop.table(table(MU284$REG));

# e) Compare the means of the RMT85 variable for the four above samples.
mean(MU284$RMT85);
mean(MU284.s1$RMT85);
mean(MU284.s2$RMT85);
mean(MU284.s3$RMT85);
mean(MU284.s4$RMT85);
