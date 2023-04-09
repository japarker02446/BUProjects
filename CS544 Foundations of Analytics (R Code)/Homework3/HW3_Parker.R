# CS544, Summer 2018
# Jefferson Parker
# japarker@bu.edu
# Homework 3

# Initialize libraries
library(UsingR);

#####
# Part 1, primes data
# primes;
# help("primes");
primesdiff <- diff(primes);
primesdiff;
table(primesdiff);
barplot(table(primesdiff), col = rainbow(9), ylim = c(0,80));

#####
# Part 2, coins data
# coins;
# help("coins");

# a) Frequency by denomination.
table(coins$value);

# b) The coins data set is a table, convert it to a data frame and the 
# denominations from a factor to numeric.
# Multiply the number of coins per denomination to get the total value.
coins.df <- as.data.frame(table(coins$value));
coins.df$Var1 <- as.numeric(as.character(coins.df$Var1));
coins.df$total <- coins.df$Var1 * coins.df$Freq;
coins.df;

# c) Total value of all coins.
sum(coins.df$total);

# d) Barplot of the number of coins by year.
barplot(table(coins$year), col = "green", xlab = "Year", ylab = "No. Coins", las = 2);

#####
# Part 3, south data
# south;
# help("south");

# a) stem plot
stem(south);

# b) five number summary
fivenum(south);

# outlier boundaries
fivenum(south)[4] + (1.5 * (fivenum(south)[4] - fivenum(south)[2]));
fivenum(south)[2] - (1.5 * (fivenum(south)[4] - fivenum(south)[2]));

# Functions to identify outliers.
find.outliers <- function(x){
	fiveNum <-fivenum(x);
	firstQuartile <- fiveNum[2];
	thirdQuartile <- fiveNum[4];
	iqrVal <- fiveNum[4] - fiveNum[2];
	
	upperBound <- thirdQuartile + (1.5 * iqrVal);
	lowerBound <- firstQuartile - (1.5 * iqrVal);
	return (sort(x[x <= lowerBound | x >= upperBound]));
}
find.outliers(south);

# c) Horizontal boxplot labeled with five number summary values.
boxplot(south, horizontal = TRUE, xaxt = "n")
axis(side = 1, at = fivenum(south), labels = TRUE);

#####
# Part 4, pi2000 data
# pi2000;
# help("pi2000");

# a) Count of each digit 0 to 9
table(pi2000);

# b) Percentage of the frequency of digits 0 - 9
prop.table(table(pi2000)) * 100;

# c) histogram of the frequencies
hist(pi2000, col = "cyan");

#####
# Part 5, sports data
# a) Use cbind to create the matrix
sports <- cbind(c(25, 20), c(10, 40), c(15,30));

# b) set the row names
rownames(sports) <- c("Men", "Women");

# c) set the column names
colnames(sports) <- c("NFL", "NBA", "NHL");

# d) add dimension variables Gender and Sport
dim1 <- c("NFL", "NBA", "NHL");
dim2 <- c("Men", "Women");
dimnames(sports) <- list(Gender = dim2, Sport = dim1);
sports;

# e) show the marginal distributions for Gender and Sport
margin.table(sports, 1);
margin.table(sports, 2);

# f) add the margins to the data table
addmargins(sports);

# g) show the proportional data for Gender and Sport.  Interpret.
prop.table(sports, 1);
prop.table(sports, 2);

# h) USing appropriate (and intentionally stereotypical) colors, show the plots with legends:
# 	1. Mosaic plot for the data
# 	2. Barplots for Gender and Sport separately with bars side by side.
mosaicplot(
	t(margin.table(sports, c(1,2))), 
	color = c("deepskyblue", "pink"), 
	main = "Sports by Gender"
);

# Barplot, gender
barplot(
	margin.table(sports, 1), 
	beside = TRUE, 
	ylim = c(0,100), 
	col = c("deepskyblue", "pink")
);

# Barplot, sport
barplot(
	margin.table(sports, 2), 
	beside = TRUE, 
	ylim = c(0,60), 
	col = c("blue3", "darkgreen", "yellow")
);

#####
# Part 6, midsize data
# midsize;
# help("midsize");

# a) show the pairwise plots for all variables
pairs(midsize, las = 2);

#####
# Part 7, MLBattend data
# MLBattend;
# help("MLBattend");

# a) Extract the WINS for the teams BAL, BOS, DET, LA and PHI into vectors.
BAL <- subset(MLBattend, franchise == "BAL", select = wins);
BOS <- subset(MLBattend, franchise == "BOS", select = wins);
DET <- subset(MLBattend, franchise == "DET", select = wins);
LA <- subset(MLBattend, franchise == "LA", select = wins);
PHI <- subset(MLBattend, franchise == "PHI", select = wins);

# b) Create a data frame of five columns from the vectors in a)
# using the team names as column names.
wins <- as.data.frame(list(BAL, BOS, DET, LA, PHI),row.names = 1:dim(BAL)[1]);
colnames(wins) <- c("BAL","BOS","DET","LA","PHI");
wins;

# c) Show the boxplot of the data
boxplot(wins, col = c("orange", "red", "darkblue", "blue", "firebrick3"));

#####
# Part 8, House and Senate Data
# Names, years in office, party, State and
# 	District for House
# 	Term End for Senate
house <- read.csv('http://kalathur.com/house.csv', stringsAsFactors = FALSE);
senate <- read.csv('http://kalathur.com/senate.csv', stringsAsFactors = FALSE);

# a) How many house and senate members by party lines.
table(c(house$Party, senate$Party));

# b) Top 10 states, descending, by number of house members
sort(table(house$State), decreasing = TRUE)[1:10];

# c) Boxplot of house members per state and identify outlier states
boxplot(as.matrix(table(house$State)));

# Identify which states are outliers.
outvals <- boxplot(as.matrix(table(house$State)))$out;
statedf <- as.data.frame(table(house$State));
statedf[statedf$Freq %in% outvals, ];

# d) Average number of years served by party by house of Congress.
for (i in unique(house$Party)){
	print(sprintf ("%s %f", i, mean(house[house$Party == i,]$Years_in_office)));
}

for (i in unique(senate$Party)){
	print(sprintf ("%s %f", i, mean(senate[senate$Party == i,]$Years_in_office)));
}
