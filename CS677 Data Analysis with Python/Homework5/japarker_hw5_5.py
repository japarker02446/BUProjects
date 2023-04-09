# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 15, 2022
Homework Problem 5.5

Construct the model performance table and discuss the results for Naive Bayes,
Decision Tree and Random Forst (best N and d).  Discuss findings.
"""
import numpy as np
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW5')

# Import helper functions to heart data from file.
from JparkerHw5Helper import *

# Load the SAME training and test data, re-run Naive Bayes, Decision Tree,
# Random Forest (N = 2, d = 1) and generate the performance metrics table.
xtrain, xtest, ytrain, ytest = JparkerHw5Helper.load_data()

model_accuracy = pd.DataFrame(columns = \
                          ['model', 'TP', 'FP', 'TN', 'FN', 'accuracy', 'TPR', 'TNR'])

# Naive Bayes
nbmodel = MultinomialNB()
nbmodel.fit(xtrain, np.ravel(ytrain))
ypred = nbmodel.predict(xtest)

acc_row = JparkerHw5Helper.calc_pred_performance(ytest, pd.DataFrame(ypred))
acc_row.insert(0, 'Naive Bayes')
model_accuracy.loc[len(model_accuracy)] = acc_row

# Decision Tree
treemod = DecisionTreeClassifier()
treemod.fit(xtrain, ytrain)
ypred = treemod.predict(xtest)

acc_row = JparkerHw5Helper.calc_pred_performance(ytest, pd.DataFrame(ypred))
acc_row.insert(0, 'Decision Tree')
model_accuracy.loc[len(model_accuracy)] = acc_row

# Random Forest
rfmodel = RandomForestClassifier(n_estimators = 2, max_depth = 1, criterion =\
                                 'entropy')
rfmodel.fit(xtrain, np.ravel(ytrain))
ypred = rfmodel.predict(xtrain)

acc_row = JparkerHw5Helper.calc_pred_performance(ytest, pd.DataFrame(ypred))
acc_row.insert(0, 'Random Forest (N = 6, d = 1)')
model_accuracy.loc[len(model_accuracy)] = acc_row
