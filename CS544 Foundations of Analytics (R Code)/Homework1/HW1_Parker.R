# CS544 Homework 1, Summer 2018
# Jefferson Parker (japarker@bu.edu)
# 
# Code supporting Homework Assignment number 1.

# Part 1, Rivers dataset
# Load the data set.
data(rivers);

# a: how many data points are in the data set
length(rivers);

# b: calculate the mean, median and mode.
mean(rivers);
median(rivers);

# Function to identify mode of the data set.
# From CS544 in class lecture.
find.mode <- function(x) {
	ux <- unique(x)
	ux[which.max(tabulate(match(x, ux)))]
}

find.mode(rivers);

# c: Compute the variand and standard deviation.
var(rivers);
sd(rivers);

# d: Calculate the five number summary, interquartile range and outliers.
fiveNum <- fivenum(rivers);
fiveNum;
fiveNum[4] -fiveNum[2];
IQR(rivers);

# Functions to identify outliers.
# First, calculate values for the first and third quartiles.
# Second, calcualte the interquartile range.
# Third, calculate the upper and lower value boundaries for outliers.
# Finally, return the list of outlier values.
find.outliers <- function(x){
	fiveNum <-fivenum(x);
	firstQuartile <- fiveNum[2];
	thirdQuartile <- fiveNum[4];
	iqrVal <- fiveNum[4] -fiveNum[2];
	
	upperBound <- thirdQuartile + iqrVal;
	lowerBound <- firstQuartile - iqrVal;
	return (sort(x[x <= lowerBound | x >= upperBound]));
}
find.outliers(rivers);

# e: Compute the standardized version (Z score) of the data.
standardize.values <- function(x){
	return ((x - mean(x) / sd(x)));
}
standardize.values(rivers);

# f: Convert the data to a matrix, two columns by 30 rows.
rivers.60 <- matrix(rivers[1:60], nrow = 2, ncol = 30);
rivers.60;

# g: (wihtout hard coding) display the first and last columns of the matrix.
# ... it's kind of impossible to not hard code the first column ...
rivers.60[,1];
rivers.60[,ncol(rivers.60)];

# h: Assign row and column names to the matrix.
# Row_n
# Length_n
rownames(rivers.60) <- paste("Row", 1:nrow(rivers.60), sep = "_");
colnames(rivers.60) <- paste("Length", 1:ncol(rivers.60), sep = "_");

####################################################################################
# Part 2, Johnson dataset
setwd("C:/Users/jparker/Code/Input");

# a: Load the data with years as row names and quarter titles as column names.
johnson <- read.csv(file = "johnson.csv", header = TRUE, row.names = 1);

# b: Show the summary of earnings per quarter.
summary(johnson);

# c: Add a column with annual earnings.
johnson$Yearly <- rowSums(johnson);

# d: Which were the best and worst performing years by total earings.
johnson[johnson$Yearly == max(johnson$Yearly), ];
johnson[johnson$Yearly == min(johnson$Yearly), ];

# e: Show all rows with Yearly greater than 20.
johnson[johnson$Yearly > 20, ];
