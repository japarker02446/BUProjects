# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: March 29, 2022
Homework Problem 2.4

Read historical stock data (PFE, SPY)
Make predictions about gain or loss labels.
Calculate true and false positive rates.
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

# Question 3.1
# Predict ENSEMBLE labels in years 4 and 5 based on True Labels in years 1 - 3.
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
# ADD Ensemble prediction which is the majority label from Prediction W = 2,3,4
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

    pfe_test.loc[i, 'PredE'] = JparkerHw2Helper.assign_ensembl(\
                                    pfe_test.loc[i, 'PredW2'],\
                                    pfe_test.loc[i, 'PredW3'],\
                                    pfe_test.loc[i, 'PredW4'])

# There's probably a better way to do this, but I only have 1.5 hours left
# at this point and I still have to figure out plotting.
for i in range(pfe_test.shape[0]):

    # True label is +
    if pfe_test.loc[i, 'TrueLabel'] == '+':

        # W = 2
        if pfe_test.loc[i, 'PredW2'] == '+':
            pfe_test.loc[i, 'AccW2'] = 1
            pfe_test.loc[i, 'TP2'] = 1
            pfe_test.loc[i, 'FP2'] = 0
            pfe_test.loc[i, 'TN2'] = 0
            pfe_test.loc[i, 'FN2'] = 0
        else:
            pfe_test.loc[i, 'AccW2'] = 0
            pfe_test.loc[i, 'TP2'] = 0
            pfe_test.loc[i, 'FP2'] = 1
            pfe_test.loc[i, 'TN2'] = 0
            pfe_test.loc[i, 'FN2'] = 0

        # W = 3
        if pfe_test.loc[i, 'PredW3'] == '+':
            pfe_test.loc[i, 'AccW3'] = 1
            pfe_test.loc[i, 'TP3'] = 1
            pfe_test.loc[i, 'FP3'] = 0
            pfe_test.loc[i, 'TN3'] = 0
            pfe_test.loc[i, 'FN3'] = 0
        else:
            pfe_test.loc[i, 'AccW3'] = 0
            pfe_test.loc[i, 'TP3'] = 0
            pfe_test.loc[i, 'FP3'] = 1
            pfe_test.loc[i, 'TN3'] = 0
            pfe_test.loc[i, 'FN3'] = 0

        # W = 4
        if pfe_test.loc[i, 'PredW4'] == '+':
            pfe_test.loc[i, 'AccW4'] = 1
            pfe_test.loc[i, 'TP4'] = 1
            pfe_test.loc[i, 'FP4'] = 0
            pfe_test.loc[i, 'TN4'] = 0
            pfe_test.loc[i, 'FN4'] = 0
        else:
            pfe_test.loc[i, 'AccW4'] = 0
            pfe_test.loc[i, 'TP4'] = 0
            pfe_test.loc[i, 'FP4'] = 1
            pfe_test.loc[i, 'TN4'] = 0
            pfe_test.loc[i, 'FN4'] = 0

        # Ensemble
        if pfe_test.loc[i, 'PredE'] == '+':
            pfe_test.loc[i, 'AccE'] = 1
            pfe_test.loc[i, 'TPE'] = 1
            pfe_test.loc[i, 'FPE'] = 0
            pfe_test.loc[i, 'TNE'] = 0
            pfe_test.loc[i, 'FNE'] = 0
        else:
            pfe_test.loc[i, 'AccE'] = 0
            pfe_test.loc[i, 'TPE'] = 0
            pfe_test.loc[i, 'FPE'] = 1
            pfe_test.loc[i, 'TNE'] = 0
            pfe_test.loc[i, 'FNE'] = 0

    # True label is -
    else:

        # W = 2
        if pfe_test.loc[i, 'PredW2'] == '-':
            pfe_test.loc[i, 'AccW2'] = 1
            pfe_test.loc[i, 'TP2'] = 0
            pfe_test.loc[i, 'FP2'] = 0
            pfe_test.loc[i, 'TN2'] = 1
            pfe_test.loc[i, 'FN2'] = 0
        else:
            pfe_test.loc[i, 'AccW2'] = 0
            pfe_test.loc[i, 'TP2'] = 0
            pfe_test.loc[i, 'FP2'] = 0
            pfe_test.loc[i, 'TN2'] = 0
            pfe_test.loc[i, 'FN2'] = 1

        # W = 3
        if pfe_test.loc[i, 'PredW3'] == '-':
            pfe_test.loc[i, 'AccW3'] = 1
            pfe_test.loc[i, 'TP3'] = 0
            pfe_test.loc[i, 'FP3'] = 0
            pfe_test.loc[i, 'TN3'] = 1
            pfe_test.loc[i, 'FN3'] = 0
        else:
            pfe_test.loc[i, 'AccW3'] = 0
            pfe_test.loc[i, 'TP3'] = 0
            pfe_test.loc[i, 'FP3'] = 0
            pfe_test.loc[i, 'TN3'] = 0
            pfe_test.loc[i, 'FN3'] = 1

        # W = 4
        if pfe_test.loc[i, 'PredW4'] == '-':
            pfe_test.loc[i, 'AccW4'] = 1
            pfe_test.loc[i, 'TP4'] = 0
            pfe_test.loc[i, 'FP4'] = 0
            pfe_test.loc[i, 'TN4'] = 1
            pfe_test.loc[i, 'FN4'] = 0
        else:
            pfe_test.loc[i, 'AccW4'] = 0
            pfe_test.loc[i, 'TP4'] = 0
            pfe_test.loc[i, 'FP4'] = 0
            pfe_test.loc[i, 'TN4'] = 0
            pfe_test.loc[i, 'FN4'] = 1

        # Ensemble
        if pfe_test.loc[i, 'PredE'] == '-':
            pfe_test.loc[i, 'AccE'] = 1
            pfe_test.loc[i, 'TPE'] = 0
            pfe_test.loc[i, 'FPE'] = 0
            pfe_test.loc[i, 'TNE'] = 1
            pfe_test.loc[i, 'FNE'] = 0
        else:
            pfe_test.loc[i, 'AccE'] = 0
            pfe_test.loc[i, 'TPE'] = 0
            pfe_test.loc[i, 'FPE'] = 0
            pfe_test.loc[i, 'TNE'] = 0
            pfe_test.loc[i, 'FNE'] = 1

