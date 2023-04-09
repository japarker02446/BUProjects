# CS544, Homework 2
# Jefferson Parker

# Initialize libraries and local functions:
library(prob);

bayes <- function (prior, likelihood) {
  numerators <- prior * likelihood;
  return (numerators / sum(numerators));
}

# Part 1.a, non-smoker lung disease
prior <- c(0.07, 0.93);
like <- c(0.1, 0.75);
bayes(prior, like);

# Part 1.b, political sales tax
prior <- c(0.4, 0.5, 0.1);
like <- c(0.7, 0.4, 0.2);
bayes(prior, like);

# Part 2.a, random variables
# Define function to calculate absolute value of the difference.
absdiff <- function(x){return(abs(x[1] - x[2]));}

S <- rolldie(2, makespace = TRUE);
S <- addrv(S, FUN = absdiff, name = "A");
S;

# Part 2.b., probabilty of Absolute difference having certain values.
Prob(S, A <= 2);
Prob(S, A >= 3);

# Part 2.c., show the marginal distribution of the Absolute diff (A).
marginal(S, vars = "A");

# Part 2.d., second random variable
# If the sum of values in X (should be two) is even return true, otherwise return false.
eventest <- function(x){
  if(((x[1] + x[2]) %% 2) == 0){
    return (TRUE);
  } else {return(FALSE);}
}

S <- addrv(S, FUN = eventest, name = "E");
Prob(S, E);
marginal(S, vars = "E");

# Part 3., Sum even numbers in the vector, two ways.
evensum <- function(data){
  sumtot = 0;
  for(i in data){
    if((data[i] %%2) == 0){sumtot <- sumtot + data[i];}
  }
  return(sumtot);
}

evensum2 <- function(data){
  return(sum(data[(data %% 2) == 0]));
}

test <- 1:50;
evensum(test);
evensum2(test);

# Part 4, R.
# Download the online data set.
dow <- read.csv('http://kalathur.com/dow.csv', stringsAsFactors = FALSE);

# a. Add a column of consecutive difference values.
dow$DIFF <- c(0, diff(dow$VALUE));

# b. How many days did the DOW close higher or lower than the previous day?
dim(dow[dow$DIFF > 0, ])[1];   #higher close
dim(dow[dow$DIFF < 0, ])[1];  #lower close

# c. Subset with at least a 400 point gain.
dow[dow$DIFF >= 400, ];

# d. Calculate the longest gaining streak of at least 100 points per day.
# Hint - use rle() function.
# Adapted additional code / suggestions from http://masterr.org/r/how-to-find-consecutive-repeats-in-r/
dow$RUN <- "N";
dow[dow$DIFF >= 100, ]$RUN <- "Y";

# Get the run length encoding values for any value in dow$RUN.
rl <- rle(dow$RUN);

# Find the start and end positions of runs of Y's
# Put these into a data frame with the length of the run.
myruns <- which(rl$values == "Y");
runs.lengths.cumsum <- cumsum(rl$lengths);
myends <- runs.lengths.cumsum[myruns];

newindex <- ifelse(myruns > 1, myruns - 1, 0);
mystarts <- runs.lengths.cumsum[newindex] + 1;
if(0 %in% newindex){mystarts <- c(1, mystarts);}  # Adjust for first run at start of the list.

mydex <- data.frame(matrix(c(mystarts, myends), ncol = 2, nrow = length(mystarts)));
mydex$diff <- mydex$X2 - mydex$X1;

# Finally, for the RUN with MAX LENGTH (max(mydex$diff)) - extract the INDEX for the START (X1)
# and END (X2) of the run in dow.
runstart <- mydex$X1[which(mydex$diff == max(mydex$diff))];
runend <- mydex$X2[which(mydex$diff == max(mydex$diff))];
dow[runstart:runend, ];
