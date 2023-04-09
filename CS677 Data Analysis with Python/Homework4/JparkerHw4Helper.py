# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 7, 2022
Homework Problem 4.*

Support functions for Homework 4.

WARNING: IF you are running this in an IDE you need to change the path of the
working directory manually below.  The __file__ variable is set when running
python as a script from the command line.
REFERENCE: https://stackoverflow.com/questions/16771894/python-nameerror-global-name-file-is-not-defined
"""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import os
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW4')

class JparkerHw4Helper (object):
    '''
    Helper class for Homework 3.
    '''

    def load_data ():
        '''
        Load the heart failure data set from a csv file to a pandas dataframe.
        Returns
        -------
        Pandas DataFrame with banknote data with column names.
        '''
        heart_data = pd.DataFrame()
        heart_data = pd.read_csv("heart_failure_clinical_records_dataset.csv")
        return heart_data
    # End load_data.

    def regress_linearly (xtrain, xtest, ytrain, ytest, order:int = 1) -> list:
        '''
        Implement linear regression training and testing with a model of
        degree order (order > 1 is a polynomial model).

        Return the model parameters (intercept, coefficient weights), error as
        MSE and predicted values.

        Parameters
        ----------
        xtrain : TYPE
            Independent variable object for training.
        xtest : TYPE
            Independent variable object for testing.
        ytrain : TYPE
            Dependent variable (vector) for training.
        ytest : TYPE
            Dependent variable (vector) for testing.
        order : int
            Integer value of the polynomial order of the desired model.

        Returns
        -------
        Return a list of the model parameters (intercept, coefficient weights),
        error as MSE, transformed xtest values and predicted y values.
        '''

        # Make a linear regression object, transform the training data to the
        # desired polynomial degree.
        model = LinearRegression()
        poly = PolynomialFeatures(order, include_bias = False)
        xtrain = poly.fit_transform(xtrain)

        # Fit the training data to the model, calculate the predicted values.
        model.fit(xtrain, ytrain)
        xtest = poly.fit_transform(xtest)
        ypred = model.predict(xtest)

        # Compute the error and return the important bits.
        MSE = metrics.mean_squared_error(ytest, ypred)

        return [model.intercept_, model.coef_, MSE, xtest, ypred]
    # End regress_linearly


    def plot_linearly (xtest, ytest, ypred, plot_text: str, death_class: str()):
        '''
        Plot test X values vs actual and predicted Y values.
        REFERENCE: https://matplotlib.org/stable/gallery/text_labels_and_annotations/custom_legends.html
        REFERENCE: https://stackoverflow.com/questions/7045729/automatically-position-text-box-in-matplotlib

        Parameters
        ----------
        xtest : TYPE
            Vector of X values (possibly multi-dimensional).
        ytest : TYPE
            Vector of actual (test) dependent variable values.
        ypred : TYPE
            Vector of predicted dependent variable values.
        plot_text: str
            Annotation string to print on the plot.
        death_class: str
            Annotation to add to the label.

        Returns
        -------
       A matplot.pyplot object.
        '''
        # Gettin' plotty with it.
        plt.figure(figsize = (11, 8.5))
        plt.plot(xtest.sum(axis = 1), ytest, 'k.')
        plt.plot(xtest.sum(axis = 1), ypred, 'g.')
        legend_elements = [Line2D([0],[0], marker = 'o', color = 'k', \
                                  label = 'Y-Test'), \
                           Line2D([0],[0], marker = 'o', color = 'g', \
                                                     label = 'Y-Predicted')]
        plt.legend(handles = legend_elements, loc = 'best')
        plt.annotate(plot_text, xy=(0.05, 0.90), xycoords='axes fraction')
        plt.xlabel ('Creatinine phosphokinase (CPK)')
        plt.ylabel ('Platelet count')
        plt.title ('Scatterplot of Predicted Values for Death Event ='+death_class)
        return plt
    # End plot_linearly