# Calculate the summary values for each model.
pfe_tp_2 = sum(pfe_test['TP2'])
pfe_tp_3 = sum(pfe_test['TP3'])
pfe_tp_4 = sum(pfe_test['TP4'])
pfe_tp_E = sum(pfe_test['TPE'])

pfe_fp_2 = sum(pfe_test['FP2'])
pfe_fp_3 = sum(pfe_test['FP3'])
pfe_fp_4 = sum(pfe_test['FP4'])
pfe_fp_E = sum(pfe_test['FPE'])

pfe_tn_2 = sum(pfe_test['TN2'])
pfe_tn_3 = sum(pfe_test['TN3'])
pfe_tn_4 = sum(pfe_test['TN4'])
pfe_tn_E = sum(pfe_test['TNE'])

pfe_fn_2 = sum(pfe_test['FN2'])
pfe_fn_3 = sum(pfe_test['FN3'])
pfe_fn_4 = sum(pfe_test['FN4'])
pfe_fn_E = sum(pfe_test['FNE'])

pfe_accuracy_2 = sum(pfe_test['AccW2']) / pfe_test.shape[0] * 100
pfe_accuracy_3 = sum(pfe_test['AccW3']) / pfe_test.shape[0] * 100
pfe_accuracy_4 = sum(pfe_test['AccW4']) / pfe_test.shape[0] * 100
pfe_accuracy_E = sum(pfe_test['AccE']) / pfe_test.shape[0] * 100

pfe_tpr_2 = pfe_tp_2 / (pfe_tp_2 + pfe_fn_2)
pfe_tpr_3 = pfe_tp_3 / (pfe_tp_3 + pfe_fn_3)
pfe_tpr_4 = pfe_tp_4 / (pfe_tp_4 + pfe_fn_4)
pfe_tpr_E = pfe_tp_E / (pfe_tp_E + pfe_fn_E)

pfe_tnr_2 = pfe_tn_2 / (pfe_tn_2 + pfe_fp_2)
pfe_tnr_3 = pfe_tn_3 / (pfe_tn_3 + pfe_fp_3)
pfe_tnr_4 = pfe_tn_4 / (pfe_tn_4 + pfe_fp_4)
pfe_tnr_E = pfe_tn_E / (pfe_tn_E + pfe_fp_E)

print ("Q3: TP for PFE W2 is {:.3f}".format(pfe_tp_2))
print ("Q3: TP for PFE W3 is {:.3f}".format(pfe_tp_3))
print ("Q3: TP for PFE W4 is {:.3f}".format(pfe_tp_4))
print ("Q3: TP for PFE E is {:.3f}".format(pfe_tp_E))

