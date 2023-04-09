# CS544, Summer 2018
# Jefferson Parker
# japarker@bu.edu
# Homework 6

library(stringr);
library(tidyverse);

#####
# Part 1, Gettysburg Address data with stringr

file <- "http://kalathur.com/cs544/data/lincoln.txt";
words <- scan(file, what = character());

# a) detect and show all the words with punctuation symbols.
pattern <- ("\\b.+?[:punct:]");
gotpunct <- str_detect(words, pattern);
words[which(gotpunct)];

# b) Replace all punctuation symbols in words with an empty string.
# Make this the new words data.
pattern <- ("[:punct:]");
words <- str_replace(words, pattern, "");
words;

# c) Show the frequencies of the word lengths in the new words data.
# Plot the distribution of the frequencies.
table(str_length(words));
barplot(table(str_length(words)), 
				main = "Gettysburg Address",
				xlab = "String Length", 
				ylab = "Frequency", 
				ylim = c(0,60)
);
abline(h = 0);

# d) Which are the words with longest length.
words[str_length(words) == max(str_length(words))];

# e) Show all words that start with the letter 'p'.
pattern <- ("^p");
startp <- str_detect(words, pattern);
words[which(startp)];

# f) Show all words that end with the letter 'r'.
pattern <- ("r$");
endr <- str_detect(words, pattern);
words[which(endr)];

# g) Show all the words that start with the letter 'p' AND end with the letter 'r'.
pattern <- ("^p.+?r$");
startPendR <- str_detect(words, pattern);
words[which(startPendR)];

#####
# Part 2, US Average Temps data with tidyverse
# Download the data file and load it to a data frame.
# NOTE - REPLACE THE WORKING DIRECTORY PATH BELOW TO THE LOCAL PATH.
setwd("C:/Users/jparker/Code/Input");
tempdata <- as_tibble(read.csv(file = "usa_daily_avg_temps.csv"));

# a) Convert the data frame to a tibble and assign it to the variable usaDailyTemps.
usaDailyTemps <- as_tibble(tempdata);
glimpse(usaDailyTemps);

# b) What are the max temperatures for each year, plot the data appropriately.
usaDailyTemps %>% group_by(year) %>% summarise(maxtemp = max(avgtemp)) -> maxyears;
maxyears;

plot(maxyears, 
		 main = "Maximum Average Temperature", 
		 xlab = "Year", 
		 ylab = "Temperature", 
		 ylim = c(95,110),
		 las = 2
);

# c) What are the maximum temperatures for each state, plot the data appropriately.
usaDailyTemps %>% group_by(state) %>% summarise(maxtemp = max(avgtemp)) -> maxstates;
barplot(names.arg = as.character(maxstates$state), 
				height = maxstates$maxtemp,
				main = "Maximum Average Temperature", 
				ylab = "Temperature", 
				ylim = c(0,120),
				las = 2
);
abline(h=0);

# d) Filter the Boston data to a variable bostonDailyTemps
usaDailyTemps %>% filter(city == "Boston") -> bostonDailyTemps;
bostonDailyTemps;

# e) Show and plot the monthly average temperature for Boston.
bostonDailyTemps %>% group_by(month) %>% summarise(meantemp = mean(avgtemp)) -> bostonMonthlyTemp;
bostonMonthlyTemp;

# Add month names to our data.
getMonth <- function(x){return (month.name[x]);}
bostonMonthlyTemp %>% mutate(month.name = getMonth(month)) -> bostonMonthlyTemp;

barplot(names.arg = bostonMonthlyTemp$month.name,
				height = bostonMonthlyTemp$meantemp,
				main = "Average Monthly Temp", 
				ylab = "Temperature",
				las = 2
);
abline(h=0);
