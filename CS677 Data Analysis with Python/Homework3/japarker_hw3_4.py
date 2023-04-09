# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 1, 2022
Homework Problem 3.4

Read and plot real vs fake bank note data from UCI Data Set repository.
Implement k-NN classifier to predict bill authenticity with dropped features
F1, F2, F3 or F4.
"""
import numpy as np
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

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

# We will be calculating Euclidian distances for k-NN classification, so we
# need to scale the data.
sc_X = StandardScaler()
X_train_sc = sc_X.fit_transform(X_train)
X_test_sc = sc_X.transform(X_test)

# QUESTION 4.1.
# For k* = 5 use our Xtrain and Xtest to train a k-NN classifier.
# This time, serially drop one of the features (F1, F2, F3 or F4) from Xtrain
#   and Xtest.  Measure and record the accuracy of each new model.
#
# Build a table of k values vs prediction metrics.
f_accuracy = pd.DataFrame(columns = \
                          ['Feature', 'TP', 'FP', 'TN', 'FN', 'accuracy', 'TPR', 'TNR'])

for i in range(4):
    X_train_drop = np.delete(X_train_sc, i, axis = 1)
    X_test_drop = np.delete(X_test_sc, i, axis = 1)

    classifier = KNeighborsClassifier(n_neighbors = 5, p = 2, metric = 'euclidean')
    classifier.fit(X_train_drop, y_train)
    y_pred = classifier.predict(X_test_drop)

    pred_calc = pd.DataFrame(y_pred, index = X_test.index, columns = ['Prediction'])
    f_row = JparkerHw3Helper.calc_pred_performance(y_test, pred_calc)
    f_row.insert(0, 'F' + str( i + 1))
    f_accuracy.loc[len(f_accuracy)] = f_row

# QUESTION 4.2
# The accuracy with all four features and k = 5 was 1 (which is odd, since
# that is perfect) so no, the accuracy did not increase in any of the drop cases.

# QUESTION 4.3
# Feature F1 contributed the greatest loss of accuracy, from 1 to 0.961,
# indicating it is likely the most important for classification.

# QUESTION 4.4
# Feature F4 contributed the least loss of accuracy, from 1 to 0.998, meaning
# it is the least meaningful for classificaiton.