print ("Q3: FP for PFE W2 is {:.3f}".format(pfe_fp_2))
print ("Q3: FP for PFE W3 is {:.3f}".format(pfe_fp_3))
print ("Q3: FP for PFE W4 is {:.3f}".format(pfe_fp_4))
print ("Q3: FP for PFE E is {:.3f}".format(pfe_fp_E))

print ("Q3: TN for PFE W2 is {:.3f}".format(pfe_tn_2))
print ("Q3: TN for PFE W3 is {:.3f}".format(pfe_tn_3))
print ("Q3: TN for PFE W4 is {:.3f}".format(pfe_tn_4))
print ("Q3: TN for PFE E is {:.3f}".format(pfe_tn_E))

print ("Q3: FN for PFE W2 is {:.3f}".format(pfe_fn_2))
print ("Q3: FN for PFE W3 is {:.3f}".format(pfe_fn_3))
print ("Q3: FN for PFE W4 is {:.3f}".format(pfe_fn_4))
print ("Q3: FN for PFE E is {:.3f}".format(pfe_fn_E))

print ("Q3: Accuracy for PFE W2 is {:.3f}".format(pfe_accuracy_2))
print ("Q3: Accuracy for PFE W3 is {:.3f}".format(pfe_accuracy_3))
print ("Q3: Accuracy for PFE W4 is {:.3f}".format(pfe_accuracy_4))
print ("Q3: Accuracy for PFE Ensemble is {:.3f}".format(pfe_accuracy_E))

print ("Q3: TPR for PFE W2 is {:.3f}".format(pfe_tpr_2))
print ("Q3: TPR for PFE W3 is {:.3f}".format(pfe_tpr_3))
print ("Q3: TPR for PFE W4 is {:.3f}".format(pfe_tpr_4))
print ("Q3: TPR for PFE E is {:.3f}".format(pfe_tpr_E))

print ("Q3: TNR for PFE W2 is {:.3f}".format(pfe_tnr_2))
print ("Q3: TNR for PFE W3 is {:.3f}".format(pfe_tnr_3))
print ("Q3: TNR for PFE W4 is {:.3f}".format(pfe_tnr_4))
print ("Q3: TNR for PFE E is {:.3f}".format(pfe_tnr_E))


##### DO IT AGAIN FOR SPY #####
# Removing most comments as the code is copy-pasta'd from above.
spy_df = pd.DataFrame(JparkerHw2Helper.load_ticker('SPY'), \
                        columns= ['Date','Year','DayOfWeek','Adj.Cloose',\
                                  'PercentGain'])
spy_df = spy_df.sort_values('Date')
spy_df['TrueLabel'] = np.where(spy_df['PercentGain'] < 0, '-', '+')

# Question 3.1
# Predict ENSEMBLE labels in years 4 and 5 based on True Labels in years 1 - 3.
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
for i in range(start_day, spy_test.shape[0]):
    spy_test.loc[i,'s2'] = str(spy_test.loc[i-1, 'TrueLabel'] + \
                             spy_test.loc[i, 'TrueLabel'])
    spy_test.loc[i, 's3'] = str(spy_test.loc[i-2, 'TrueLabel'] + \
                         spy_test.loc[i, 's2'])
    spy_test.loc[i, 's4'] = str(spy_test.loc[i-3, 'TrueLabel'] + \
                         spy_test.loc[i, 's3'])

# Now calculate the predictions for each W = 2,3,4 for s[+|-] as the one
# which is more frequent in the training data.
# ADD Ensemble prediction which is the majority label from Prediction W = 2,3,4
for i in range(start_day, spy_test.shape[0]):
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

    spy_test.loc[i, 'PredE'] = JparkerHw2Helper.assign_ensembl(\
                                    spy_test.loc[i, 'PredW2'],\
                                    spy_test.loc[i, 'PredW3'],\
                                    spy_test.loc[i, 'PredW4'])

