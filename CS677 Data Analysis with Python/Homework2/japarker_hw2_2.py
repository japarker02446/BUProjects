# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: March 29, 2022
Homework Problem 2.2

Read historical stock data (PFE, SPY) and PREDICT label for gain or loss days.
"""
import numpy as np
import pandas as pd
import os
import operator

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW2')

# Import helper functions to stock data from file.
from JparkerHw2Helper import *

# Define constant values for default probabilities based on values from Q1.
PFE_DEFAULT = '+'
SPY_DEFAULT = '+'

# Load the data for PFE (Pfizer Inc).
# load_ticker() returns a list of lists including:
#   Datestamp,
#   Year
#   Numeric day of week
#   Adjusted closing price
#   Percent day return

# Load the data to a pandas DataFrame
# Sort the list by date.

# Assign a "TrueLabel" column based on PercentGains.
#   '+' for postive gains
#   '-' for losses
pfe_df = pd.DataFrame(JparkerHw2Helper.load_ticker('PFE'), \
                        columns= ['Date','Year','DayOfWeek','Adj.Cloose',\
                                  'PercentGain'])
pfe_df = pfe_df.sort_values('Date')
pfe_df['TrueLabel'] = np.where(pfe_df['PercentGain'] < 0, '-', '+')

# Question 2.1
# Predict labels in years 4 and 5 based on True Labels in years 1 - 3.
#
# First, extract the true labels from years 1 - 3 as a text string (see Q1).
pfe_train = pfe_df.loc[(pfe_df['Year'].isin([2016, 2017, 2018]))]
pfe_train_str = pfe_train['TrueLabel'].to_string(index = False).replace('\n','')

# Quantify each substring in pfe_train_str of length 3, 4 and 5 in a dict, the
# substring value will be the key.
pfe_train_dict = dict()
for i in range(len(pfe_train_str)):
    if pfe_train_str[i:i + 3] in pfe_train_dict:
        pfe_train_dict[pfe_train_str[i:i + 3]] += 1
    else:
        pfe_train_dict[pfe_train_str[i:i + 3]] = 1
    if pfe_train_str[i:i + 4] in pfe_train_dict:
        pfe_train_dict[pfe_train_str[i:i + 4]] += 1
    else:
        pfe_train_dict[pfe_train_str[i:i + 4]] = 1
    if pfe_train_str[i:i + 5] in pfe_train_dict:
        pfe_train_dict[pfe_train_str[i:i + 5]] += 1
    else:
        pfe_train_dict[pfe_train_str[i:i + 5]] = 1

# Calculate the probability of each substring in pfe_train_dict.
# REFERENCE: https://www.geeksforgeeks.org/count-of-sub-strings-of-length-n-\
#   possible-from-the-given-string/#:~:text=Approach%3A%20The%20count%20of%20\
#   sub,length%20of%20the%20given%20string.
for key in pfe_train_dict:
    pfe_train_dict[key] = pfe_train_dict[key] / (len(pfe_train_str) - len(key) + 1)

# Prediction process:
# For a day d, predict the label for day d + 1 based on the majority label
# following the pattern of hyper-parameter W, the true label "word" s of length
# W (W including day d) for all W = 2,3,4.
#
# We need to predict on W = 2,3,4, these are going to be overlapping ...
# NOTE - In order to predict DAY 0 we need to look at W from the end of year 3.
# Reset the dataframe index for safety.
pfe_test = pfe_df.loc[(pfe_df['Year'].isin([2019,2020]))]
pfe_test = pd.concat([pfe_train.tail(3), pfe_test])
pfe_test = pfe_test.reset_index(drop = True)

# Day 1 is the beginning of 2019
start_day = min(pfe_test.index[pfe_test['Year'] == 2019])

# First construct the strings for W = 2,3,4 from years 4 and 5.
# This isn't really a necessary step, but it's useful to see what is being
#   captured as the W strings and make sure it's being done correctly, cuz
#   honestly this is confusing.
for i in range(start_day, pfe_test.shape[0]):
    pfe_test.loc[i,'s2'] = str(pfe_test.loc[i-1, 'TrueLabel'] + \
                             pfe_test.loc[i, 'TrueLabel'])
    pfe_test.loc[i, 's3'] = str(pfe_test.loc[i-2, 'TrueLabel'] + \
                         pfe_test.loc[i, 's2'])
    pfe_test.loc[i, 's4'] = str(pfe_test.loc[i-3, 'TrueLabel'] + \
                         pfe_test.loc[i, 's3'])

# Now calculate the predictions for each W = 2,3,4 for s[+|-] as the one
# which is more frequent in the training data.
for i in range(start_day, pfe_test.shape[0]):
    pfe_test.loc[i, 'PredW2'] = JparkerHw2Helper.assign_prediction(\
                                    pfe_test.loc[i, 's2'], \
                                    PFE_DEFAULT, \
                                    pfe_train_dict)
    pfe_test.loc[i, 'PredW3'] = JparkerHw2Helper.assign_prediction(\
                                    pfe_test.loc[i, 's3'], \
                                    PFE_DEFAULT, \
                                    pfe_train_dict)
    pfe_test.loc[i, 'PredW4'] = JparkerHw2Helper.assign_prediction(\
                                    pfe_test.loc[i, 's4'], \
                                    PFE_DEFAULT, \
                                    pfe_train_dict)

# Q2.2 - Calculate the accuracy for each prediction of W=2,3,4

# Does the prediction match the true label?
for i in range(pfe_test.shape[0]):
    pfe_test.loc[i, 'AccW2'] = int(pfe_test.loc[i, 'PredW2'] == \
                                   pfe_test.loc[i, 'TrueLabel'])
    pfe_test.loc[i, 'AccW3'] = int(pfe_test.loc[i, 'PredW3'] == \
                                   pfe_test.loc[i, 'TrueLabel'])
    pfe_test.loc[i, 'AccW4'] = int(pfe_test.loc[i, 'PredW4'] == \
                                   pfe_test.loc[i, 'TrueLabel'])

# Calculate the accuracy (percent correct) of each prediction.
pfe_accuracy_2 = sum(pfe_test['AccW2']) / pfe_test.shape[0] * 100
pfe_accuracy_3 = sum(pfe_test['AccW3']) / pfe_test.shape[0] * 100
pfe_accuracy_4 = sum(pfe_test['AccW4']) / pfe_test.shape[0] * 100

print ("Q2.2: Accuracy for PFE W2 is {:.3f}".format(pfe_accuracy_2))
print ("Q2.2: Accuracy for PFE W3 is {:.3f}".format(pfe_accuracy_3))
print ("Q2.2: Accuracy for PFE W4 is {:.3f}".format(pfe_accuracy_4))


##### DO IT AGAIN FOR SPY #####
# Removing most comments as the code is copy-pasta'd from above.
spy_df = pd.DataFrame(JparkerHw2Helper.load_ticker('SPY'), \
                        columns= ['Date','Year','DayOfWeek','Adj.Cloose',\
                                  'PercentGain'])
spy_df = spy_df.sort_values('Date')
spy_df['TrueLabel'] = np.where(spy_df['PercentGain'] < 0, '-', '+')

# Question 2.1
# Predict labels in years 4 and 5 based on True Labels in years 1 - 3.
#
# First, extract the true labels from years 1 - 3 as a text string (see Q1).
spy_train = spy_df.loc[(spy_df['Year'].isin([2016, 2017, 2018]))]
spy_train_str = spy_train['TrueLabel'].to_string(index = False).replace('\n','')

# Quantify each substring in spy_train_str of length 3, 4 and 5 in a dict, the
# substring value will be the key.
spy_train_dict = dict()
for i in range(len(spy_train_str)):
    if spy_train_str[i:i + 3] in spy_train_dict:
        spy_train_dict[spy_train_str[i:i + 3]] += 1
    else:
        spy_train_dict[spy_train_str[i:i + 3]] = 1
    if spy_train_str[i:i + 4] in spy_train_dict:
        spy_train_dict[spy_train_str[i:i + 4]] += 1
    else:
        spy_train_dict[spy_train_str[i:i + 4]] = 1
    if spy_train_str[i:i + 5] in spy_train_dict:
        spy_train_dict[spy_train_str[i:i + 5]] += 1
    else:
        spy_train_dict[spy_train_str[i:i + 5]] = 1

# Calculate the probability of each substring in spy_train_dict.
# REFERENCE: https://www.geeksforgeeks.org/count-of-sub-strings-of-length-n-\
#   possible-from-the-given-string/#:~:text=Approach%3A%20The%20count%20of%20\
#   sub,length%20of%20the%20given%20string.
for key in spy_train_dict:
    spy_train_dict[key] = spy_train_dict[key] / (len(spy_train_str) - len(key) + 1)

# Prediction process:
# For a day d, predict the label for day d + 1 based on the majority label
# following the pattern of hyper-parameter W, the true label "word" s of length
# W (W including day d) for all W = 2,3,4.
#
# We need to predict on W = 2,3,4, these are going to be overlapping ...
# NOTE - In order to predict DAY 0 we need to look at W from the end of year 3.
# Reset the dataframe index for safety.
spy_test = spy_df.loc[(spy_df['Year'].isin([2019,2020]))]
spy_test = pd.concat([spy_train.tail(3), spy_test])
spy_test = spy_test.reset_index(drop = True)

# Day 1 is the beginning of 2019
start_day = min(spy_test.index[spy_test['Year'] == 2019])

# First construct the strings for W = 2,3,4 from years 4 and 5.
# This isn't really a necessary step, but it's useful to see what is being
#   captured as the W strings and make sure it's being done correctly, cuz
#   honestly this is confusing.
for i in range(start_day, spy_test.shape[0]-1):
    spy_test.loc[i,'s2'] = str(spy_test.loc[i-1, 'TrueLabel'] + \
                             spy_test.loc[i, 'TrueLabel'])
    spy_test.loc[i, 's3'] = str(spy_test.loc[i-2, 'TrueLabel'] + \
                         spy_test.loc[i, 's2'])
    spy_test.loc[i, 's4'] = str(spy_test.loc[i-3, 'TrueLabel'] + \
                         spy_test.loc[i, 's3'])

# Now calculate the predictions for each W = 2,3,4 for s[+|-] as the one
# which is more frequent in the training data.
for i in range(start_day, spy_test.shape[0]-1):
    spy_test.loc[i, 'PredW2'] = JparkerHw2Helper.assign_prediction(\
                                    spy_test.loc[i, 's2'], \
                                    SPY_DEFAULT, \
                                    spy_train_dict)
    spy_test.loc[i, 'PredW3'] = JparkerHw2Helper.assign_prediction(\
                                    spy_test.loc[i, 's3'], \
                                    SPY_DEFAULT, \
                                    spy_train_dict)
    spy_test.loc[i, 'PredW4'] = JparkerHw2Helper.assign_prediction(\
                                    spy_test.loc[i, 's4'], \
                                    SPY_DEFAULT, \
                                    spy_train_dict)

# Q2.2 - Calculate the accuracy for each prediction of W=2,3,4

# Does the prediction match the true label?
for i in range(spy_test.shape[0]):
    spy_test.loc[i, 'AccW2'] = int(spy_test.loc[i, 'PredW2'] == \
                                   spy_test.loc[i, 'TrueLabel'])
    spy_test.loc[i, 'AccW3'] = int(spy_test.loc[i, 'PredW3'] == \
                                   spy_test.loc[i, 'TrueLabel'])
    spy_test.loc[i, 'AccW4'] = int(spy_test.loc[i, 'PredW4'] == \
                                   spy_test.loc[i, 'TrueLabel'])

# Calculate the accuracy (percent correct) of each prediction.
spy_accuracy_2 = sum(spy_test['AccW2']) / spy_test.shape[0] * 100
spy_accuracy_3 = sum(spy_test['AccW3']) / spy_test.shape[0] * 100
spy_accuracy_4 = sum(spy_test['AccW4']) / spy_test.shape[0] * 100

print ("Q2.2: Accuracy for SPY W2 is {:.3f}".format(spy_accuracy_2))
print ("Q2.2: Accuracy for SPY W3 is {:.3f}".format(spy_accuracy_3))
print ("Q2.2: Accuracy for SPY W4 is {:.3f}".format(spy_accuracy_4))
