"""
Jefferson Parker
Class: CS 677
Date: April 15, 2022
Homework Problem 5.*

Support functions for Homework 5.

WARNING: IF you are running this in an IDE you need to change the path of the
working directory manually below.  The __file__ variable is set when running
python as a script from the command line.
REFERENCE: https://stackoverflow.com/questions/16771894/python-nameerror-global-name-file-is-not-defined
"""
import os
from os.path import exists
import pandas as pd
from sklearn.model_selection import train_test_split

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW5')

class JparkerHw5Helper (object):
    '''
    Helper class for Homework 5.
    '''

    def load_data():
        '''
        Load the SPLIT fetal data set Xtrain, Xtest, Ytrain and Ytest for reuse
        across multiple problems.

        If the data has not been split, filter to our columns of interest and
        split it into training and test sets, save these as files.

        If the data has been split, load the split data sets from files.

        Returns xtrain, xtest, ytrain and ytest.
        '''
        # If the data file has been split into training and test sets, load them.
        if exists("xtrain.csv"):
            xtrain = pd.read_csv("xtrain.csv")
            ytrain = pd.read_csv("ytrain.csv")
            xtest = pd.read_csv("xtest.csv")
            ytest = pd.read_csv("ytest.csv")

        # If the data file has not been split: read it in, subset to desired
        # columns and split to training and test sets.
        # Save training and test sets as files.
        #
        # This is "technically" part of the answer to question 5.2.1.
        else:
            try:
                xldf = pd.read_csv("GTG_clean.csv")
            except FileNotFoundError:
                print ("ERROR: Please run japarker_hw5_1.py to generate",\
                       "cleaned data file GTG_clean.csv")

            xldf = xldf.loc[:, ['LB', 'ALTV', 'Min', 'Mean', 'class_label']]
            xtrain, xtest, ytrain, ytest = train_test_split(\
                                    xldf.loc[:, ['LB', 'ALTV', 'Min', 'Mean']],\
                                    xldf.loc[:, ['class_label']],\
                                    test_size = 0.5, random_state = 9)
            xtrain.to_csv("xtrain.csv", index = False)
            ytrain.to_csv("ytrain.csv", index = False)
            xtest.to_csv("xtest.csv", index = False)
            ytest.to_csv("ytest.csv", index = False)

        return(xtrain, xtest, ytrain, ytest)
    # End load_data

    # Recycling calc_pred_performance from HW3, becuase OOP does it like that.
    #
    # Compute [True|False][Positive|Negative] counts, True Positive Rate
    #   (Sensitivity) and True Negative Rate (Specificity)
    def calc_pred_performance(truth_vector, prediction_vector) -> list:
        '''
        Compare two vectors of values, truth and prediction, to determine
        [True|False][Positive|Negative] counts, True Positive Rate (Sensitivity)
        and True Negative Rate (Specificity)

        Be sure to normalize values for True and False before calling the function.

        Parameters
        ----------
        truth_vector : TYPE
            Iterable of TRUTH values.
        prediction_vector : TYPE
            Iterable of PREDICTED values.

        Returns
        -------
        list
            Returns a list of TP, FP, TN, FN, Accuracy, TPR (Sensitivity) and TNR
            (Specificity)
        '''

        # Merge the input vectors into a DataFrame.
        # Note, this assumes the two vectors have the same index.
        calc_table = pd.DataFrame(prediction_vector).merge(truth_vector, \
                                                           left_index = True, \
                                                           right_index = True)
        calc_table.columns = ['Prediction', 'Truth']

        # Create empty counter columns of ZEROS.
        calc_table['TP'] = 0
        calc_table['FP'] = 0
        calc_table['TN'] = 0
        calc_table['FN'] = 0

        # For all the things.
        for i in calc_table.index:

            # Positive prediction (TP, FP)
            if calc_table.loc[i, 'Prediction'] == 0:
                if calc_table.loc[i, 'Prediction'] == calc_table.loc[i, 'Truth']:
                    calc_table.loc[i, 'TP'] = 1
                else:
                    calc_table.loc[i, 'FP'] = 1

            # Negative prediction (TN, FN)
            else:
                if calc_table.loc[i, 'Prediction'] == calc_table.loc[i, 'Truth']:
                    calc_table.loc[i, 'TN'] = 1
                else:
                    calc_table.loc[i, 'FN'] = 1

        # Quantify the total counts of TP, FP, TN, FN.
        # Calculate Accuracy, TPR, TNR.
        # Return the sums and rates as a list.
        TP = sum(calc_table.TP)
        FP = sum(calc_table.FP)
        TN = sum(calc_table.TN)
        FN = sum(calc_table.FN)

        # OY! MATH!
        try:
            accuracy = (TP + TN) / (TP + FP + TN + FN)
        except ZeroDivisionError:
            accuracy = 0
        try:
            TPR = TP / (TP + FN)
        except ZeroDivisionError:
            TPR = 0
        try:
            TNR = TN / (TN + FP)
        except ZeroDivisionError:
            TNR = 0

        return list([TP, FP, TN, FN, accuracy, TPR, TNR])
    # End calc_pred_performance
