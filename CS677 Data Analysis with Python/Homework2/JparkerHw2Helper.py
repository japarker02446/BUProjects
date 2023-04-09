# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: March 29, 2022
Homework Problem 2.*

Support function to read and parse stock data from a pre-downloaded file.

WARNING: IF you are running this in an IDE you need to change the path of the
working directory manually below.  The __file__ variable is set when running
python as a script from the command line.
REFERENCE: https://stackoverflow.com/questions/16771894/python-nameerror-global-name-file-is-not-defined
"""
import operator
import os

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW2')

class JparkerHw2Helper (object):
    '''
        Helper class for Homework 2
    '''

    # Local function to map the day of the week to a numeric value.
    def day_map (day: str) -> int:
        '''
            Convert the day of week value to a numeric value.
            REFERENCE: https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
        '''
        return {
            'Monday': 1,
            'Tuesday': 2,
            'Wednesday': 3,
            'Thursday': 4,
            'Friday': 5
            }[day]
    # End def day_map

    # Load the data file for a ticker.
    def load_ticker (ticker: str) -> list:
        '''
            Load the stock data for an input ticker from the previously downloaded
            file.  Parse to date, year, weekday, adjusted closing price and percent
            change.
        '''

        input_file = ticker + '.csv'
        try:
            with open(input_file) as file:
                lines = file.read().splitlines()
            print('Opened file for ticker: ', ticker)

        except Exception as e:
            print(e)
            print('Failed to read stock data for ticker: ', ticker)

        # Parse the lines list by Year and Weekday.  Push useful values to a new list.
        # Skip the header row.
        #
        # [0] Date  - THIS IS OUR SORT VALUE
        # [1] Year  - THIS IS A KEY
        # [2] Month
        # [3] Day
        # [4] Weekday  - THIS IS A KEY
        # [5] Week_Number
        # [6] Year_Week
        # [7] Open
        # [8] High
        # [9] Low
        # [10] Close
        # [11] Volume
        # [12 Adj Close - THIS IS OUR VALUE
        # [13] Return
        # [14] Short_MA
        # [15] Long_MA
        full_list = list()
        for i in range(1, len(lines)):
            full_list.append([lines[i].split(',')[0].replace('-',''), # Date as YYYYMMDD
                              int(lines[i].split(',')[1]),            # Year as int
                              JparkerHw2Helper.day_map(lines[i].split(',')[4]),        # Numeric day of week
                              float(lines[i].split(',')[12])])        # Adj close as float

        # Calculate the daily return values.  Store positive and negative changes
        # in new lists.
        #
        # Daily return = ((close.today - close.previous) / close.previous) * 100
        #
        # Sort the parsed list by date.  This will order the values regardless of
        # weekends or holidays.
        full_list = sorted(full_list, key=operator.itemgetter(1))
        for i in range(0, len(full_list)):
            if i == 0:
                full_list[0].append(0)
            else:
                full_list[i].append(                                \
                    (                                               \
                        (full_list[i][3] - full_list[i - 1][3]) /   \
                                   full_list[i - 1][3]              \
                    ) * 100                                         \
                )
        return full_list
    # End def load_ticker

    def assign_prediction(labels: str, default_val: str, probabilities: dict) -> str:
        '''
        Return the predicted label for an input string from a dict of probabilites.

        Parameters
        ----------
        labels : str
            Input string to test.
        probabilities : dict
            Probabilities of string + 1 from the training set.

        Returns
        -------
        str
            The predicted label.
        '''
        if probabilities[labels + '+'] > probabilities[labels + '-']:
            return '+'
        elif probabilities[labels + '+'] < probabilities[labels + '-']:
            return '-'
        else:
            return default_val

    def assign_ensembl(label1: str, label2: str, label3: str) -> str:
        '''
        Calculate the ensemble label as the majority label of the three
        input labels.

        Parameters
        ----------
        label1 : str
            Input label 1.
        label2 : str
            Input label 2.
        label3 : str
            Input label 3.

        Returns
        -------
        str
            Ensemble label prediction.
        '''
        plus_count = str(label1 + label2 + label3).count('+')
        minus_count = str(label1 + label2 + label3).count('-')

        if plus_count > minus_count:
            return '+'
        else:
            return '-'