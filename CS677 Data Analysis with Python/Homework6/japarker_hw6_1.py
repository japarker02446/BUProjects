# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 24, 2022
Homework Problem 6.1

For question 1, subset the dataset to two of the three class labels based on
the last digit of your BU ID (last_digit % 3).  Split the data 50/50 into
training and test sets.  Use SVM to predict classes.

Calculate accuracy and confusion matrix for three kernels of SVM.

Label selection:
    8 % 3 = 2
    Use Class L = 1 (negative) and L = 3 (positive)
"""
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW6')

# Import helper functions to seed data from file.
from JparkerHw6Helper import *

### Question 1
# Load the data, subset to class labels 1 and 3.
seed_df = JparkerHw6Helper.load_data()
sub_df = seed_df.loc[seed_df['class'].isin([1,3])]

# Split the data 50/50 into training and test sets.
xtrain, xtest, ytrain, ytest = train_test_split(\
                        sub_df.loc[:, ['area', 'perimeter', 'compactness', \
                                     'kernel_length', 'kernel_width',
                                     'assymetry', 'groove_length']],\
                        sub_df.loc[:, ['class']],\
                        test_size = 0.5, random_state = 5)

# Save the training and test sets to files for later use (Question 2).
xtrain.to_csv("xtrain.csv", index = False)
ytrain.to_csv("ytrain.csv", index = False)
xtest.to_csv("xtest.csv", index = False)
ytest.to_csv("ytest.csv", index = False)

# Question 1.1
# Implement linear kernel SVM.  Calculate accuracy and confusion matrix.
# NOTE - Changing the value of c from 10 to 1 improved accuracy by 2%
xtrain_scaled = StandardScaler().fit_transform(xtrain)
xtest_scaled = StandardScaler().fit_transform(xtest)

c = 1
linear_svm = svm.LinearSVC(C = c, loss = "hinge")
linear_svm.fit(xtrain_scaled, np.ravel(ytrain))
ypred = linear_svm.predict(xtest_scaled)
linear_svm_performance = JparkerHw6Helper.calc_pred_performance(ytest, \
                            pd.DataFrame(ypred, index = xtest.index), 3, 1)
print("Linear SVM Accuracy: {:.3f}".format(linear_svm_performance[4]))

ax = plt.subplot()
conmat = confusion_matrix(ytest, ypred)
sns.heatmap(conmat, square = True, annot = True, fmt = 'd', ax = ax, \
            xticklabels = ['Negative', 'Positive'], \
            yticklabels = ['Negative', 'Positive'], \
            cmap = 'Blues', cbar = False)
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Linear SVM Confusion Matrix')
plt.show()

# Question 1.2
# Implement Gaussian kernel SVM.  Calculate accuracy and confusion matrix.
xtrain_scaled = StandardScaler().fit_transform(xtrain)
xtest_scaled = StandardScaler().fit_transform(xtest)

gauss_svm = svm.SVC(kernel = 'rbf')
gauss_svm.fit(xtrain_scaled, np.ravel(ytrain))
ypred = gauss_svm.predict(xtest_scaled)
gaussian_svm_performance = JparkerHw6Helper.calc_pred_performance(ytest, \
                            pd.DataFrame(ypred, index = xtest.index), 3, 1)
print("Gaussian SVM Accuracy: {:.3f}".format(gaussian_svm_performance[4]))

ax = plt.subplot()
conmat = confusion_matrix(ytest, ypred)
sns.heatmap(conmat, square = True, annot = True, fmt = 'd', ax = ax, \
            xticklabels = ['Negative', 'Positive'], \
            yticklabels = ['Negative', 'Positive'], \
            cmap = 'Blues', cbar = False)
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Gaussian SVM Confusion Matrix')
plt.show()

# Question 1.3
# Implement polynomial kernel (degree = 3) SVM.  Calculate accuracy and
#   confusion matrix.
xtrain_scaled = StandardScaler().fit_transform(xtrain)
xtest_scaled = StandardScaler().fit_transform(xtest)

poly_svm = svm.SVC(kernel = 'poly', degree = 3)
poly_svm.fit(xtrain_scaled, np.ravel(ytrain))
ypred = poly_svm.predict(xtest_scaled)
polynomial_svm_performance = JparkerHw6Helper.calc_pred_performance(ytest, \
                            pd.DataFrame(ypred, index = xtest.index), 3, 1)
print("Polynomial SVM Accuracy: {:.3f}".format(polynomial_svm_performance[4]))

ax = plt.subplot()
conmat = confusion_matrix(ytest, ypred)
sns.heatmap(conmat, square = True, annot = True, fmt = 'd', ax = ax, \
            xticklabels = ['Negative', 'Positive'], \
            yticklabels = ['Negative', 'Positive'], \
            cmap = 'Blues', cbar = False)
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Polynomial SVM Confusion Matrix')
plt.show()