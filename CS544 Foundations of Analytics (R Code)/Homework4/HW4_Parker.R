# CS544, Summer 2018
# Jefferson Parker
# japarker@bu.edu
# Homework 4

# Initialize libraries
library(prob);

#####
# Part 1, Binomial Distribution
# For a pitcher in baseball with a p chance of getting a strike out, for the
# next n batters, what is the probability and lot the CDF for the listed probability.

# the plotcdf function makes a CDF plot for the binomial
# distribution for probabilty p and size n.
plotcdf <- function(n, p, title){
	pmf <- dbinom(0:n, size = n, prob = p);
	cdf = c(0, cumsum(pmf));
	cdfplot = stepfun(0:n, cdf);
	plot(cdfplot, 
			 verticals = FALSE, 
			 pch = 16,
			 main = title, 
			 xlab = "x", 
			 ylab = "CDF"
	);
}

# a - b: 50%
n <- 6;
p <- 0.5;
dbinom(6, size = n, prob = p);
percLabel <- paste0("Pitching CDF at ", p * 100,"%");
plotcdf(n, p, percLabel);

# c: 70%
n <- 6;
p <- 0.7;
dbinom(6, size = n, prob = p);
percLabel <- paste0("Pitching CDF at ", p * 100,"%");
plotcdf(n, p, percLabel);

# d: 30%
n <- 6;
p <- 0.3;
dbinom(6, size = n, prob = p);
percLabel <- paste0("Pitching CDF at ", p * 100,"%");
plotcdf(n, p, percLabel);

#####
# Part 2, Binomial Distribution
# 80% of flights arrive on time.

# a, Probability that four of the next 10 flights arrive on time.
n <- 10;
p <- 0.8;

sum(dbinom(3:9, size = n, prob = p));

# b: Probability of four or fewer flights arriving on time, of 10.
pbinom(4, size = n, prob = p);

# c: PRobability distribution of 10 flights arriving on time.
dbinom(0:n, size = n, prob = p);

# d: Plot the PMF and CDF for the next 10 flights.
percLabel <- paste0("Flight CDF at ", p * 100,"%");
plotcdf(n, p, percLabel);

# Function to plot PMF as spike plot.
plotpmf <- function(n, p, title){
	heights <- dbinom(0:n, size = n, prob = p);
	plot(0:n, 
			 heights, 
			 type = "h",
			 main = title, 
			 xlab = "x", 
			 ylab = "PMF"
	);
	points(0:n, heights, pch = 16);
}

percLabel <- paste0("Flight PMF at ", p * 100, "%");
plotpmf(n, p, percLabel);

#####
# Part 3, Poisson Distribution
# AVerage of 10 cars between 3:00 - 4:00 PM.

l = 10;

# a, probability of exactly 3 cars.
dpois(3, lambda = l);

# b, probability of serving at least 3 cars...
1 - dpois(3, lambda = l);

# c, probability of serving 2-5 cars (inclusive)
ppois(5, lambda = l) - ppois(2, lambda = l);

# d, Calculate and Plot the PMF for the first 20 cars.
pmf <- dpois(0:20, lambda = l);
pmf;

plot(0:20,
		 pmf,
		 type = "h",
		 xlab = "x",
		 ylab = "PMF"
);
abline(h = 0);

#####
# Part 4, Uniform Distribution
# Exams are scored on a uniform distribution from 60 - 100 inclusive.

# a, What is the probability of scoring 60, 80 or 100.
dunif(60, min = 60, max = 100);
dunif(80, min = 60, max = 100);
dunif(100, min = 60, max = 100);

# b, What is the mean and standard deviation
(60 + 100)/2;
(sqrt((60 + 100)^2)/12);

# c, What is the probability of scoring at MOST 70
punif(70, min = 60, max = 100);

# d, Probability of scoring GREATER than 80 (use lower.tail)
punif(80, min = 60, max = 100, lower.tail = FALSE);

# e, What is the probability of scoring between 90 - 100 (inclusive)
punif(100, min = 60, max = 100) - punif(90, min = 60, max = 100);

#####
# Part 5, Normal Distribution
# Theme park spending.  Mean = 100, SD = 10.
mu <- 100;
sig <- 10;
spend <- seq(0, 200, 0.1);

# a, PDF plot showing the distribution 3 SD around the mean.
pdf <- dnorm(spend, mean = mu, sd = sig);
plot(spend, pdf, type = "l", col = "cyan", xlim = c(70, 130));

# b, Probability that a random visitor will spend more than 120.
1 - pnorm(120, mean = mu, sd = sig);

# c, Probability that a random visitor will spend 80 - 90 inclusive
pnorm(90, mean = mu, sd = sig) - pnorm(80, mean = mu, sd = sig);

# d, Probability of spending within one, two or three SD.
# ASSUMPTION - this is +/- N SD around the MEAN, it was not
# clear from the question.
pnorm(mu + 1*sig, mean = mu, sd = sig) - pnorm(mu - 1*sig, mean = mu, sd = sig);
pnorm(mu + 2*sig, mean = mu, sd = sig) - pnorm(mu - 2*sig, mean = mu, sd = sig);
pnorm(mu + 3*sig, mean = mu, sd = sig) - pnorm(mu - 3*sig, mean = mu, sd = sig);

# e, Value covering the middle (around the mean) 90% of money spent.
upper90 <- qnorm(0.9, mean = mu, sd = sig);
upper90;
mu - (upper90 - mu);

# f, Plot of 10,000 visitors
y <- round(rnorm(1000, mean = mu, sd = sig));
plot(table(y), type = "h", col = "red");

#####
# Part 6, Exponential Distribution
# Receives calls at 18 / hour

# a, Probability of next call within 2 min
pexp(2/60, rate = 18);

# b, Probability of next call within 5 min
pexp(5/60, rate = 18);

# c, Probability of next call within 2 - 5 min (inclusive)
pexp(5/60, rate = 18) - pexp(2/60, rate = 18);

# d, CDF
x <- seq(0, 1, by = 1/60);
cdf <- pexp(x, rate = 18);
plot(x, cdf, type = "l", col = "red");
