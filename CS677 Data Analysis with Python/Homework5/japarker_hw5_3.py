# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 15, 2022
Homework Problem 5.3

Using the saved Fetal Cardiotocography training and test data.
Use Decision Tree classifier to predict class of X/Y-test.
"""
import os
import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW5')

# Import helper functions to heart data from file.
from JparkerHw5Helper import *

# Question 3.1
# Load the SAME training and test data, use Decision tree to predict class
#   labels of xtest.
xtrain, xtest, ytrain, ytest = JparkerHw5Helper.load_data()
treemod = DecisionTreeClassifier()
treemod.fit(xtrain, ytrain)
ypred = treemod.predict(xtest)

# Question 3.2
# What is the accuracy for the Decision Tree classifier from 3.1?
[TP, FP, TN, FN, accuracy, TPR, TNR] = JparkerHw5Helper.calc_pred_performance(\
    ytest, pd.DataFrame(ypred))
print ("The accuracy for the Decision Tree classifier is: {:.3f}".format(accuracy))

# Question 3.3
# Compute the confusion matrix for the Decision Tree classifier from 3.1.
# confusion matrix.
conmat = confusion_matrix(ytest, ypred)
sns.heatmap(conmat, square = True, annot = True, fmt = 'd', cmap = 'Blues', \
            cbar = False, xticklabels = ['Negative', 'Positive'], \
            yticklabels = ['Negative', 'Positive'])

# Question 5
# In case re-running the prediction generates something different, I am
# running this here.
print("Decision Tree Classifer metrics:")
JparkerHw5Helper.calc_pred_performance(ytest, pd.DataFrame(ypred))
