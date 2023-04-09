# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 1, 2022
Homework Problem 3.1

Read and summarize real vs fake bank note data from UCI Data Set repository.
"""
import os

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW3')

# Import helper functions to stock data from file.
from JparkerHw3Helper import *

# Load the banknote data set from a text file to a pandas dataframe.
note_data = JparkerHw3Helper.load_note_data()

# QUESTION 1.1
# Assign a color label for each Class value.  Green for 0 and Red for 1.
note_data['Color'] = ['green' if c == 0 else 'red' for c in note_data.Class]

# QUESTION 1.2
# For each feature F1 - F4 (only), compute the mean and standard deviation (only)
#   for Class 0, Class 1 and all entries.  Round to two decimal places.
print ("ALL Values")
print(note_data.drop(['Class'], axis=1).describe().loc[['mean', 'std'], ].\
      round(2))

print ('Class 0')
print(note_data.drop(['Class'], axis=1).loc[note_data.Class == 0].describe().\
      loc[['mean', 'std'], ].round(2))

print('Class 1')
print(note_data.drop(['Class'], axis=1).loc[note_data.Class == 1].describe().\
      loc[['mean', 'std'], ].round(2))

# QUESTION 1.3
# Good notes (class 0) have F1 > 0, F2 > 0 and F3 < 1
# Bad notes (class 1) have F1 < 0, F2 < 0 and F3 > 1
# F4 doesn't seem to be able to differentiate
