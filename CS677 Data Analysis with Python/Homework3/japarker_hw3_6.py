# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 1, 2022
Homework Problem 3.6

Read and plot real vs fake bank note data from UCI Data Set repository.
Implement logistic regression to predict bill authenticity with dropped features
F1, F2, F3 or F4.
"""
import numpy as np
import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW3')

# Import helper functions to stock data from file.
from JparkerHw3Helper import *

# Load the banknote data set from a text file to a pandas dataframe.
note_data = JparkerHw3Helper.load_note_data()

# Split the data into Xtrain and Xtest parts (50/50).
# Using the same random_state value should give us the same split as before.
X = note_data.iloc[:, :4]
y = note_data.Class
X_train,X_test,y_train, y_test = train_test_split(X, y, test_size = 0.5,\
                                                  random_state = 1,\
                                                  stratify = y)

# QUESTION 6.1
# Predict accuracy by logistic regression.
# This time, serially drop one of the features (F1, F2, F3 or F4) from Xtrain
#   and Xtest.  Measure and record the accuracy of each new model.
#
# Build a table of k values vs prediction metrics.
f_accuracy = pd.DataFrame(columns = \
                          ['Feature', 'TP', 'FP', 'TN', 'FN', 'accuracy', 'TPR', 'TNR'])

for i in ['F1', 'F2', 'F3', 'F4']:
    X_train_drop = X_train.drop(i, axis = 1)
    X_test_drop = X_test.drop(i, axis = 1)

    log_reg = LogisticRegression()
    log_reg.fit(X_train_drop, y_train)
    y_pred = log_reg.predict(X_test_drop)

    pred_calc = pd.DataFrame(y_pred, index = X_test.index, columns = ['Prediction'])
    f_row = JparkerHw3Helper.calc_pred_performance(y_test, pred_calc)
    f_row.insert(0, i)
    f_accuracy.loc[len(f_accuracy)] = f_row

# QUESTION 6.2
# Did accuracy increase in any of the four drop cases vs all four features?
# No, they all did worse with less data.

# QUESTION 6.3
# Again, feature F1 contributed the greatest loss in accuracy with a drop from
# 98.7% to 82.1%.

# QUESTION 6.4
# Again, feature F4 contributed the least loss in accuracy (no loss)

# QUESTION 6.5
# Compare the results from 6.5 against 4.2