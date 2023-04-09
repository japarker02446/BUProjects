# CS555 Data Analysis and Visualization
# Homework1.R
# Jefferson Parker, japarker@bu.edu
# 20180703

# 1. Save the data to a .csv file and read it into R.
# The file was saved locally as CdifficileData.csv.
inputdir <- "C:/Users/jparker/Code/Input";
setwd(inputdir);
difi.data <- read.csv(file = "CdifficileData.csv", header = FALSE);

# The read.csv function automatically creates a data frame.
# Convert the data to an unnamed integer vector for convenience.
difi.data <- unname(unlist(difi.data));

# 2. Make a histogram of the duration of hospital days, binned by single
# days.  Lable the plot apporpriately.
hist(difi.data, 
		 breaks = 14, 
		 xlim = c(0,15),
		 main = "Distribution of C. dificile Hospital Stay Duration",
		 xlab = "Days",
		 ylab = "Frequency"
);

# Determine if there are outliers.
find.outliers <- function(x){
	fiveNum <- fivenum(x);
	firstQuartile <- fiveNum[2];
	thirdQuartile <- fiveNum[4];
	iqrVal <- fiveNum[4] - fiveNum[2];
	
	upperBound <- thirdQuartile + (1.5 * iqrVal);
	lowerBound <- firstQuartile - (1.5 * iqrVal);
	return(sort(x[x <= lowerBound | x >= upperBound]));
}

table(find.outliers(difi.data));

# 3. Find the mean, median and standard deviation, first and third
# quartiles, min, max.
summary(difi.data);
sd(difi.data);

# 4. Assume normal distribution with mean = 5 and sd = 3.
# a) What percentage of patients are in the hospital less than a week?
pnorm(7, mean = 5, sd = 3);

# b) For a sample n = 10, what is the probability a hospital stay is 
# more than 7 days?
#
# First, we use the provided information to find the Standard Error of the mean.
# Then we use this as the estimate of the population standard deviation to 
# calculate our probability.
se.xbar = 3/sqrt(10);
1 - pnorm(7, mean = 5, sd = se.xbar);
