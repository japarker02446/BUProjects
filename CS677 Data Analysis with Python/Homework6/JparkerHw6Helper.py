# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 24, 2022
Homework Problem 6.*

Support functions for Homework 6.

WARNING: IF you are running this in an IDE you need to change the path of the
working directory manually below.  The __file__ variable is set when running
python as a script from the command line.
REFERENCE: https://stackoverflow.com/questions/16771894/python-nameerror-global-name-file-is-not-defined
"""
import os
import pandas as pd

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW6')

class JparkerHw6Helper (object):
    '''
    Helper class for Homework 6.
    '''

    def load_data ():
        '''
        Load the seeds data set from a csv file to a pandas dataframe.
        NOTE - the source seeds dataset from the UCI web page was pre-processed
        by course staff to improperly formatted data fields.

        For some reason, the file was labeled 'csv' (comma separated value) but
        it was actually a tab delimited file.  I reformatted this to an actual
        csv file.

        Returns
        -------
        Pandas DataFrame with seeds data with column names.
        '''
        try:
            seeds_df = pd.read_csv("seeds_dataset.csv", header = None)
        except FileNotFoundError:
            print("ERROR: Could not find file seeds_dataset.csv")

        seeds_df.columns = ['area', 'perimeter', 'compactness', 'kernel_length', \
                            'kernel_width', 'assymetry', 'groove_length', 'class']
        return seeds_df
    # End load_data.

    def load_train_test ():
        '''
        Load previously generated training and test data sets for reuse.

        Returns
        -------
        Training and test datasets (xtrain, xtest, ytrain, ytest)
        '''
        try:
            xtrain = pd.read_csv("xtrain.csv")
            ytrain = pd.read_csv("ytrain.csv")
            xtest = pd.read_csv("xtest.csv")
            ytest = pd.read_csv("ytest.csv")
        except FileNotFoundError:
            print("ERROR: Could not find training and test data files.")

        return (xtrain, xtest, ytrain, ytest)
    # End load_train_test.

    # Compute [True|False][Positive|Negative] counts, True Positive Rate
    #   (Sensitivity) and True Negative Rate (Specificity)
    def calc_pred_performance(truth_vector, prediction_vector, positive, \
                              negative) -> list:
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
        positive:
            The value considered "positive"
        negative:
            The value considered "negative"

        Returns
        -------
        list
            Returns a list of TP, FP, TN, FN, Accuracy, TPR (Sensitivity) and TNR
            (Specificity)
        '''

        # Merge the input vectors into a DataFrame.
        # Note, this assumes the two vectors have the same index.
        if (truth_vector.index != prediction_vector.index).all():
            raise ValueError("Index of truth and prediction vectors is not equal.")
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
            if calc_table.loc[i, 'Prediction'] == positive:
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