# There's probably a better way to do this, but I only have 1.5 hours left
# at this point and I still have to figure out plotting.
for i in range(spy_test.shape[0]):

    # True label is +
    if spy_test.loc[i, 'TrueLabel'] == '+':

        # W = 2
        if spy_test.loc[i, 'PredW2'] == '+':
            spy_test.loc[i, 'AccW2'] = 1
            spy_test.loc[i, 'TP2'] = 1
            spy_test.loc[i, 'FP2'] = 0
            spy_test.loc[i, 'TN2'] = 0
            spy_test.loc[i, 'FN2'] = 0
        else:
            spy_test.loc[i, 'AccW2'] = 0
            spy_test.loc[i, 'TP2'] = 0
            spy_test.loc[i, 'FP2'] = 1
            spy_test.loc[i, 'TN2'] = 0
            spy_test.loc[i, 'FN2'] = 0

        # W = 3
        if spy_test.loc[i, 'PredW3'] == '+':
            spy_test.loc[i, 'AccW3'] = 1
            spy_test.loc[i, 'TP3'] = 1
            spy_test.loc[i, 'FP3'] = 0
            spy_test.loc[i, 'TN3'] = 0
            spy_test.loc[i, 'FN3'] = 0
        else:
            spy_test.loc[i, 'AccW3'] = 0
            spy_test.loc[i, 'TP3'] = 0
            spy_test.loc[i, 'FP3'] = 1
            spy_test.loc[i, 'TN3'] = 0
            spy_test.loc[i, 'FN3'] = 0

        # W = 4
        if spy_test.loc[i, 'PredW4'] == '+':
            spy_test.loc[i, 'AccW4'] = 1
            spy_test.loc[i, 'TP4'] = 1
            spy_test.loc[i, 'FP4'] = 0
            spy_test.loc[i, 'TN4'] = 0
            spy_test.loc[i, 'FN4'] = 0
        else:
            spy_test.loc[i, 'AccW4'] = 0
            spy_test.loc[i, 'TP4'] = 0
            spy_test.loc[i, 'FP4'] = 1
            spy_test.loc[i, 'TN4'] = 0
            spy_test.loc[i, 'FN4'] = 0

        # Ensemble
        if spy_test.loc[i, 'PredE'] == '+':
            spy_test.loc[i, 'AccE'] = 1
            spy_test.loc[i, 'TPE'] = 1
            spy_test.loc[i, 'FPE'] = 0
            spy_test.loc[i, 'TNE'] = 0
            spy_test.loc[i, 'FNE'] = 0
        else:
            spy_test.loc[i, 'AccE'] = 0
            spy_test.loc[i, 'TPE'] = 0
            spy_test.loc[i, 'FPE'] = 1
            spy_test.loc[i, 'TNE'] = 0
            spy_test.loc[i, 'FNE'] = 0

    # True label is -
    else:

        # W = 2
        if spy_test.loc[i, 'PredW2'] == '-':
            spy_test.loc[i, 'AccW2'] = 1
            spy_test.loc[i, 'TP2'] = 0
            spy_test.loc[i, 'FP2'] = 0
            spy_test.loc[i, 'TN2'] = 1
            spy_test.loc[i, 'FN2'] = 0
        else:
            spy_test.loc[i, 'AccW2'] = 0
            spy_test.loc[i, 'TP2'] = 0
            spy_test.loc[i, 'FP2'] = 0
            spy_test.loc[i, 'TN2'] = 0
            spy_test.loc[i, 'FN2'] = 1

        # W = 3
        if spy_test.loc[i, 'PredW3'] == '-':
            spy_test.loc[i, 'AccW3'] = 1
            spy_test.loc[i, 'TP3'] = 0
            spy_test.loc[i, 'FP3'] = 0
            spy_test.loc[i, 'TN3'] = 1
            spy_test.loc[i, 'FN3'] = 0
        else:
            spy_test.loc[i, 'AccW3'] = 0
            spy_test.loc[i, 'TP3'] = 0
            spy_test.loc[i, 'FP3'] = 0
            spy_test.loc[i, 'TN3'] = 0
            spy_test.loc[i, 'FN3'] = 1

        # W = 4
        if spy_test.loc[i, 'PredW4'] == '-':
            spy_test.loc[i, 'AccW4'] = 1
            spy_test.loc[i, 'TP4'] = 0
            spy_test.loc[i, 'FP4'] = 0
            spy_test.loc[i, 'TN4'] = 1
            spy_test.loc[i, 'FN4'] = 0
        else:
            spy_test.loc[i, 'AccW4'] = 0
            spy_test.loc[i, 'TP4'] = 0
            spy_test.loc[i, 'FP4'] = 0
            spy_test.loc[i, 'TN4'] = 0
            spy_test.loc[i, 'FN4'] = 1

        # Ensemble
        if spy_test.loc[i, 'PredE'] == '-':
            spy_test.loc[i, 'AccE'] = 1
            spy_test.loc[i, 'TPE'] = 0
            spy_test.loc[i, 'FPE'] = 0
            spy_test.loc[i, 'TNE'] = 1
            spy_test.loc[i, 'FNE'] = 0
        else:
            spy_test.loc[i, 'AccE'] = 0
            spy_test.loc[i, 'TPE'] = 0
            spy_test.loc[i, 'FPE'] = 0
            spy_test.loc[i, 'TNE'] = 0
            spy_test.loc[i, 'FNE'] = 1

