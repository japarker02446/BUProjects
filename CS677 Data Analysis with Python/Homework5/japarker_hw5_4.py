# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 15, 2022
Homework Problem 5.4

Using the saved Fetal Cardiotocography training and test data.
Use Random Forest classifier to predict class of X/Y-test.
"""
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW5')

# Import helper functions to heart data from file.
from JparkerHw5Helper import *

# Question 4.1
# Load the SAME training and test data, use Random Forest with
#   N = 1 - 10 and d = 1 -5 (50 models) to predict class labels of xtest.
# Record the error for each pair of N and d (remember, error is just 1 - accuracy)
#
# This takes more than a second, be patient.
xtrain, xtest, ytrain, ytest = JparkerHw5Helper.load_data()
rf_tracker = pd.DataFrame(columns = ['N', 'd', 'error'])
for N in range(1, 11):
    for d in range(1, 6):
        rfmodel = RandomForestClassifier(n_estimators = N, max_depth = d, \
                                         criterion = 'entropy')
        rfmodel.fit(xtrain, np.ravel(ytrain))
        ypred = rfmodel.predict(xtrain)
        [TP, FP, TN, FN, accuracy, TPR, TNR] = JparkerHw5Helper.calc_pred_performance(\
            ytest, pd.DataFrame(ypred))

        rf_tracker.loc[len(rf_tracker)] = [N, d, 1 - accuracy]

# Question 4.2
# Plot the error rates vs N for each d, find the best combination of N and d.
# REFERENCE: https://stackoverflow.com/questions/4270301/matplotlib-multiple-datasets-on-the-same-scatter-plot
# REFERENCE: https://stackoverflow.com/questions/9707676/defining-a-discrete-colormap-for-imshow-in-matplotlib
color_map = {1:'black', 2:'darkorange', 3:'limegreen', 4:'royalblue',5:'gold'}
fig = plt.figure(figsize = (11, 8.5))
ax1 = fig.add_subplot(111)

for i in range(1, 6):
    sub_track = rf_tracker.loc[rf_tracker['d'] == i]
    ax1.scatter(sub_track.N, sub_track.error, color = color_map[i], \
                marker = 'o', label = 'd ='+str(i))
    ax1.plot(sub_track.N, sub_track.error, color = color_map[i], linestyle = 'solid')
plt.xlim([0, 11])
plt.ylim([.2, 0.5])
plt.legend(loc = 'best')
plt.xlabel('Number of Subtrees (N)')
plt.ylabel('Max depth (d)')
plt.title('Plot of Random Forest Error by Subtrees and Max Depth')
plt.show()

# Question 4.3
# What is the accuracy for the beset combination of N and d?
# N = 6, d = 1, accuracy = 0.766698

# Question 4.4
# Compute the confusion matrix for best Random Forest.
rfmodel = RandomForestClassifier(n_estimators = 3, max_depth = 2, \
                                 criterion = 'entropy')
rfmodel.fit(xtrain, np.ravel(ytrain))
ypred = rfmodel.predict(xtrain)

conmat = confusion_matrix(ytest, ypred)
sns.heatmap(conmat, square = True, annot = True, fmt = 'd', cmap = 'Blues', \
            cbar = False, xticklabels = ['Negative', 'Positive'], \
            yticklabels = ['Negative', 'Positive'])

# Question 5
# In case re-running the prediction generates something different, I am
# running this here.
print("Random Forest Classifer metrics:")
JparkerHw5Helper.calc_pred_performance(ytest, pd.DataFrame(ypred))
