# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 7, 2022
Homework Problem 4.2

Load the heart failure data into a pandas data frame, run multiple linear
regression models for living and deceased patients.
"""
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.model_selection import train_test_split

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW4')

# Import helper functions to heart data from file.
from JparkerHw4Helper import *

# Question 2.1
# Load the heart failure data set from a text file to a pandas dataframe.
# Split into death event = 0 (living) or death event = 1 (dead).
# Extract modeling variables X = Creatinine phosphokinase and Y = platelets.
fail_data = JparkerHw4Helper.load_data()

# Split the data into test and train sets.
fail0 = fail_data.loc[fail_data.DEATH_EVENT == 0, \
                           ['creatinine_phosphokinase', 'platelets']]
X0_train,X0_test,y0_train, y0_test = train_test_split(fail0.iloc[:, :1], \
                                                      fail0.iloc[:, 1:2], \
                                                      test_size = 0.5, \
                                                      random_state = 1)

fail1 = fail_data.loc[fail_data.DEATH_EVENT == 1, \
                           ['creatinine_phosphokinase', 'platelets']]
X1_train,X1_test,y1_train, y1_test = train_test_split(fail1.iloc[:, :1], \
                                                      fail1.iloc[:, 1:2], \
                                                      test_size = 0.5,\
                                                      random_state = 1)

# Calculate linear regressions for the following models for living and
# deceased patients.  For each model:
#   Fit the data to xtrain
#   Print the weights (intercept, model coefficients)
#   Compute the predicte values with xtest
#   Plot predicted and actual values in xtest
#   Compute and print the loss function (SSE)

##### Model the Living
print("Modeling living subjects, Death Event = 0")
xtrain = X0_train
xtest = X0_test
ytrain = y0_train
ytest = y0_test
death_class = '0'

### 1. y = ax + b (simple linear regression)
model_text = "Model: y = ax + b (simple linear regression)"
order = 1
[intercept, coef, MSE, xtest_out, ypred] = JparkerHw4Helper.regress_linearly(\
                                                                  xtrain, \
                                                                  xtest, \
                                                                  ytrain, \
                                                                  ytest, order)

print(model_text)
print("Intercept: {:.2f}".format(intercept[0]))
for i in range(coef.size):
    print("Coefficient x^{}: {:.2E}".format(i + 1, coef[0, i]))
print("Error (SSE): {:.2E}".format(MSE * ypred.shape[0]))
print()

plot = JparkerHw4Helper.plot_linearly(xtest, ytest, ypred, model_text, death_class)
plot.show()

### 2. Quadratic
model_text = "Model: y = ax^2 + bx + c (quadratc)"
order = 2
[intercept, coef, MSE, xtest_out, ypred] = JparkerHw4Helper.regress_linearly(\
                                                                  xtrain, \
                                                                  xtest, \
                                                                  ytrain, \
                                                                  ytest, order)

print(model_text)
print("Intercept: {:.2f}".format(intercept[0]))
for i in range(coef.size):
    print("Coefficient x^{}: {:.2E}".format(i + 1, coef[0, i]))
print("Error (SSE): {:.2E}".format(MSE * ypred.shape[0]))
print()

plot = JparkerHw4Helper.plot_linearly(xtest, ytest, ypred, model_text, death_class)
plot.show()

### 3. Cubic
model_text = "Model: y = ax^3 + bx^2 + cx + d (cubic)"
order = 3
[intercept, coef, MSE, xtest_out, ypred] = JparkerHw4Helper.regress_linearly(\
                                                                  xtrain, \
                                                                  xtest, \
                                                                  ytrain, \
                                                                  ytest, order)

print(model_text)
print("Intercept: {:.2f}".format(intercept[0]))
for i in range(coef.size):
    print("Coefficient x^{}: {:.2E}".format(i + 1, coef[0, i]))
print("Error (SSE): {:.2E}".format(MSE * ypred.shape[0]))
print()

plot = JparkerHw4Helper.plot_linearly(xtest, ytest, ypred, model_text, death_class)
plot.show()

### 4. log linear
model_text = "Model: y = alog(x) + b (log linear)"
order = 1

# We need to transform Xtrain and Xtest for this one.
log_xtrain = np.log(xtrain)
log_xtest = np.log(xtest)
[intercept, coef, MSE, xtest_out, ypred] = JparkerHw4Helper.regress_linearly(\
                                                                  log_xtrain, \
                                                                  log_xtest, \
                                                                  ytrain, \
                                                                  ytest, order)

print(model_text)
print("Intercept: {:.2f}".format(intercept[0]))
for i in range(coef.size):
    print("Coefficient x^{}: {:.2E}".format(i + 1, coef[0, i]))
print("Error (SSE): {:.2E}".format(MSE * ypred.shape[0]))
print()

# Use regular (non-log) xtest for plotting.
plot = JparkerHw4Helper.plot_linearly(xtest, ytest, ypred, model_text, death_class)
plot.show()

### 5. log-log linear
model_text = "Model: log(y) = alog(x) + b (log linear)"
order = 1

# We need to transform X's and Y's for this one.
log_xtrain = np.log(xtrain)
log_xtest = np.log(xtest)
log_ytrain = np.log(ytrain)
log_ytest = np.log(ytest)
[intercept, coef, MSE, xtest_out, ypred] = JparkerHw4Helper.regress_linearly(\
                                                                  log_xtrain, \
                                                                  log_xtest, \
                                                                  log_ytrain, \
                                                                  log_ytest, order)

print(model_text)
print("Intercept: {:.2f}".format(intercept[0]))
for i in range(coef.size):
    print("Coefficient x^{}: {:.2E}".format(i + 1, coef[0, i]))
print("Error (SSE): {:.2E}".format(MSE * ypred.shape[0]))
print()

# Use regular (non-log) variables for plotting.
# Nope, gotta fix y-pred
exp_ypred = np.exp(ypred)
plot = JparkerHw4Helper.plot_linearly(xtest, ytest, exp_ypred, model_text, death_class)
plot.show()

##### Model the Dead
print("Modeling deceased subjects, Death Event = 1")
xtrain = X1_train
xtest = X1_test
ytrain = y1_train
ytest = y1_test
death_class = '1'

### 1. y = ax + b (simple linear regression)
model_text = "Model: y = ax + b (simple linear regression)"
order = 1
[intercept, coef, MSE, xtest_out, ypred] = JparkerHw4Helper.regress_linearly(\
                                                                  xtrain, \
                                                                  xtest, \
                                                                  ytrain, \
                                                                  ytest, order)

print(model_text)
print("Intercept: {:.2f}".format(intercept[0]))
for i in range(coef.size):
    print("Coefficient x^{}: {:.2E}".format(i + 1, coef[0, i]))
print("Error (SSE): {:.2E}".format(MSE * ypred.shape[0]))
print()

plot = JparkerHw4Helper.plot_linearly(xtest, ytest, ypred, model_text, death_class)
plot.show()

### 2. Quadratic
model_text = "Model: y = ax^2 + bx + c (quadratc)"
order = 2
[intercept, coef, MSE, xtest_out, ypred] = JparkerHw4Helper.regress_linearly(\
                                                                  xtrain, \
                                                                  xtest, \
                                                                  ytrain, \
                                                                  ytest, order)

print(model_text)
print("Intercept: {:.2f}".format(intercept[0]))
for i in range(coef.size):
    print("Coefficient x^{}: {:.2E}".format(i + 1, coef[0, i]))
print("Error (SSE): {:.2E}".format(MSE * ypred.shape[0]))
print()

plot = JparkerHw4Helper.plot_linearly(xtest, ytest, ypred, model_text, death_class)
plot.show()

### 3. Cubic
model_text = "Model: y = ax^3 + bx^2 + cx + d (cubic)"
order = 3
[intercept, coef, MSE, xtest_out, ypred] = JparkerHw4Helper.regress_linearly(\
                                                                  xtrain, \
                                                                  xtest, \
                                                                  ytrain, \
                                                                  ytest, order)

print(model_text)
print("Intercept: {:.2f}".format(intercept[0]))
for i in range(coef.size):
    print("Coefficient x^{}: {:.2E}".format(i + 1, coef[0, i]))
print("Error (SSE): {:.2E}".format(MSE * ypred.shape[0]))
print()

plot = JparkerHw4Helper.plot_linearly(xtest, ytest, ypred, model_text, death_class)
plot.show()

### 4. log linear
model_text = "Model: y = alog(x) + b (log linear)"
order = 1

# We need to transform Xtrain and Xtest for this one.
log_xtrain = np.log(xtrain)
log_xtest = np.log(xtest)
[intercept, coef, MSE, xtest_out, ypred] = JparkerHw4Helper.regress_linearly(\
                                                                  log_xtrain, \
                                                                  log_xtest, \
                                                                  ytrain, \
                                                                  ytest, order)

print(model_text)
print("Intercept: {:.2f}".format(intercept[0]))
for i in range(coef.size):
    print("Coefficient x^{}: {:.2E}".format(i + 1, coef[0, i]))
print("Error (SSE): {:.2E}".format(MSE * ypred.shape[0]))
print()

# Use regular (non-log) xtest for plotting.
plot = JparkerHw4Helper.plot_linearly(xtest, ytest, ypred, model_text, death_class)
plot.show()

### 5. log-log linear
model_text = "Model: log(y) = alog(x) + b (log linear)"
order = 1

# We need to transform X's and Y's for this one.
log_xtrain = np.log(xtrain)
log_xtest = np.log(xtest)
log_ytrain = np.log(ytrain)
log_ytest = np.log(ytest)
[intercept, coef, MSE, xtest_out, ypred] = JparkerHw4Helper.regress_linearly(\
                                                                  log_xtrain, \
                                                                  log_xtest, \
                                                                  log_ytrain, \
                                                                  log_ytest, order)

print(model_text)
print("Intercept: {:.2f}".format(intercept[0]))
for i in range(coef.size):
    print("Coefficient x^{}: {:.2E}".format(i + 1, coef[0, i]))
print("Error (SSE): {:.2E}".format(MSE * ypred.shape[0]))
print()

# Use regular (non-log) variables for plotting.
# Nope, gotta fix y-pred
exp_ypred = np.exp(ypred)
plot = JparkerHw4Helper.plot_linearly(xtest, ytest, exp_ypred, model_text, death_class)
plot.show()