# Calculate the summary values for each model.
spy_tp_2 = sum(spy_test['TP2'])
spy_tp_3 = sum(spy_test['TP3'])
spy_tp_4 = sum(spy_test['TP4'])
spy_tp_E = sum(spy_test['TPE'])

spy_fp_2 = sum(spy_test['FP2'])
spy_fp_3 = sum(spy_test['FP3'])
spy_fp_4 = sum(spy_test['FP4'])
spy_fp_E = sum(spy_test['FPE'])

spy_tn_2 = sum(spy_test['TN2'])
spy_tn_3 = sum(spy_test['TN3'])
spy_tn_4 = sum(spy_test['TN4'])
spy_tn_E = sum(spy_test['TNE'])

spy_fn_2 = sum(spy_test['FN2'])
spy_fn_3 = sum(spy_test['FN3'])
spy_fn_4 = sum(spy_test['FN4'])
spy_fn_E = sum(spy_test['FNE'])

spy_accuracy_2 = sum(spy_test['AccW2']) / spy_test.shape[0] * 100
spy_accuracy_3 = sum(spy_test['AccW3']) / spy_test.shape[0] * 100
spy_accuracy_4 = sum(spy_test['AccW4']) / spy_test.shape[0] * 100
spy_accuracy_E = sum(spy_test['AccE']) / spy_test.shape[0] * 100

spy_tpr_2 = spy_tp_2 / (spy_tp_2 + spy_fn_2)
spy_tpr_3 = spy_tp_3 / (spy_tp_3 + spy_fn_3)
spy_tpr_4 = spy_tp_4 / (spy_tp_4 + spy_fn_4)
spy_tpr_E = spy_tp_E / (spy_tp_E + spy_fn_E)

spy_tnr_2 = spy_tn_2 / (spy_tn_2 + spy_fp_2)
spy_tnr_3 = spy_tn_3 / (spy_tn_3 + spy_fp_3)
spy_tnr_4 = spy_tn_4 / (spy_tn_4 + spy_fp_4)
spy_tnr_E = spy_tn_E / (spy_tn_E + spy_fp_E)

print ("Q3: TP for SPY W2 is {:.3f}".format(spy_tp_2))
print ("Q3: TP for SPY W3 is {:.3f}".format(spy_tp_3))
print ("Q3: TP for SPY W4 is {:.3f}".format(spy_tp_4))
print ("Q3: TP for SPY E is {:.3f}".format(spy_tp_E))

print ("Q3: FP for SPY W2 is {:.3f}".format(spy_fp_2))
print ("Q3: FP for SPY W3 is {:.3f}".format(spy_fp_3))
print ("Q3: FP for SPY W4 is {:.3f}".format(spy_fp_4))
print ("Q3: FP for SPY E is {:.3f}".format(spy_fp_E))

print ("Q3: TN for SPY W2 is {:.3f}".format(spy_tn_2))
print ("Q3: TN for SPY W3 is {:.3f}".format(spy_tn_3))
print ("Q3: TN for SPY W4 is {:.3f}".format(spy_tn_4))
print ("Q3: TN for SPY E is {:.3f}".format(spy_tn_E))

print ("Q3: FN for SPY W2 is {:.3f}".format(spy_fn_2))
print ("Q3: FN for SPY W3 is {:.3f}".format(spy_fn_3))
print ("Q3: FN for SPY W4 is {:.3f}".format(spy_fn_4))
print ("Q3: FN for SPY E is {:.3f}".format(spy_fn_E))

print ("Q3: Accuracy for SPY W2 is {:.3f}".format(spy_accuracy_2))
print ("Q3: Accuracy for SPY W3 is {:.3f}".format(spy_accuracy_3))
print ("Q3: Accuracy for SPY W4 is {:.3f}".format(spy_accuracy_4))
print ("Q3: Accuracy for SPY Ensemble is {:.3f}".format(spy_accuracy_E))

print ("Q3: TPR for SPY W2 is {:.3f}".format(spy_tpr_2))
print ("Q3: TPR for SPY W3 is {:.3f}".format(spy_tpr_3))
print ("Q3: TPR for SPY W4 is {:.3f}".format(spy_tpr_4))
print ("Q3: TPR for SPY E is {:.3f}".format(spy_tpr_E))

print ("Q3: TNR for SPY W2 is {:.3f}".format(spy_tnr_2))
print ("Q3: TNR for SPY W3 is {:.3f}".format(spy_tnr_3))
print ("Q3: TNR for SPY W4 is {:.3f}".format(spy_tnr_4))
print ("Q3: TNR for SPY E is {:.3f}".format(spy_tnr_E))

