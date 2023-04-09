# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 1, 2022
Homework Problem 3.2

Read and plot real vs fake bank note data from UCI Data Set repository.
Devise a simple classification model by visual examination of the plot data.
"""
import os
import pandas as pd
import seaborn as sns
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

# QUESTION 2.1
# Split the data into Xtrain and Xtest parts (50/50).  Use the seaborn pairplot
# function to plot pairwise relationships of Xtrain for Class 0 and Class 1.
# Save each plot as a PDF file.
X = note_data.iloc[:, :4]
y = note_data.Class
X_train,X_test,y_train, y_test = train_test_split(X, y, test_size = 0.5,\
                                                  random_state = 1,\
                                                  stratify = y)

sns.pairplot(X_train.loc[note_data.Class == 0]).savefig('japarker_hw3_good_bills.pdf')
sns.pairplot(X_train.loc[note_data.Class == 1]).savefig('japarker_hw3_fake_bills.pdf')

# QUESTION 2.2
# Visually examine the results and derive three simple comparisons to identify
#   a fake bill.
# Based on a visual examination of the plotted data I selected a simple classifier
#   of: F1 >= 0 and F2 >= 5 and F3 <= 5. This was implemented in the function
#   JparkerHw3Helper.simple_simple_classifier.

# QUESTION 2.3
# Apply your simple classifer to Xtest and compute predicted class labels.
for i in X_test.index:
    X_test.loc[i, 'Simple'] = JparkerHw3Helper.simple_classifier(X_test.loc[i, :])

# QUESTION 3.4
# Compare the predicted labels with the true labels.
#
# Extract the predictions from the Simple Classifier as a series.
# Convert the prediction values to the Notes classifier values.
pred_series = pd.DataFrame([0 if c == 'good' else 1 for c in X_test.Simple], \
                           index = X_test.index, columns = ['Prediction'])

# Pass the prediction values and the truth values to the Accuracy Calculator.
# The list returned is: TP, FP, TN, FN, accuracy, TPR, TNR
simple_accuracy = JparkerHw3Helper.calc_pred_performance(y_test, pred_series)

# QUESTION 3.5
# Summarize the accuracy metrics in a table.
print("Simple Predictor:")
print("TP:", simple_accuracy[0], end=',')
print(" FP:", simple_accuracy[1], end=',')
print(" TN:", simple_accuracy[2], end=',')
print(" FN:", simple_accuracy[3], end=',')
print(" Acc: {:.3f}".format(simple_accuracy[4]), end=',')
print(" TPR: {:.3f}".format(simple_accuracy[5]), end=',')
print(" TNR: {:.3f}".format(simple_accuracy[6]))

# QUESTION 3.6
# Is the simple classifier give higher accuracy on idneitfying fake bills or
# real bills? (TPR vs TNR)
# Does the simple classifier give higher accuracy than random (50%)?
# It does pretty good (Accuracy = 68.8%).
