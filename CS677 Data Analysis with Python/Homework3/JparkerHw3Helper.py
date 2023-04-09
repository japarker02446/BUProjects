# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 1, 2022
Homework Problem 3.*

Support functions for Homework 3.

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
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW3')

class JparkerHw3Helper (object):
    '''
    Helper class for Homework 3.
    '''

    def load_note_data ():
        '''
        Load the banknote data set from a text file to a pandas dataframe.
        NOTE - the file is saved with .txt extension but if you open it you can
          clearly see that it is a CSV (comma separated value) file.
        Returns
        -------
        Pandas DataFrame with banknote data with column names.
        '''
        note_data = pd.DataFrame()
        note_data = pd.read_csv("data_banknote_authentication.txt", \
                                header = None, \
                                names=['F1', 'F2', 'F3','F4','Class']
                    )
        return note_data
    # End load_note_data.

    # Implement the "simple classifier" from homework question 3.2
    def simple_simple_classifier(F1: float, F2: float, F3: float, *F4) -> str:
        '''
        Simple bill classifier based on visual inspection of training data for good
        and bad bills.

        Parameters
        ----------
        F1 : float
            Bank note data parameter F1.
        F2 : float
            Bank note data parameter F2.
        F3 : float
            Bank note data parameter F3.
        *F4 : TYPE
            Bank note data parameter F4 (optional).

        Returns
        -------
        str
            Classification selection, 'good' if predicted as authentic bill,
            'fake' if predicted to be counterfeit.
        '''
        if F1 >= 0 and F2 >= 5 and F3 <= 5:
            return 'good'
        else:
            return 'fake'
    # End simple_simple_classifier

    def simple_classifier(series) -> str:
        '''


        Parameters
        ----------
        series : TYPE
            Pandas Series objects representing one row of bill classifier data.

        Returns
        -------
        str
            Classification selection, 'good' if predicted as authentic bill,
            'fake' if predicted to be counterfeit.
        '''
        return(JparkerHw3Helper.simple_simple_classifier(\
                                        float(series['F1']), \
                                        float(series['F2']), \
                                        float(series['F3'])  \
                                        )                    \
               )
    # End simple_classifier

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