# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 15, 2022
Homework Problem 5.2

Split the data set 50/50 into training and test sets.
Save the data for later use throughout the problem set.

Use Naive Bayes classifier to predict class of X/Y-test.
"""
import os
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW5')

# Import helper functions to heart data from file.
from JparkerHw5Helper import *

# Question 2.1
#
# The 50/50 split of the data into training and test is implemented in the
# load_data() function of JparkerHw5Helper.py.
xtrain, xtest, ytrain, ytest = JparkerHw5Helper.load_data()

# Create the Naive Bayes Classifier and predict classes for X/Ytest
# NOTE - need to use the Numpy ravel function to flatten the pandas series
#   ytest to a 1D array.
nbmodel = MultinomialNB()
nbmodel.fit(xtrain, np.ravel(ytrain))
ypred = nbmodel.predict(xtest)

# Question 2.2
# What is the accuracy for the NB classifier from 2.1?
[TP, FP, TN, FN, accuracy, TPR, TNR] = JparkerHw5Helper.calc_pred_performance(\
    ytest, pd.DataFrame(ypred))
print ("The accuracy for the NB classifier is: {:.3f}".format(accuracy))

# Question 2.3
# Compute the confusion matrix for the NB classifier from 2.1.
# confusion matrix.
conmat = confusion_matrix(ytest, ypred)
sns.heatmap(conmat, square = True, annot = True, fmt = 'd', cmap = 'Blues', \
            cbar = False, xticklabels = ['Negative', 'Positive'], \
            yticklabels = ['Negative', 'Positive'])

# Question 5
# In case re-running the prediction generates something different, I am
# running this here.
print("Naive Bayes classifier metrics:")
JparkerHw5Helper.calc_pred_performance(ytest, pd.DataFrame(ypred))