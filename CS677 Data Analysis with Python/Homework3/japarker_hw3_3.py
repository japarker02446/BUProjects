# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 1, 2022
Homework Problem 3.3

Read and plot real vs fake bank note data from UCI Data Set repository.
Implement k-NN classifier to predict bill authenticity.
"""
import matplotlib.pyplot as plt
import os
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
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
# Using the same randome_state value should give us the same split as before.
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

# Side note: I was a little thrown off and then concerned that two different
#   scaling methods were listed in the example code from class.  Turns out this
#   is a feature of the StandardScaler and not a bug.  The fit_transform
#   measures the mean and SD of the data from the training data.  The
#   transform function applies the scaling to the test data using the SAME
#   PARAMETERS.
#
#   smaht.

# QUESTION 3.1.
# For k = 3,5,7,9,11 use our Xtrain and Xtest to train a k-NN classifier.
# Build a table of k values vs prediction metrics.
k_accuracy = pd.DataFrame(columns = \
                          ['k', 'TP', 'FP', 'TN', 'FN', 'accuracy', 'TPR', 'TNR'])

for i in [3,5,7,9,11]:
    print ("I is ",i)
    classifier = KNeighborsClassifier(n_neighbors = i, p = 2, metric = 'euclidean')
    classifier.fit(X_train_sc, y_train)
    y_pred = classifier.predict(X_test_sc)

    pred_calc = pd.DataFrame(y_pred, index = X_test.index, columns = ['Prediction'])
    k_row = JparkerHw3Helper.calc_pred_performance(y_test, pred_calc)
    k_row.insert(0, i)
    k_accuracy.loc[len(k_accuracy)] = k_row

    # My function calculates the same accuracy (I checked)
    # k_onfoosed = confusion_matrix(y_test, y_pred)
    # print(accuracy_score(y_test, y_pred))

# QUESTION 3.2.
# Plot a graph of k vs accuracy for each k.
# Good thing I have these in a table.
plt.plot(k_accuracy.k, k_accuracy.accuracy)
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.title('k-NN Prediction Accuracy for Bill Authenticity Data')

# QUESTION 3.3
# Use the optimal k* to calculate performance metrics.
k_accuracy.loc[1]

# QUESTION 3.4
# Is the k-NN classifier better than the simple classifier for any measures?

# QUESTION 3.5
# Consider a bill with feature values corresponding to the last four digits of
# your BU ID.  What is the class label predicted for this bill using the simple
# classifier and the k-NN with k* = 5?
bu_pred_simple = JparkerHw3Helper.simple_simple_classifier(8, 9, 2, 8)

classifier = KNeighborsClassifier(n_neighbors = 5, p = 2, metric = 'euclidean')
classifier.fit(X_train_sc, y_train)
y_pred = classifier.predict(sc_X.transform([[8,9,2,8]]))

# Both are good!
