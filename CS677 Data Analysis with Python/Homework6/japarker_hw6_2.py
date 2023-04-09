# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 24, 2022
Homework Problem 6.2

For question 2, use the same train and test data split as for question 1.
Calculate accuracy and confusion matrix for a classifier of choice.

I will use logistic regression for this question.

Label selection:
    8 % 3 = 2
    Use Class L = 1 (negative) and L = 3 (positive)
"""
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW6')

# Import helper functions to seed data from file.
from JparkerHw6Helper import *

### Question 2
# Load the data, subset to class labels 1 and 3.
(xtrain, xtest, ytrain, ytest)= JparkerHw6Helper.load_train_test()

# Execute logistic regression on this data set.
log_reg = LogisticRegression()
log_reg.fit(xtrain, np.ravel(ytrain))
ypred = log_reg.predict(xtest)

logistic_performance = JparkerHw6Helper.calc_pred_performance(ytest, \
                            pd.DataFrame(ypred, index = xtest.index), 3, 1)
print("Logistic Regression Accuracy: {:.3f}".format(logistic_performance[4]))

ax = plt.subplot()
conmat = confusion_matrix(ytest, ypred)
sns.heatmap(conmat, square = True, annot = True, fmt = 'd', ax = ax, \
            xticklabels = ['Negative', 'Positive'], \
            yticklabels = ['Negative', 'Positive'], \
            cmap = 'Blues', cbar = False)
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Logistic Regression Confusion Matrix')
plt.show()
