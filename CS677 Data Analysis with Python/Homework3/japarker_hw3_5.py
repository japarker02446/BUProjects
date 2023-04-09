# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 1, 2022
Homework Problem 3.5

Read and plot real vs fake bank note data from UCI Data Set repository.
Implement logistic regression to predict bill authenticity.
"""
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

# QUESTION 5.1
# Use the same Xtrain and Xtest as before.  Run predictions using logistic
# regression and compute the accuracy.
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred = log_reg.predict(X_test)

# QUESTION 5.2
# Summarize the performance measures in the table.
pred_calc = pd.DataFrame(y_pred, index = X_test.index, columns = ['Prediction'])
log_row = JparkerHw3Helper.calc_pred_performance(y_test, pred_calc)

# QUESTION 5.3
# Is the logistic regression better than the simple classifier of Q.2.5?
# Yes, the simple classifier had an accuracy of 68.8%  while logistic
# regression gave 98.7%.

# QUESTION 5.4
# Is the logistic regression better than k-NN with k* = 5?
# No, the k-NN accuracy was 1 (100%), which still worries me.

# QUESTION 5.5
# What is the class label for our BU ID bill?  Is it hte same as predicted by
# k-NN?
buid_pred = log_reg.predict([[8,9,2,8]])

# Predicted a good bill (class 0), this is the same.
