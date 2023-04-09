# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: March 29, 2022
Homework Problem 2.1

Read historical stock data (PFE, SPY) and assign a label for gain or loss days.
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

# Load the data for PFE (Pfizer Inc).
# load_ticker() returns a list of lists including:
#   Datestamp,
#   Year
#   Numeric day of week
#   Adjusted closing price
#   Percent day return

# Load the data to a pandas DataFrame
# Sort the list by date.
pfe_df = pd.DataFrame(JparkerHw2Helper.load_ticker('PFE'), \
                        columns= ['Date','Year','DayOfWeek','Adj.Cloose',\
                                  'PercentGain'])
pfe_df = pfe_df.sort_values('Date')

# Question 1.1
# Assign a "TrueLabel" column based on PercentGains.
#   '+' for postive gains
#   '-' for losses
pfe_df['TrueLabel'] = np.where(pfe_df['PercentGain'] < 0, '-', '+')

# Question 1.2
# For years 1 - 3, what is the probability that the next day is an up day.
pfe_Ltot = pfe_df.loc[(pfe_df['Year'].isin([2016, 2017, 2018]))]
pfe_Lplus = pfe_Ltot.loc[(pfe_Ltot['TrueLabel'] == '+')]
pfe_plus_probability = pfe_Lplus.shape[0] / (pfe_Ltot.shape[0] - 1)
print("Q1.2: Probability of a PFE up day {:.3f}: ".format(pfe_plus_probability))

# Question 1.3
# For years 1 - 3, what is the probability that after seeing k consecutive
# down days (TrueLable = '-') the next day will be an up day for k = 1,2 and 3?

# Convert pfeLtot TrueLabel to a string.
pfe_Ltot_str = pfe_Ltot['TrueLabel'].to_string(index = False).replace('\n','')
# Calcuate the probability of '-+', '--+', '---+'

# Probability k2
pfe_k2_prob = pfe_Ltot_str.count('-+') / \
    (pfe_Ltot_str.count('-+') + pfe_Ltot_str.count('--'))
print("Q1.3: PFE k2 down probability is: {:.3f}".format(pfe_k2_prob))

# Probability k3
pfe_k3_prob = pfe_Ltot_str.count('--+') / \
    (pfe_Ltot_str.count('--+') + pfe_Ltot_str.count('---'))
print("Q1.3: PFE k3 down probability is: {:.3f}".format(pfe_k3_prob))

# Probability k4
pfe_k4_prob = pfe_Ltot_str.count('---+') / \
    (pfe_Ltot_str.count('---+') + pfe_Ltot_str.count('----'))
print("Q1.3: PFE k4 down probability is: {:.3f}".format(pfe_k4_prob))

# Question 1.4
# For years 1 - 3, what is the probability that after seeing k consecutive
# up days (TrueLable = '+') the next day will be an up day for k = 1,2 and 3?

# Probability k2
pfe_k2_prob = pfe_Ltot_str.count('++') / \
    (pfe_Ltot_str.count('++') + pfe_Ltot_str.count('+-'))
print("Q1.4: PFE k2 up probability is: {:.3f}".format(pfe_k2_prob))

# Probability k3
pfe_k3_prob = pfe_Ltot_str.count('+++') / \
    (pfe_Ltot_str.count('+++') + pfe_Ltot_str.count('++-'))
print("Q1.4: PFE k3 up probability is: {:.3f}".format(pfe_k3_prob))

# Probability k4
pfe_k4_prob = pfe_Ltot_str.count('++++') / \
    (pfe_Ltot_str.count('++++') + pfe_Ltot_str.count('+++-'))
print("Q1.4: PFE k4 up probability is: {:.3f}".format(pfe_k4_prob))

##### DO IT AGAIN FOR SPY #####
# Removing most comments as the code is copy-pasta'd from above.
# Load the data to a pandas DataFrame
# Sort the list by date.
spy_df = pd.DataFrame(JparkerHw2Helper.load_ticker('SPY'), \
                        columns= ['Date','Year','DayOfWeek','Adj.Cloose',\
                                  'PercentGain'])
spy_df = spy_df.sort_values('Date')

# Question 1.1
spy_df['TrueLabel'] = np.where(spy_df['PercentGain'] < 0, '-', '+')

# Question 1.2
spy_Ltot = spy_df.loc[(spy_df['Year'].isin([2016, 2017, 2018]))]
spy_Lplus = spy_Ltot.loc[(spy_Ltot['TrueLabel'] == '+')]
spy_plus_probability = spy_Lplus.shape[0] / (spy_Ltot.shape[0] - 1)
print("Q1.2: Probability of a SPY up day {:.3f}: ".format(spy_plus_probability))

# Question 1.3
# For years 1 - 3, what is the probability that after seeing k consecutive
# down days (TrueLable = '-') the next day will be an up day for k = 1,2 and 3?

# Convert spyLtot TrueLabel to a string.
spy_Ltot_str = spy_Ltot['TrueLabel'].to_string(index = False).replace('\n','')
# Calcuate the probability of '-+', '--+', '---+'

# Probability k2
spy_k2_prob = spy_Ltot_str.count('-+') / \
    (spy_Ltot_str.count('-+') + spy_Ltot_str.count('--'))
print("Q1.3: SPY k2 down probability is: {:.3f}".format(spy_k2_prob))

# Probability k3
spy_k3_prob = spy_Ltot_str.count('--+') / \
    (spy_Ltot_str.count('--+') + spy_Ltot_str.count('---'))
print("Q1.3: SPY k3 down probability is: {:.3f}".format(spy_k3_prob))

# Probability k4
spy_k4_prob = spy_Ltot_str.count('---+') / \
    (spy_Ltot_str.count('---+') + spy_Ltot_str.count('----'))
print("Q1.3: SPY k4 down probability is: {:.3f}".format(spy_k4_prob))

# Question 1.4
# For years 1 - 3, what is the probability that after seeing k consecutive
# up days (TrueLable = '+') the next day will be an up day for k = 1,2 and 3?

# Probability k2
spy_k2_prob = spy_Ltot_str.count('++') / \
    (spy_Ltot_str.count('++') + spy_Ltot_str.count('+-'))
print("Q1.4: SPY k2 up probability is: {:.3f}".format(spy_k2_prob))

# Probability k3
spy_k3_prob = spy_Ltot_str.count('+++') / \
    (spy_Ltot_str.count('+++') + spy_Ltot_str.count('++-'))
print("Q1.4: SPY k3 up probability is: {:.3f}".format(spy_k3_prob))

# Probability k4
spy_k4_prob = spy_Ltot_str.count('++++') / \
    (spy_Ltot_str.count('++++') + spy_Ltot_str.count('+++-'))
print("Q1.4: SPY k4 up probability is: {:.3f}".format(spy_k4_prob))